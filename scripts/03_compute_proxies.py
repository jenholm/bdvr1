#!/usr/bin/env python3
"""Compute organization proxies for SPARC and xGASS."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd

from bdvr1.config import (
    SPARC_PATHS, XGASS_PATHS,
    XGASS_SCORE_COL, XGASS_QUARTILE_COL,
    SPARC_CURRENT_SCORE_COL, SPARC_CURRENT_QUARTILE_COL,
)
from bdvr1.io import read_table, write_table
from bdvr1.proxies import (
    compute_xgass_coherence_proxy,
    compute_sparc_demographic_proxy,
    assign_quartiles,
)


def main():
    # SPARC demographic proxy (diagnostic, not the paper-facing M74 table)
    sparc_path = SPARC_PATHS["btfr_residuals"]
    if sparc_path.exists():
        df = read_table(sparc_path)
        df[SPARC_CURRENT_SCORE_COL] = compute_sparc_demographic_proxy(df)
        df[SPARC_CURRENT_QUARTILE_COL] = assign_quartiles(df[SPARC_CURRENT_SCORE_COL])
        write_table(df, SPARC_PATHS["proxy_table"])
        print(f"SPARC demographic proxy table: {len(df)} galaxies -> {SPARC_PATHS['proxy_table']}")
    else:
        print(f"SPARC residuals not found at {sparc_path}, skipping")

    # xGASS
    xgass_path = XGASS_PATHS["btfr_residuals"]
    if xgass_path.exists():
        df = read_table(xgass_path)
        df[XGASS_SCORE_COL] = compute_xgass_coherence_proxy(df)
        df[XGASS_QUARTILE_COL] = assign_quartiles(df[XGASS_SCORE_COL])
        write_table(df, XGASS_PATHS["proxy_table"])
        print(f"xGASS proxy table: {len(df)} galaxies -> {XGASS_PATHS['proxy_table']}")
    else:
        print(f"xGASS residuals not found at {xgass_path}, skipping")


if __name__ == "__main__":
    main()
