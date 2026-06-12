#!/usr/bin/env python3
"""Validate derived tables reproduce the paper's key numerical results."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bdvr1.config import (
    DERIVED_DIR, XGASS_SCORE_COL, XGASS_QUARTILE_COL,
    SPARC_CURRENT_SCORE_COL, SPARC_CURRENT_QUARTILE_COL, SPARC_M74_SCORE_COL,
    SPARC_PATHS,
)
from bdvr1.io import read_table, read_json, write_table
from bdvr1.statistics import q4_q1_ratio, spearman_proxy_abs_residual, bootstrap_q4_q1

RTOL = 1e-5


def check(condition: bool, msg: str) -> None:
    if not condition:
        print(f"  FAIL: {msg}")
        raise AssertionError(msg)
    print(f"  OK: {msg}")


def test_xgass_proxy_table():
    path = DERIVED_DIR / "xgass_proxy_table.csv"
    assert path.exists(), f"Missing {path}"
    df = read_table(path)
    check(len(df) == 363, f"xGASS proxy table has {len(df)} rows (expect 363)")

    non_missing = df[XGASS_SCORE_COL].notna().sum()
    check(non_missing == 320, f"xGASS non-missing proxy: {non_missing} (expect 320)")

    missing = df[XGASS_SCORE_COL].isna().sum()
    check(missing == 43, f"xGASS missing proxy: {missing} (expect 43)")

    quartile_counts = df[XGASS_QUARTILE_COL].value_counts()
    for q in ["Q1", "Q2", "Q3", "Q4"]:
        cnt = quartile_counts.get(q, 0)
        check(cnt == 80, f"xGASS {q}: {cnt} galaxies (expect 80)")


def test_xgass_ablation():
    path = DERIVED_DIR / "proxy_ablation_results.csv"
    assert path.exists(), f"Missing {path}"
    df = read_table(path)
    check(len(df) == 7, f"Ablation has {len(df)} variants (expect 7)")

    ref_path = DERIVED_DIR / "arxiv_revised_analysis.json"
    ref = read_json(ref_path)
    full_ref = ref["ablation"]["full"]

    full_row = df[df["variant"] == "full"].iloc[0]
    check(
        abs(full_row["Q4_Q1_ratio"] - full_ref["ratio"]) < RTOL,
        f"full Q4/Q1 ratio: CSV={full_row['Q4_Q1_ratio']:.10f}, JSON={full_ref['ratio']:.10f}",
    )

    for variant in ["incl_fatm_no_w50", "w50_fatm_no_incl", "incl_only", "w50_only", "gas_only", "no_gas"]:
        if variant in ref["ablation"]:
            row = df[df["variant"] == variant].iloc[0]
            ref_v = ref["ablation"][variant]
            check(
                abs(row["Q4_Q1_ratio"] - ref_v["ratio"]) < RTOL,
                f"{variant} Q4/Q1 ratio: CSV={row['Q4_Q1_ratio']:.10f}, JSON={ref_v['ratio']:.10f}",
            )


def test_sparc_m74_table():
    path = SPARC_PATHS["m74_proxy_table"]
    assert path.exists(), f"Missing {path}"
    df = read_table(path)
    check(len(df) == 87, f"M74 SPARC table: {len(df)} galaxies (expect 87)")

    # Reproduce the paper Q4/Q1 scatter ratio from the M74 table
    valid = df.dropna(subset=["coherence_quartile", "btfr_offset_dex"])
    quartiles = valid.groupby("coherence_quartile", observed=True)["btfr_offset_dex"]
    stds = quartiles.std()
    q1_std = stds.get("Q1_low", np.nan)
    q4_std = stds.get("Q4_high", np.nan)
    ratio = q4_std / q1_std if q1_std > 0 else np.nan

    paper_ratio = 0.6506373440385053
    check(
        abs(ratio - paper_ratio) < RTOL,
        f"M74 Q4/Q1 ratio: computed={ratio:.10f}, paper={paper_ratio:.10f}",
    )
    check(
        abs(q1_std - 0.0752713364616819) < RTOL,
        f"M74 Q1 scatter: computed={q1_std:.10f}, paper=0.0752713365",
    )
    check(
        abs(q4_std - 0.04897434243765741) < RTOL,
        f"M74 Q4 scatter: computed={q4_std:.10f}, paper=0.0489743424",
    )

    # Verify quartile sizes
    qcounts = valid["coherence_quartile"].value_counts()
    check(qcounts.get("Q1_low", 0) == 22, "M74 Q1_low: 22 galaxies")
    check(qcounts.get("Q2", 0) == 22, "M74 Q2: 22 galaxies")
    check(qcounts.get("Q3", 0) == 21, "M74 Q3: 21 galaxies")
    check(qcounts.get("Q4_high", 0) == 22, "M74 Q4_high: 22 galaxies")


def test_xgass_residuals_no_legacy_cols():
    path = DERIVED_DIR / "btfr_residuals_xgass.csv"
    assert path.exists(), f"Missing {path}"
    df = read_table(path)
    check("coherence_score" not in df.columns, "btfr_residuals_xgass: no coherence_score")
    check("coherence_quartile" not in df.columns, "btfr_residuals_xgass: no coherence_quartile")


def test_paper_values_in_json():
    path = DERIVED_DIR / "arxiv_revised_analysis.json"
    ref = read_json(path)
    check("paper_values" in ref, "arxiv_revised_analysis.json has paper_values")
    pv = ref["paper_values"]
    check("delta_r2" in pv, "paper_values.delta_r2 present")
    check(
        abs(pv["delta_r2"] - 0.0034819227679210307) < RTOL,
        f"paper delta_r2 = {pv['delta_r2']:.10f}",
    )
    check(
        abs(pv["sparc"]["scatter_ratio_Q4_Q1"] - 0.6506373440385053) < RTOL,
        f"paper SPARC ratio = {pv['sparc']['scatter_ratio_Q4_Q1']:.10f}",
    )


def main():
    print("=" * 60)
    print("Paper number validation")
    print("=" * 60)

    tests = [
        ("xGASS proxy table", test_xgass_proxy_table),
        ("xGASS ablation matches JSON", test_xgass_ablation),
        ("SPARC M74 table reproduces paper Q4/Q1", test_sparc_m74_table),
        ("xGASS residuals no legacy columns", test_xgass_residuals_no_legacy_cols),
        ("paper_values in arxiv_revised_analysis.json", test_paper_values_in_json),
    ]

    n_pass = 0
    for name, func in tests:
        print(f"\n--- {name} ---")
        try:
            func()
            n_pass += 1
        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\n{'=' * 60}")
    print(f"Result: {n_pass}/{len(tests)} passed")
    if n_pass < len(tests):
        sys.exit(1)
    print("All paper numbers validated.")


if __name__ == "__main__":
    main()
