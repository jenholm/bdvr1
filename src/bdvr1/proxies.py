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
    require_columns(df, ["RHI", "Rdisk", "SBdisk", "L36", "MHI"], "SPARC proxy input")
    rhi = pd.to_numeric(df["RHI"], errors="coerce").to_numpy()
    rdisk = pd.to_numeric(df["Rdisk"], errors="coerce").to_numpy()
    sbdisk = pd.to_numeric(df["SBdisk"], errors="coerce").to_numpy()
    l36 = pd.to_numeric(df["L36"], errors="coerce").to_numpy()
    mhi = pd.to_numeric(df["MHI"], errors="coerce").to_numpy()

    # Stellar surface density: log10 of SBdisk
    log_sigma = np.log10(np.maximum(sbdisk, 1.0))

    # Stellar fraction: M* / Mbar
    mstar = 0.5 * l36 * 1e9
    mbar = mstar + 1.33 * mhi * 1e9
    f_star = mstar / np.maximum(mbar, 1.0)

    # H I-to-optical disk scale-length ratio
    rhi_rd = rhi / np.maximum(rdisk, 0.1)

    # Robust z-score
    def robust_z(x):
        med = np.nanmedian(x)
        mad = np.nanmedian(np.abs(x - med))
        return (x - med) / max(mad, 1e-10)

    z1 = robust_z(log_sigma)
    z2 = robust_z(f_star)
    z3 = robust_z(rhi_rd)

    # D = (1/3)*z_logSigma + (1/3)*z_f* - (1/3)*z_RHI/Rd
    D = (z1 + z2 - z3) / 3.0

    # Minmax normalize to [0, 1]
    dmin, dmax = np.nanmin(D), np.nanmax(D)
    if dmax == dmin:
        C = np.zeros_like(D)
    else:
        C = (D - dmin) / (dmax - dmin)
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
