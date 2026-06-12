"""Statistical utilities: scatter ratios, Spearman rho, bootstrap, controls."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from bdvr1.config import N_BOOTSTRAP, RANDOM_SEED


def scatter_by_quartile(df: pd.DataFrame, score_col: str = "proxy", residual_col: str = "btfr_abs_residual") -> dict:
    valid = df[[score_col, residual_col]].dropna()
    C = valid[score_col].to_numpy()
    abs_res = valid[residual_col].to_numpy()
    order = np.argsort(C)
    n = len(order)
    qsize = n // 4
    q_labels = {}
    for i, label in enumerate(["Q1", "Q2", "Q3", "Q4"]):
        lo = i * qsize
        hi = (i + 1) * qsize if i < 3 else n
        idx = order[lo:hi]
        q_labels[label] = {
            "N": int(len(idx)),
            "scatter_std": float(np.nanstd(abs_res[idx])),
            "mean_proxy": float(np.nanmean(C[idx])),
        }
    return q_labels


def q4_q1_ratio(df: pd.DataFrame, score_col: str = "proxy", residual_col: str = "btfr_abs_residual") -> dict:
    valid = df[[score_col, residual_col]].dropna()
    C = valid[score_col].to_numpy()
    abs_res = valid[residual_col].to_numpy()
    order = np.argsort(C)
    n = len(order)
    qsize = n // 4
    q4_idx = order[-qsize:]
    q1_idx = order[:qsize]
    q4_scatter = float(np.nanstd(abs_res[q4_idx]))
    q1_scatter = float(np.nanstd(abs_res[q1_idx]))
    ratio = q4_scatter / q1_scatter if q1_scatter > 0 else np.nan
    return {
        "Q4_scatter": q4_scatter,
        "Q1_scatter": q1_scatter,
        "Q4_Q1_ratio": ratio,
        "N_Q4": int(qsize),
        "N_Q1": int(qsize),
    }


def bootstrap_q4_q1(
    df: pd.DataFrame,
    score_col: str = "proxy",
    residual_col: str = "btfr_abs_residual",
    n_boot: int = N_BOOTSTRAP,
) -> dict:
    valid = df[[score_col, residual_col]].dropna()
    C = valid[score_col].to_numpy()
    abs_res = valid[residual_col].to_numpy()
    n = len(C)
    rng = np.random.default_rng(RANDOM_SEED)
    boot_ratios = []
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        C_boot = C[idx]
        ar_boot = abs_res[idx]
        order = np.argsort(C_boot)
        qsize = n // 4
        q1 = np.nanstd(ar_boot[order[:qsize]])
        q4 = np.nanstd(ar_boot[order[-qsize:]])
        boot_ratios.append(q4 / q1 if q1 > 0 else np.nan)
    boot_ratios = np.array(boot_ratios)
    boot_ratios = boot_ratios[~np.isnan(boot_ratios)]
    ci_low, ci_high = np.percentile(boot_ratios, [2.5, 97.5])
    return {
        "bootstrap_Q4_Q1_ratio": float(np.nanmean(boot_ratios)),
        "bootstrap_Q4_Q1_ci_95_low": float(ci_low),
        "bootstrap_Q4_Q1_ci_95_high": float(ci_high),
        "n_bootstrap": n_boot,
    }


def spearman_proxy_abs_residual(df: pd.DataFrame, score_col: str = "proxy", residual_col: str = "btfr_abs_residual") -> dict:
    valid = df[[score_col, residual_col]].dropna()
    rho, p = spearmanr(valid[score_col], valid[residual_col])
    return {
        "spearman_rho": float(rho),
        "spearman_p": float(p),
        "N": int(len(valid)),
    }


def mass_residualized_correlation(df: pd.DataFrame, score_col: str = "proxy", mass_col: str = "logMbar", residual_col: str = "btfr_abs_residual") -> dict:
    valid = df[[score_col, mass_col, residual_col]].dropna()
    C = valid[score_col].to_numpy()
    M = valid[mass_col].to_numpy()
    R = valid[residual_col].to_numpy()
    A = np.vstack([np.ones_like(M), M]).T
    coeffs, _, _, _ = np.linalg.lstsq(A, C, rcond=None)
    C_resid = C - A @ coeffs
    rho, p = spearmanr(C_resid, R)
    return {
        "spearman_mass_residualized_C_vs_abs": float(rho),
        "spearman_mass_residualized_p": float(p),
        "N": int(len(C)),
    }


def multi_linear_regression(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float, np.ndarray]:
    Xd = np.column_stack([np.ones(X.shape[0]), X])
    coeffs, residuals, _, _ = np.linalg.lstsq(Xd, y, rcond=None)
    pred = Xd @ coeffs
    rss = np.sum((y - pred) ** 2)
    tss = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - rss / tss if tss > 0 else 0.0
    return coeffs, float(r2), pred


def mass_matched_quartile_scatter(df: pd.DataFrame, score_col: str = "proxy", mass_col: str = "logMbar", residual_col: str = "btfr_abs_residual") -> dict:
    valid = df[[score_col, mass_col, residual_col]].dropna()
    C = valid[score_col].to_numpy()
    M = valid[mass_col].to_numpy()
    R = valid[residual_col].to_numpy()
    mass_bins = np.linspace(np.nanpercentile(M, 5), np.nanpercentile(M, 95), 6)
    matched_low, matched_high = [], []
    for i in range(len(mass_bins) - 1):
        lo, hi = mass_bins[i], mass_bins[i + 1]
        mask = (M >= lo) & (M < hi)
        if np.sum(mask) < 4:
            continue
        C_bin = C[mask]
        R_bin = R[mask]
        thresh = np.nanmedian(C_bin)
        low_idx = C_bin < thresh
        high_idx = C_bin >= thresh
        if np.sum(low_idx) > 0 and np.sum(high_idx) > 0:
            matched_low.extend(R_bin[low_idx])
            matched_high.extend(R_bin[high_idx])
    ml = np.array(matched_low)
    mh = np.array(matched_high)
    if len(ml) > 0 and len(mh) > 0:
        ratio = float(np.nanstd(mh) / np.nanstd(ml)) if np.nanstd(ml) > 0 else np.nan
    else:
        ratio = np.nan
    return {
        "mass_matched_low_scatter": float(np.nanstd(ml)) if len(ml) > 0 else np.nan,
        "mass_matched_high_scatter": float(np.nanstd(mh)) if len(mh) > 0 else np.nan,
        "mass_matched_ratio": ratio,
        "N_low": int(len(ml)),
        "N_high": int(len(mh)),
    }


def measurement_quality_regression(df: pd.DataFrame, score_col: str = "proxy", mass_col: str = "logMbar", residual_col: str = "btfr_abs_residual", extra_control_cols: list[str] | None = None) -> dict:
    controls = [mass_col, "INCL"]
    if extra_control_cols:
        controls.extend(extra_control_cols)
    all_cols = [score_col, residual_col] + controls
    valid = df[[c for c in all_cols if c in df.columns]].dropna()
    R = valid[residual_col].to_numpy()
    X_null = valid[[c for c in controls if c in valid.columns]].to_numpy()
    _, r2_null, _ = multi_linear_regression(X_null, R)
    if score_col in valid.columns:
        Cv = valid[score_col].to_numpy()
        X_full = np.column_stack([X_null, Cv])
        _, r2_full, _ = multi_linear_regression(X_full, R)
    else:
        r2_full = r2_null
    return {
        "r2_controls_only": float(r2_null),
        "r2_controls_plus_proxy": float(r2_full),
        "delta_r2": float(r2_full - r2_null),
        "N": int(len(R)),
    }
