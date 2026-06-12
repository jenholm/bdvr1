"""Read SPARC/xGASS tables and write outputs."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd


def require_columns(df: pd.DataFrame, required: Iterable[str], dataset_name: str = "data") -> None:
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"{dataset_name} missing required columns: {', '.join(missing)}")


def read_sparc_raw(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, comment="#")
    df.columns = df.columns.str.strip()
    return df


def read_xgass_raw(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, comment="#")
    df.columns = df.columns.str.strip()
    return df


def write_table(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def read_table(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_sparc(df: pd.DataFrame) -> pd.DataFrame:
    require_columns(
        df,
        ["galaxy_name", "Q", "Vflat", "L36", "MHI", "Rdisk", "RHI", "SBdisk", "Inc", "T"],
        "SPARC input",
    )
    out = df.copy()
    for col in ["Vflat", "L36", "MHI", "Rdisk", "RHI", "Inc"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out[out["Q"] == 1].copy()
    out = out.dropna(subset=["Vflat", "L36", "Inc"])
    out["Mbar_msun"] = 0.5 * out["L36"] * 1e9 + 1.33 * out["MHI"] * 1e9
    out["logMbar"] = np.log10(out["Mbar_msun"])
    out["logVflat"] = np.log10(out["Vflat"])
    return out.reset_index(drop=True)


def clean_xgass(df: pd.DataFrame) -> pd.DataFrame:
    require_columns(
        df,
        ["GASS", "INCL", "W50cor", "lgMstar", "lgMHI", "HI_FLAG", "HIconf_flag", "lgSFR_tot_median"],
        "xGASS input",
    )
    out = df.copy()
    for col in ["INCL", "W50cor", "lgMstar", "lgMHI"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out[out["HI_FLAG"].isin([1, 3, 5])].copy()
    out = out.dropna(subset=["INCL", "W50cor", "lgMstar"])
    out["Mbar_msun"] = 10 ** out["lgMstar"] + 1.33 * 10 ** out["lgMHI"].fillna(0)
    out["logMbar"] = np.log10(out["Mbar_msun"])
    out["f_atm"] = (1.33 * 10 ** out["lgMHI"].fillna(0)) / out["Mbar_msun"]
    out["Vflat"] = out["W50cor"] / 2.0
    out["logVflat"] = np.log10(out["Vflat"].clip(lower=1.0))
    out["logVw50"] = np.log10(out["W50cor"].clip(lower=1.0))
    return out.reset_index(drop=True)
