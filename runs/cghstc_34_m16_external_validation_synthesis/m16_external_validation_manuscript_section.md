# External proxy diagnostics across gas, H I structure, IFU, and early-type systems

The M11--M15 external-data sequence provides a cross-dataset consistency audit for the CGHSTC-34 evolutionary-governor picture. These diagnostics are deliberately heterogeneous: THINGS supplies resolved H I structure, MaNGA supplies a large-N scalar proxy sample, ATLAS3D supplies early-type angular-momentum structure, and xGASS/xCOLD GASS supplies gas depletion and molecular/atomic gas information. The sequence is not direct BDVR validation, not `A_gov_inferred` except where explicitly transferred from M9 as a pilot diagnostic, and not a replacement for dark matter.

| Stage | Dataset | N | Class | Headline artifact result | Manuscript weight |
|---|---:|---:|---|---|---|
| M11 | THINGS | 8 | transferred_activation_pilot | Spearman(S_HI_disturbance, A_gov_inferred) = -0.283; low-A median disturbance 0.700 vs high-A 0.550 | pilot diagnostic only |
| M12 | MaNGA | 10185 | large_N_scalar_proxy | N=10185; Spearman(A_proxy, surface density)=0.367; Spearman(A_proxy, sSFR)=-0.391 | large-N proxy support |
| M13 | ATLAS3D | 260 | mixed_support_bridge_proxy | N=260; fast-rotator median bridge 0.551 vs slow-rotator 0.186 | early-type bridge proxy support |
| M14 | ATLAS3D | 260 | pressure_channel_proxy | N=260; slow-rotator median pressure response 0.750 vs fast-rotator 0.469 | separate spheroid mapping proxy support |
| M15 | xGASS/xCOLD GASS | 562 | gas_depletion_maturity_proxy | N=562; Spearman(maturity, f_gas)=-0.950; Spearman(maturity, M_H2/M_HI)=0.373 | gas/maturity proxy support |

Taken together, the external proxy diagnostics are coherent with the proposed maturity ordering: gas-rich systems rank low in the xGASS/xCOLD maturity proxy, compact and low-sSFR MaNGA systems rank higher in scalar proxy activation, ATLAS3D fast rotators occupy a mixed-support bridge branch, and slow rotators require a separate pressure-supported spheroid channel. The THINGS cross-match is much smaller and should be treated only as a pilot H I structure diagnostic.

Claim boundary: this synthesis is external_proxy_synthesis_not_direct_validation. It does not establish the BDVR law, does not replace a full rotation-curve likelihood analysis, is not a replacement for dark matter, and does not complete lensing/X-ray/dynamical-excess validation for ellipticals.

deferred stricter tests:
- full resolved SPARC and non-SPARC rotation-curve fitting with uncertainty propagation
- matched BTFR/RAR/halo-model comparison on the same sample and predeclared loss functions
- direct dynamical-excess, lensing, X-ray, and dark-matter-fraction tests for pressure-supported ellipticals
- larger THINGS/LITTLE THINGS-style H I structure samples with direct kinematic modeling
- hierarchical treatment of proxy definitions, selection functions, and measurement covariance
