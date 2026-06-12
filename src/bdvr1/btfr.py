"""Baryonic Tully-Fisher Relation fitting and residuals."""

from __future__ import annotations

import numpy as np
import pandas as pd

from bdvr1.config import HELIUM_FACTOR, WTURB_KMS


def compute_mbar(mstar_msun: float, mhi_msun: float, helium_factor: float = HELIUM_FACTOR) -> float:
    return mstar_msun + helium_factor * mhi_msun


def correct_w50(w50: float | np.ndarray, wturb: float = WTURB_KMS) -> float:
    return np.sqrt(np.maximum(w50**2 - wturb**2, 0.0))


def compute_vrot(w50_corr: float | np.ndarray, inclination_deg: float | np.ndarray) -> float:
    incl_rad = np.radians(np.asarray(inclination_deg, dtype=float))
    return np.asarray(w50_corr, dtype=float) / (2.0 * np.sin(np.maximum(incl_rad, 0.1)))


def fit_btfr_ols(log_mbar: np.ndarray, log_v: np.ndarray) -> tuple[float, float]:
    A = np.vstack([np.ones_like(log_mbar), log_mbar]).T
    coeffs, _, _, _ = np.linalg.lstsq(A, log_v, rcond=None)
    return float(coeffs[0]), float(coeffs[1])


def predict_velocity(log_mbar: np.ndarray, intercept: float, slope: float) -> np.ndarray:
    return intercept + slope * log_mbar


def compute_btfr_residuals(
    log_v_obs: np.ndarray,
    log_v_pred: np.ndarray,
) -> np.ndarray:
    return log_v_obs - log_v_pred


def mcGaugh2012_btfr_residual(mbar_msun: np.ndarray, vflat_kms: np.ndarray) -> np.ndarray:
    """McGaugh 2012 BTFR: Mbar = 50 * Vflat^4 (Mbar in Msun, Vflat in km/s)."""
    log_v_pred = 0.25 * (np.log10(np.maximum(mbar_msun, 1.0)) - np.log10(50.0))
    residual = np.log10(np.maximum(vflat_kms, 1.0)) - log_v_pred
    return residual


def fit_and_residualize(
    df: pd.DataFrame,
    mass_col: str = "logMbar",
    vel_col: str = "logVflat",
    mbar_msun_col: str | None = None,
    vflat_kms_col: str | None = None,
) -> pd.DataFrame:
    out = df.copy()
    if "btfr_residual_dex" in out.columns and out["btfr_residual_dex"].notna().any():
        return out
    valid = df[mass_col].notna() & df[vel_col].notna()
    log_m = df.loc[valid, mass_col].to_numpy(dtype=float)
    log_v = df.loc[valid, vel_col].to_numpy(dtype=float)
    intercept, slope = fit_btfr_ols(log_m, log_v)
    out["btfr_intercept"] = intercept
    out["btfr_slope"] = slope
    out["btfr_pred_logV"] = np.nan
    out["btfr_residual_dex"] = np.nan
    out["btfr_abs_residual"] = np.nan
    out.loc[valid, "btfr_pred_logV"] = predict_velocity(log_m, intercept, slope)
    res = compute_btfr_residuals(log_v, out.loc[valid, "btfr_pred_logV"].to_numpy())
    out.loc[valid, "btfr_residual_dex"] = res
    out.loc[valid, "btfr_abs_residual"] = np.abs(res)

    # Add McGaugh 2012 residual for SPARC if columns available
    if mbar_msun_col is not None and vflat_kms_col is not None:
        mcg = mcGaugh2012_btfr_residual(
            df[mbar_msun_col].to_numpy(dtype=float),
            df[vflat_kms_col].to_numpy(dtype=float),
        )
        out["btfr_mcgaugh2012_residual_dex"] = mcg
        out["btfr_mcgaugh2012_abs_residual"] = np.abs(mcg)
    return out
