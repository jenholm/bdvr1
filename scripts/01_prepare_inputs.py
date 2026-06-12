#!/usr/bin/env python3
"""Prepare cleaned SPARC and xGASS analysis tables."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bdvr1.config import DATA_DIR, SPARC_PATHS, XGASS_PATHS
from bdvr1.io import clean_sparc, clean_xgass, write_table, read_sparc_raw, read_xgass_raw


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    sparc_raw = SPARC_PATHS["raw_quality1"]
    if sparc_raw.exists():
        print(f"Reading SPARC inputs from {sparc_raw}")
        df_sparc = read_sparc_raw(sparc_raw)
        df_sparc_clean = clean_sparc(df_sparc)
        write_table(df_sparc_clean, SPARC_PATHS["processed"])
        print(f"  SPARC clean: {len(df_sparc_clean)} galaxies -> {SPARC_PATHS['processed']}")
    else:
        print(f"SPARC input not found at {sparc_raw}")
        print("  Download SPARC data first (see data/README.md)")
        print("  Creating placeholder processing path...")
        SPARC_PATHS["processed"].parent.mkdir(parents=True, exist_ok=True)

    xgass_raw = XGASS_PATHS["raw_sample"]
    if xgass_raw.exists():
        print(f"Reading xGASS inputs from {xgass_raw}")
        df_xgass = read_xgass_raw(xgass_raw)
        df_xgass_clean = clean_xgass(df_xgass)
        write_table(df_xgass_clean, XGASS_PATHS["processed"])
        print(f"  xGASS clean: {len(df_xgass_clean)} galaxies -> {XGASS_PATHS['processed']}")
    else:
        print(f"xGASS input not found at {xgass_raw}")
        print("  Download xGASS data first (see data/README.md)")
        XGASS_PATHS["processed"].parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
