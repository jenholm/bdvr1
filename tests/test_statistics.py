"""Tests for statistical utilities."""

from __future__ import annotations

import numpy as np
import pandas as pd

from bdvr1.statistics import (
    scatter_by_quartile,
    q4_q1_ratio,
    bootstrap_q4_q1,
    spearman_proxy_abs_residual,
    mass_residualized_correlation,
    mass_matched_quartile_scatter,
    measurement_quality_regression,
)


def _make_df(n=40):
    rng = np.random.default_rng(42)
    proxy = np.linspace(0, 1, n)
    residual = 0.1 * (1 - proxy) + rng.normal(0, 0.02, n)
    return pd.DataFrame({
        "proxy": proxy,
        "btfr_abs_residual": np.abs(residual),
        "logMbar": rng.uniform(9, 11, n),
        "INCL": rng.uniform(30, 80, n),
    })


def test_scatter_by_quartile():
    df = _make_df()
    result = scatter_by_quartile(df)
    assert "Q1" in result
    assert "Q4" in result
    assert result["Q1"]["N"] > 0
    assert result["Q4"]["N"] > 0
    # Q4 should have lower scatter (proxy anti-correlated)
    assert result["Q4"]["scatter_std"] <= result["Q1"]["scatter_std"] + 1e-6


def test_q4_q1_ratio():
    df = _make_df()
    result = q4_q1_ratio(df)
    assert "Q4_Q1_ratio" in result
    assert result["Q4_Q1_ratio"] <= 1.0 + 1e-6
    assert result["N_Q4"] > 0
    assert result["N_Q1"] > 0


def test_bootstrap_q4_q1():
    df = _make_df()
    result = bootstrap_q4_q1(df, n_boot=50)
    assert "bootstrap_Q4_Q1_ratio" in result
    assert "bootstrap_Q4_Q1_ci_95_low" in result
    assert "bootstrap_Q4_Q1_ci_95_high" in result
    assert result["n_bootstrap"] == 50


def test_spearman_proxy_abs_residual():
    df = _make_df()
    result = spearman_proxy_abs_residual(df)
    assert "spearman_rho" in result
    assert "spearman_p" in result
    assert result["spearman_rho"] < 0  # anti-correlated by construction


def test_mass_residualized_correlation():
    df = _make_df()
    result = mass_residualized_correlation(df)
    assert "spearman_mass_residualized_C_vs_abs" in result
    assert result["N"] > 0


def test_mass_matched_quartile_scatter():
    df = _make_df(n=80)
    result = mass_matched_quartile_scatter(df)
    assert "mass_matched_ratio" in result


def test_measurement_quality_regression():
    df = _make_df()
    result = measurement_quality_regression(df)
    assert "r2_controls_only" in result
    assert "r2_controls_plus_proxy" in result
    assert "delta_r2" in result
    assert result["N"] > 0
