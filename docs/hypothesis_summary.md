# BDVR Hypothesis Summary

The Bound Domain Vacuum Response (BDVR) hypothesis is treated here as a **phenomenological** framework: baryonic structure and dynamical organization may influence how an additional effective acceleration response is expressed through ordered rotation.

## Key idea

In the BDVR picture, the observed total acceleration is:

a_obs(r) = a_b(r) + Q_eff(r) * sqrt(a_b(r) * a0)

where Q_eff is not universal but depends on how "organized" the galaxy is — its stellar fraction, surface density, kinematic settling, and gas distribution.

## Why BTFR scatter?

If Q varies systematically across galaxy populations, then the Baryonic Tully-Fisher Relation — which traces the relationship between baryonic mass and flat rotation velocity — should show population-dependent scatter. Galaxies with higher organization proxies should have more consistent (less scattered) BTFR endpoints.

## What this package tests

This package tests scalar proxies (not the BDVR coordinate itself):
- For xGASS: an organization proxy combining inclination, H I linewidth, and inherited atomic-gas-fraction information.
- For SPARC: two proxy products are documented. The paper-facing result uses the historical M74 coherence score (5-component average with radial-curve bonuses), treated in the paper as an organization proxy. The current pipeline also produces a separate diagnostic demographic proxy based on stellar surface density, stellar mass fraction, and H I extent.

The key prediction: galaxies in the top quartile of organization proxies should have smaller BTFR scatter than those in the bottom quartile (Q4/Q1 < 1).

## Limitations of scalar proxies

Scalar proxies cannot distinguish between:
1. A physical BDVR organization coordinate
2. Observational selection effects (inclination, linewidth recoverability)
3. Simple mass or surface brightness trends

Resolved H I kinematics (kinematic maps, lopsidedness, warp indices) are needed for a decisive test.
