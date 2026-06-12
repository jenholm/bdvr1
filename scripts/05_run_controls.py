#!/usr/bin/env python3
"""Run inclination, mass, and measurement-quality controls."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np
from scipy.stats import spearmanr

from bdvr1.config import OUTPUT_TABLES, XGASS_PATHS, XGASS_SCORE_COL
from bdvr1.io import read_table, write_table
from bdvr1.proxies import compute_xgass_coherence_proxy, compute_proxy_variant
from bdvr1.statistics import (
    q4_q1_ratio,
    spearman_proxy_abs_residual,
    mass_residualized_correlation,
    mass_matched_quartile_scatter,
    measurement_quality_regression,
)


def main():
    proxy_path = XGASS_PATHS["proxy_table"]
    if not proxy_path.exists():
        print(f"Proxy table not found at {proxy_path}, skipping")
        return

    df = read_table(proxy_path)
    score_col = XGASS_SCORE_COL
    if score_col not in df.columns:
        df[score_col] = compute_xgass_coherence_proxy(df)

    # 1. Inclination-restricted analysis
    incl_restricted_rows = []
    for label, lo, hi in [("all", 0, 90), ("mid_45_75", 45, 75), ("mid_50_80", 50, 80)]:
        subset = df[(df["INCL"] >= lo) & (df["INCL"] <= hi)].copy()
        row = {"label": label}
        if len(subset) < 10:
            row.update({"N": len(subset), "error": "insufficient data"})
        else:
            qs = q4_q1_ratio(subset, score_col=score_col)
            sr = spearman_proxy_abs_residual(subset, score_col=score_col)
            rho_incl, p_incl = spearmanr(subset["INCL"], subset["btfr_abs_residual"])
            row.update({**qs, **sr, "spearman_incl_vs_abs": float(rho_incl), "spearman_incl_p": float(p_incl)})
        incl_restricted_rows.append(row)
    write_table(pd.DataFrame(incl_restricted_rows), OUTPUT_TABLES / "inclination_restricted_summary.csv")

    # 2. Mass controls
    mass_rows = []
    mr = mass_residualized_correlation(df, score_col=score_col)
    mm = mass_matched_quartile_scatter(df, score_col=score_col)
    sr = spearman_proxy_abs_residual(df, score_col=score_col)
    mass_rows.append({"test": "mass_residualized", **mr})
    mass_rows.append({"test": "mass_matched", **mm})
    mass_rows.append({"test": "raw_spearman", **sr})
    write_table(pd.DataFrame(mass_rows), OUTPUT_TABLES / "mass_controls_summary.csv")

    # 3. xGASS controls summary
    xgass_ctrl_rows = []
    for variant in ["full", "incl_only", "w50_only", "gas_only"]:
        score_col = f"proxy_{variant}"
        if score_col not in df.columns:
            df[score_col] = compute_proxy_variant(df, variant)
        subset = df[[score_col, "btfr_abs_residual"]].dropna()
        qs = q4_q1_ratio(subset, score_col=score_col, residual_col="btfr_abs_residual")
        sr = spearman_proxy_abs_residual(subset, score_col=score_col, residual_col="btfr_abs_residual")
        xgass_ctrl_rows.append({"variant": variant, **qs, **sr})
    write_table(pd.DataFrame(xgass_ctrl_rows), OUTPUT_TABLES / "xgass_controls_summary.csv")

    # 4. Measurement quality controls
    qual = measurement_quality_regression(df, score_col=score_col)
    write_table(pd.DataFrame([qual]), OUTPUT_TABLES / "measurement_quality_controls.csv")


if __name__ == "__main__":
    main()
