"""Tests for proxy computation module."""

from __future__ import annotations

import numpy as np
import pandas as pd

from bdvr1.proxies import (
    compute_xgass_coherence_proxy,
    compute_sparc_demographic_proxy,
    compute_proxy_variant,
    assign_quartiles,
)


def _make_xgass_df(n=10):
    return pd.DataFrame({
        "INCL": np.linspace(20, 80, n),
        "W50cor": np.linspace(100, 400, n),
        "f_atm": np.linspace(0.1, 0.8, n),
    })


def _make_sparc_df(n=10):
    return pd.DataFrame({
        "RHI": np.linspace(5, 30, n),
        "Rdisk": np.linspace(1, 6, n),
        "SBdisk": np.linspace(100, 500, n),
        "L36": np.linspace(0.1, 10, n),
        "MHI": np.linspace(0.1, 5, n),
    })


def test_xgass_proxy_bounded():
    df = _make_xgass_df()
    C = compute_xgass_coherence_proxy(df)
    assert len(C) == len(df)
    assert C.between(0, 1).all()


def test_xgass_proxy_monotonic():
    df = _make_xgass_df()
    C = compute_xgass_coherence_proxy(df)
    vals = C.to_numpy()
    assert np.all(np.diff(vals) >= 0) or np.all(np.diff(vals) <= 0)


def test_sparc_proxy_bounded():
    df = _make_sparc_df()
    C = compute_sparc_demographic_proxy(df)
    assert len(C) == len(df)
    assert C.between(0, 1).all()


def test_proxy_variant_full():
    df = _make_xgass_df()
    C = compute_proxy_variant(df, "full")
    assert len(C) == len(df)
    assert C.between(0, 1).all()


def test_proxy_variant_incl_only():
    df = _make_xgass_df()
    C = compute_proxy_variant(df, "incl_only")
    assert len(C) == len(df)
    # incl_only = INCL / 90
    expected = df["INCL"].to_numpy() / 90.0
    np.testing.assert_allclose(C.to_numpy(), expected)


def test_proxy_variant_unknown():
    df = _make_xgass_df()
    try:
        compute_proxy_variant(df, "nonexistent")
        assert False, "should have raised ValueError"
    except ValueError:
        pass


def test_assign_quartiles():
    scores = pd.Series([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    q = assign_quartiles(scores)
    assert q.nunique() == 4
    # Q1 should have lowest scores, Q4 highest
    assert q.iloc[0] == "Q1"
    assert q.iloc[-1] == "Q4"


def test_assign_quartiles_edge():
    scores = pd.Series([0.5] * 10)
    q = assign_quartiles(scores)
    assert q.nunique() == 4
