#!/usr/bin/env python3
"""Run inclination, mass, and measurement-quality controls."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np
from scipy.stats import spearmanr

from bdvr1.config import XGASS_PATHS
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
    if "proxy" not in df.columns:
        df["proxy"] = compute_xgass_coherence_proxy(df)

    # 1. Inclination-restricted analysis
    incl_restricted = {}
    for label, lo, hi in [("all", 0, 90), ("mid_45_75", 45, 75), ("mid_50_80", 50, 80)]:
        subset = df[(df["INCL"] >= lo) & (df["INCL"] <= hi)].copy()
        if len(subset) < 10:
            incl_restricted[label] = {"N": len(subset), "error": "insufficient data"}
            continue
        qs = q4_q1_ratio(subset)
        sr = spearman_proxy_abs_residual(subset)
        rho_incl, p_incl = spearmanr(subset["INCL"], subset["btfr_abs_residual"])
        incl_restricted[label] = {
            **qs,
            **sr,
            "spearman_incl_vs_abs": float(rho_incl),
            "spearman_incl_p": float(p_incl),
        }
    write_table(incl_restricted, Path("outputs/tables/inclination_restricted_summary.csv"))

    # 2. Mass controls
    mass_ctrl = {}
    mr = mass_residualized_correlation(df)
    mm = mass_matched_quartile_scatter(df)
    sr = spearman_proxy_abs_residual(df)
    mass_ctrl["mass_residualized"] = mr
    mass_ctrl["mass_matched"] = mm
    mass_ctrl["raw_spearman"] = sr
    write_table(mass_ctrl, Path("outputs/tables/mass_controls_summary.csv"))

    # 3. xGASS controls summary
    xgass_ctrl = {}
    for variant in ["full", "incl_only", "w50_only", "gas_only"]:
        score_col = f"proxy_{variant}"
        if score_col not in df.columns:
            df[score_col] = compute_proxy_variant(df, variant)
        subset = df[[score_col, "btfr_abs_residual"]].dropna()
        qs = q4_q1_ratio(subset, score_col=score_col, residual_col="btfr_abs_residual")
        sr = spearman_proxy_abs_residual(subset, score_col=score_col, residual_col="btfr_abs_residual")
        xgass_ctrl[variant] = {**qs, **sr}
    write_table(xgass_ctrl, Path("outputs/tables/xgass_controls_summary.csv"))

    # 4. Measurement quality controls
    qual = measurement_quality_regression(df)
    write_table(qual, Path("outputs/tables/measurement_quality_controls.csv"))


if __name__ == "__main__":
    main()
