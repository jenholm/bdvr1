"""Organization proxy computation for SPARC and xGASS."""

from __future__ import annotations

import numpy as np
import pandas as pd

from bdvr1.io import require_columns


def _minmax(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    xmin, xmax = np.nanmin(x), np.nanmax(x)
    if xmax == xmin:
        return np.zeros_like(x)
    return (x - xmin) / (xmax - xmin)


def _rank01(series: pd.Series, ascending: bool = True) -> pd.Series:
    return series.rank(pct=True, ascending=ascending).clip(0.0, 1.0)


def compute_xgass_coherence_proxy(df: pd.DataFrame) -> pd.Series:
    require_columns(df, ["INCL", "W50cor", "f_atm"], "xGASS proxy input")
    incl = pd.to_numeric(df["INCL"], errors="coerce").to_numpy()
    w50 = pd.to_numeric(df["W50cor"], errors="coerce").to_numpy()
    fatm = pd.to_numeric(df["f_atm"], errors="coerce").to_numpy()
    C = (0.35 * incl / 90.0 + 0.35 * _minmax(w50) + 0.30 * (1 - fatm))
    return pd.Series(C, index=df.index, name="xgass_coherence_proxy")


def compute_sparc_demographic_proxy(df: pd.DataFrame) -> pd.Series:
    require_columns(df, ["RHI", "Rdisk", "SBdisk"], "SPARC proxy input")
    rhi = pd.to_numeric(df["RHI"], errors="coerce")
    rdisk = pd.to_numeric(df["Rdisk"], errors="coerce")
    sbdisk = pd.to_numeric(df["SBdisk"], errors="coerce")
    rhi_norm = (rhi / rdisk.replace(0, np.nan)).clip(0, 20)
    rhi_score = (1 - _rank01(rhi_norm, ascending=True)).to_numpy()
    sb_score = _rank01(sbdisk, ascending=True).to_numpy()
    C = 0.50 * rhi_score + 0.50 * sb_score
    return pd.Series(C, index=df.index, name="sparc_demographic_proxy")


def compute_proxy_variant(df: pd.DataFrame, variant: str, base_proxy_col: str = "proxy") -> pd.Series:
    require_columns(df, ["INCL", "W50cor", "f_atm"], f"proxy variant {variant}")
    incl = pd.to_numeric(df["INCL"], errors="coerce").to_numpy()
    w50 = pd.to_numeric(df["W50cor"], errors="coerce").to_numpy()
    fatm = pd.to_numeric(df["f_atm"], errors="coerce").to_numpy()

    variants = {
        "full": 0.35 * incl / 90.0 + 0.35 * _minmax(w50) + 0.30 * (1 - fatm),
        "incl_fatm_no_w50": 0.5 * incl / 90.0 + 0.5 * (1 - fatm),
        "w50_fatm_no_incl": 0.5 * _minmax(w50) + 0.5 * (1 - fatm),
        "incl_only": incl / 90.0,
        "w50_only": _minmax(w50),
        "gas_only": 1 - fatm,
        "no_raw_w50": 0.5 * incl / 90.0 + 0.5 * (1 - fatm),
        "no_incl": 0.5 * _minmax(w50) + 0.5 * (1 - fatm),
        "no_gas": 0.5 * incl / 90.0 + 0.5 * _minmax(w50),
    }
    C = variants.get(variant)
    if C is None:
        raise ValueError(f"Unknown variant '{variant}'. Options: {list(variants.keys())}")
    return pd.Series(C, index=df.index, name=f"proxy_variant_{variant}")


def assign_quartiles(score: pd.Series) -> pd.Series:
    labels = ["Q1", "Q2", "Q3", "Q4"]
    return pd.qcut(score.rank(method="first"), q=4, labels=labels)
