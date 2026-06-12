#!/usr/bin/env python3
"""Run proxy ablation analysis for xGASS."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bdvr1.config import OUTPUT_TABLES, XGASS_PATHS
from bdvr1.io import read_table, write_table
from bdvr1.proxies import compute_proxy_variant, assign_quartiles
from bdvr1.statistics import (
    q4_q1_ratio,
    spearman_proxy_abs_residual,
    bootstrap_q4_q1,
)


ABLATION_VARIANTS = [
    "full", "incl_fatm_no_w50", "w50_fatm_no_incl",
    "incl_only", "w50_only", "gas_only",
    "no_raw_w50", "no_incl", "no_gas",
]


def main():
    proxy_path = XGASS_PATHS["proxy_table"]
    if not proxy_path.exists():
        print(f"Proxy table not found at {proxy_path}, skipping")
        return

    df = read_table(proxy_path)
    results = {}

    for variant in ABLATION_VARIANTS:
        df[f"proxy_{variant}"] = compute_proxy_variant(df, variant)
        score_col = f"proxy_{variant}"
        valid = df[[score_col, "btfr_abs_residual"]].dropna()
        qs = q4_q1_ratio(valid, score_col=score_col, residual_col="btfr_abs_residual")
        sr = spearman_proxy_abs_residual(valid, score_col=score_col, residual_col="btfr_abs_residual")
        bs = bootstrap_q4_q1(valid, score_col=score_col, residual_col="btfr_abs_residual")
        results[variant] = {**qs, **sr, **bs}

    rows = []
    for variant, res in results.items():
        row = {"variant": variant}
        row.update(res)
        rows.append(row)

    result_df = pd.DataFrame(rows)
    out = ROOT / "data/derived" / "proxy_ablation_results.csv"
    write_table(result_df, out)
    print(f"Ablation results: {len(rows)} variants -> {out}")

    table_path = OUTPUT_TABLES / "table2_xgass_proxy_ablation.csv"
    write_table(result_df, table_path)
    print(f"Paper table: -> {table_path}")


if __name__ == "__main__":
    main()
