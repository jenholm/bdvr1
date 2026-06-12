# BDVR Hypothesis Summary

The Bound Domain Vacuum Response (BDVR) hypothesis proposes that coherent baryonic structures couple to a vacuum/time-current reservoir, producing an acceleration term that scales as sqrt(a_b * a0) with a coupling strength Q that depends on the galaxy's organizational state.

## Key idea

In the BDVR picture, the observed total acceleration is:

a_obs(r) = a_b(r) + Q_eff(r) * sqrt(a_b(r) * a0)

where Q_eff is not universal but depends on how "organized" the galaxy is — its stellar fraction, surface density, kinematic settling, and gas distribution.

## Why BTFR scatter?

If Q varies systematically across galaxy populations, then the Baryonic Tully-Fisher Relation — which traces the relationship between baryonic mass and flat rotation velocity — should show population-dependent scatter. Galaxies with higher organization proxies should have more consistent (less scattered) BTFR endpoints.

## What this package tests

This package tests scalar proxies (not the BDVR coordinate itself):
- For xGASS: a coherence proxy combining inclination, linewidth, and gas fraction
- For SPARC: a proxy based on H I extent and stellar surface density

The key prediction: galaxies in the top quartile of organization proxies should have smaller BTFR scatter than those in the bottom quartile (Q4/Q1 < 1).

## Limitations of scalar proxies

Scalar proxies cannot distinguish between:
1. True BDVR organization (the proposed physical coordinate)
2. Observational selection effects (inclination, linewidth recoverability)
3. Simple mass or surface brightness trends

Resolved H I kinematics (kinematic maps, lopsidedness, warp indices) are needed for a decisive test.
