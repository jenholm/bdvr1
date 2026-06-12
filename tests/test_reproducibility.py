"""Reproducibility integration tests."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from bdvr1.config import RANDOM_SEED, N_BOOTSTRAP, N_FOLDS
from bdvr1.btfr import fit_and_residualize
from bdvr1.proxies import compute_xgass_coherence_proxy, compute_sparc_demographic_proxy
from bdvr1.statistics import q4_q1_ratio, bootstrap_q4_q1
from bdvr1.validation import cross_validated_btfr_residuals


def test_random_seed_deterministic():
    rng1 = np.random.default_rng(RANDOM_SEED)
    rng2 = np.random.default_rng(RANDOM_SEED)
    np.testing.assert_array_equal(rng1.random(100), rng2.random(100))


def test_xgass_pipeline_synthetic():
    rng = np.random.default_rng(RANDOM_SEED)
    n = 100
    df = pd.DataFrame({
        "INCL": rng.uniform(20, 80, n),
        "W50cor": rng.uniform(100, 400, n),
        "f_atm": rng.uniform(0.05, 0.8, n),
        "logMbar": rng.uniform(9, 11, n),
        "logVflat": rng.uniform(1.5, 2.5, n),
    })
    df["proxy"] = compute_xgass_coherence_proxy(df)
    df = fit_and_residualize(df)
    qs = q4_q1_ratio(df)
    assert np.isfinite(qs["Q4_Q1_ratio"])


def test_sparc_pipeline_synthetic():
    rng = np.random.default_rng(RANDOM_SEED)
    n = 50
    df = pd.DataFrame({
        "RHI": rng.uniform(3, 40, n),
        "Rdisk": rng.uniform(0.5, 8, n),
        "SBdisk": rng.uniform(50, 800, n),
        "L36": rng.uniform(0.1, 10, n),
        "MHI": rng.uniform(0.1, 5, n),
        "logMbar": rng.uniform(9, 11, n),
        "logVflat": rng.uniform(1.5, 2.5, n),
    })
    df["proxy"] = compute_sparc_demographic_proxy(df)
    df = fit_and_residualize(df)
    qs = q4_q1_ratio(df)
    assert np.isfinite(qs["Q4_Q1_ratio"])


def test_bootstrap_reproducible():
    rng = np.random.default_rng(RANDOM_SEED)
    n = 60
    df = pd.DataFrame({
        "proxy": rng.uniform(0, 1, n),
        "btfr_abs_residual": rng.exponential(0.1, n),
    })
    r1 = bootstrap_q4_q1(df, n_boot=100)
    r2 = bootstrap_q4_q1(df, n_boot=100)
    assert r1["bootstrap_Q4_Q1_ratio"] == r2["bootstrap_Q4_Q1_ratio"]


def test_cv_btfr_synthetic():
    rng = np.random.default_rng(RANDOM_SEED)
    n = 60
    df = pd.DataFrame({
        "proxy": rng.uniform(0, 1, n),
        "logMbar": rng.uniform(9, 11, n),
        "logVflat": rng.uniform(1.5, 2.5, n),
    })
    result = cross_validated_btfr_residuals(df)
    if "error" not in result:
        assert np.isfinite(result["cv_held_out_Q4_Q1_ratio"])
        assert result["cv_folds"] == N_FOLDS


def test_directory_structure():
    required = [
        "src/bdvr1/__init__.py",
        "src/bdvr1/config.py",
        "src/bdvr1/io.py",
        "src/bdvr1/btfr.py",
        "src/bdvr1/proxies.py",
        "src/bdvr1/statistics.py",
        "src/bdvr1/validation.py",
        "src/bdvr1/plotting.py",
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "pyproject.toml",
        "Makefile",
    ]
    for f in required:
        assert Path(f).exists(), f"Missing required file: {f}"
