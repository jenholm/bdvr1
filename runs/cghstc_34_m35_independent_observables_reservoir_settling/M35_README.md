# M35 independent-observables Reservoir--Settling Governor diagnostic

## What was tried

- Current product gate baseline.
- Reservoir--Settling candidate using scalar reservoir features plus sparse independent H I disturbance.
- THINGS-only H I disturbance crossmatch test.
- OOF scalar+sparse-H I ridge diagnostic.
- Velocity/angular side-channel diagnostics, explicitly marked leaky/target-adjacent.
- External proxy coherence tests using xGASS/xCOLD, THINGS, MaNGA, and ATLAS3D.

## SPARC-direct fit results

See `m35_sparc_fit_summary.csv`.

Current product gate Spearman rho: `0.145881`.
Best nonleaky M35 SPARC candidate: `oof_scalar_plus_sparse_hi` with rho `0.410010`.

The new independent-observable Reservoir--Settling candidate did not beat the current product gate.

## External proxy coherence results

See `m35_external_proxy_coherence_summary.csv`. These results show proxy-dataset coherence, not direct BDVR activation validation.

## independent SFR/depletion observables

Available now through M15 xGASS/xCOLD external proxy rows. Direct SPARC-row SFR/depletion crossmatch coverage in this run was zero.

## kinematic-settling observables

Available now through M11 THINGS H I disturbance for 8 SPARC crossmatches, M12 MaNGA scalar proxy rows, and M13/M14 ATLAS3D lambda_R/V-sigma proxies. Direct SPARC independent kinematic-settling coverage is sparse.

UGC07125 remains quarantined/excluded from clean scalar/prototype use.

Claim boundary: diagnostic independent-observables test, not an accepted model revision.
