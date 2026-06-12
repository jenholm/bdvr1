"""Tests for BTFR fitting module."""

from __future__ import annotations

import numpy as np
import pandas as pd

from bdvr1.btfr import (
    compute_mbar,
    correct_w50,
    fit_btfr_ols,
    predict_velocity,
    compute_btfr_residuals,
    fit_and_residualize,
)
from bdvr1.config import HELIUM_FACTOR, WTURB_KMS


def test_compute_mbar():
    mbar = compute_mbar(1e10, 1e9)
    expected = 1e10 + HELIUM_FACTOR * 1e9
    assert np.isclose(mbar, expected)


def test_correct_w50():
    w50 = 50.0
    wcorr = correct_w50(w50, wturb=10.0)
    expected = np.sqrt(50**2 - 10**2)
    assert np.isclose(wcorr, expected)


def test_correct_w50_zero_turbulence():
    assert np.isclose(correct_w50(50.0, wturb=0.0), 50.0)


def test_correct_w50_small_w50():
    wcorr = correct_w50(5.0, wturb=10.0)
    assert np.isclose(wcorr, 0.0)


def test_fit_btfr_ols():
    log_m = np.array([9.0, 10.0, 11.0])
    log_v = np.array([1.7, 2.0, 2.3])
    intercept, slope = fit_btfr_ols(log_m, log_v)
    assert np.isfinite(intercept)
    assert np.isfinite(slope)
    assert abs(slope - 0.3) < 0.1


def test_predict_velocity():
    log_m = np.array([9.0, 10.0, 11.0])
    pred = predict_velocity(log_m, 0.5, 0.25)
    expected = 0.5 + 0.25 * log_m
    np.testing.assert_allclose(pred, expected)


def test_compute_btfr_residuals():
    obs = np.array([2.0, 2.5, 3.0])
    pred = np.array([1.9, 2.6, 2.9])
    residuals = compute_btfr_residuals(obs, pred)
    expected = np.array([0.1, -0.1, 0.1])
    np.testing.assert_allclose(residuals, expected)


def test_fit_and_residualize():
    rng = np.random.default_rng(42)
    n = 50
    log_m = rng.uniform(9, 11, n)
    log_v = 0.5 + 0.25 * log_m + rng.normal(0, 0.05, n)
    df = pd.DataFrame({"logMbar": log_m, "logVflat": log_v})
    result = fit_and_residualize(df)
    assert "btfr_intercept" in result.columns
    assert "btfr_slope" in result.columns
    assert "btfr_residual_dex" in result.columns
    assert "btfr_abs_residual" in result.columns
    assert np.all(np.isfinite(result["btfr_residual_dex"]))
    assert abs(result["btfr_intercept"].iloc[0] - 0.5) < 0.2
    assert abs(result["btfr_slope"].iloc[0] - 0.25) < 0.05
