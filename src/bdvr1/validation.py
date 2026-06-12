"""Cross-validation routines and reproducibility validation."""

from __future__ import annotations

from typing import Iterable

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from bdvr1.config import N_FOLDS, RANDOM_SEED


def check_no_missing_required_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> list[str]:
    missing = [col for col in required_columns if col not in df.columns]
    return missing


def manual_kfold(n: int, n_splits: int = N_FOLDS, shuffle: bool = True, seed: int = RANDOM_SEED) -> list[tuple[np.ndarray, np.ndarray]]:
    rng = np.random.default_rng(seed)
    indices = np.arange(n)
    if shuffle:
        rng.shuffle(indices)
    folds = []
    fold_size = n // n_splits
    for i in range(n_splits):
        test_start = i * fold_size
        test_end = test_start + fold_size if i < n_splits - 1 else n
        test_idx = indices[test_start:test_end]
        train_idx = np.concatenate([indices[:test_start], indices[test_end:]])
        folds.append((train_idx, test_idx))
    return folds


def cross_validated_btfr_residuals(
    df: pd.DataFrame,
    score_col: str = "proxy",
    mass_col: str = "logMbar",
    vel_col: str = "logVflat",
    n_folds: int = N_FOLDS,
) -> dict:
    from bdvr1.btfr import fit_btfr_ols, predict_velocity

    valid = df[[mass_col, vel_col, score_col]].dropna()
    lg_m = valid[mass_col].to_numpy(dtype=float)
    lv = valid[vel_col].to_numpy(dtype=float)
    Cv = valid[score_col].to_numpy(dtype=float)
    n = len(lg_m)
    if n < n_folds * 2:
        return {"error": f"insufficient data for {n_folds}-fold CV: n={n}"}

    folds = manual_kfold(n, n_splits=n_folds, shuffle=True, seed=RANDOM_SEED)
    held_out_abs_residuals = np.full(n, np.nan)

    for train_idx, test_idx in folds:
        intercept, slope = fit_btfr_ols(lg_m[train_idx], lv[train_idx])
        pred = predict_velocity(lg_m[test_idx], intercept, slope)
        held_out_abs_residuals[test_idx] = np.abs(lv[test_idx] - pred)

    valid_ho = ~np.isnan(held_out_abs_residuals)
    if np.sum(valid_ho) < 4:
        return {"error": "too few held-out predictions"}

    Ch = Cv[valid_ho]
    Rh = held_out_abs_residuals[valid_ho]
    order = np.argsort(Ch)
    qsize = len(order) // 4
    q4_scatter = float(np.nanstd(Rh[order[-qsize:]]))
    q1_scatter = float(np.nanstd(Rh[order[:qsize]]))
    ratio = q4_scatter / q1_scatter if q1_scatter > 0 else np.nan
    rho, p = spearmanr(Ch, Rh)

    # Full-sample BTFR
    intercept_all, slope_all = fit_btfr_ols(lg_m, lv)

    return {
        "cv_btfr_slope": float(slope_all),
        "cv_btfr_intercept": float(intercept_all),
        "cv_held_out_Q4_Q1_ratio": float(ratio),
        "cv_held_out_spearman_rho": float(rho),
        "cv_held_out_spearman_p": float(p),
        "cv_held_out_N": int(np.sum(valid_ho)),
        "cv_folds": n_folds,
    }
