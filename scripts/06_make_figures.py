#!/usr/bin/env python3
"""Reproduce all paper figures."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bdvr1.config import SPARC_PATHS, XGASS_PATHS
from bdvr1.io import read_table
from bdvr1.plotting import (
    plot_cross_survey_quartiles,
    plot_xgass_velocity_variants,
    plot_proxy_variant_comparison,
    plot_mass_bin_quartiles,
    plot_q4_q1_summary,
)


def main():
    # Load data
    sparc_df = None
    xgass_df = None

    sparc_proxy_path = SPARC_PATHS["proxy_table"]
    if sparc_proxy_path.exists():
        sparc_df = read_table(sparc_proxy_path)
        print(f"Loaded SPARC: {len(sparc_df)} galaxies")
    else:
        print("SPARC proxy table not found")

    xgass_proxy_path = XGASS_PATHS["proxy_table"]
    if xgass_proxy_path.exists():
        xgass_df = read_table(xgass_proxy_path)
        print(f"Loaded xGASS: {len(xgass_df)} galaxies")
    else:
        print("xGASS proxy table not found")

    # Figure 1: Cross-survey quartiles
    if sparc_df is not None and xgass_df is not None:
        plot_cross_survey_quartiles(sparc_df, xgass_df)
        print("Figure 1: cross-survey quartiles")

    # Figure 2: xGASS velocity variants
    if xgass_df is not None:
        plot_xgass_velocity_variants(xgass_df)
        print("Figure 2: xGASS velocity variants")

    # Figure 3: Proxy variant comparison
    ablation_path = Path("data/derived/proxy_ablation_results.csv")
    if ablation_path.exists():
        ablation_df = read_table(ablation_path)
        ablation_dict = ablation_df.set_index("variant").to_dict(orient="index")
        plot_proxy_variant_comparison(ablation_dict)
        print("Figure 3: proxy variant comparison")

    # Figure 4: Mass-bin quartiles
    if xgass_df is not None:
        plot_mass_bin_quartiles(xgass_df)
        print("Figure 4: mass-bin quartiles")

    # Figure 5: Q4/Q1 ratio summary
    if xgass_df is not None:
        summary_data = {"xGASS full": q4_q1_with_ci(xgass_df)}
        if sparc_df is not None:
            summary_data["SPARC"] = q4_q1_with_ci(sparc_df)
        plot_q4_q1_summary(summary_data)
        print("Figure 5: Q4/Q1 ratio summary")

    print("All figures generated in outputs/figures/")


def q4_q1_with_ci(df):
    from bdvr1.statistics import q4_q1_ratio, bootstrap_q4_q1
    qs = q4_q1_ratio(df)
    bs = bootstrap_q4_q1(df)
    qs["ratio_ci_95"] = [bs["bootstrap_Q4_Q1_ci_95_low"], bs["bootstrap_Q4_Q1_ci_95_high"]]
    return qs


if __name__ == "__main__":
    main()
