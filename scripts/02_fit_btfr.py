#!/usr/bin/env python3
"""Fit BTFR and compute residuals for SPARC and xGASS."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bdvr1.config import SPARC_PATHS, XGASS_PATHS
from bdvr1.io import read_table, write_table
from bdvr1.btfr import fit_and_residualize


def main():
    for name, paths in [("SPARC", SPARC_PATHS), ("xGASS", XGASS_PATHS)]:
        clean_path = paths["processed"]
        out_path = paths["btfr_residuals"]
        if not clean_path.exists():
            print(f"{name}: no clean table at {clean_path}, skipping")
            continue
        print(f"Processing BTFR for {name}...")
        df = read_table(clean_path)
        df = fit_and_residualize(df)
        write_table(df, out_path)
        if "btfr_slope" in df.columns and df["btfr_slope"].notna().any():
            slope = df["btfr_slope"].iloc[0]
            intercept = df["btfr_intercept"].iloc[0]
            print(f"  BTFR fitted: logV = {intercept:.3f} + {slope:.3f} * logMbar")
        else:
            print(f"  BTFR residuals: using pre-computed values")
        print(f"  N={len(df)}, written to {out_path}")


if __name__ == "__main__":
    main()
