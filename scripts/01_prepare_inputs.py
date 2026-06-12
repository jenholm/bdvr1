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

    for name, paths, raw_key in [
        ("SPARC", SPARC_PATHS, "raw"),
        ("xGASS", XGASS_PATHS, "raw"),
    ]:
        raw_path = paths[raw_key]
        if raw_path.exists():
            print(f"Reading {name} inputs from {raw_path}")
            if name == "SPARC":
                df = read_sparc_raw(raw_path)
                df_clean = clean_sparc(df)
            else:
                df = read_xgass_raw(raw_path)
                df_clean = clean_xgass(df)
            write_table(df_clean, paths["processed"])
            print(f"  {name} clean: {len(df_clean)} galaxies -> {paths['processed']}")
        else:
            print(f"{name} input not found at {raw_path}")
            print(f"  Data should be placed in data/raw/ (see data/README.md)")
            paths["processed"].parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
