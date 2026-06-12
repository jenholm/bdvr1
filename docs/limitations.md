# Limitations

## Proxy limitations

1. **Unresolved scalars**: The xGASS and SPARC proxies use global, unresolved measurements (inclination, linewidth, gas fraction, surface brightness). They do not resolve the proposed BDVR organization coordinate.

2. **Inclination-linewidth entanglement**: The xGASS organization proxy explicitly includes both inclination and W50 linewidth. These are not entirely independent — inclined galaxies have broader linewidths due to projection, and measurement uncertainty in either propagates to the proxy.

3. **Gas term degeneracy**: The gas term, `1 - f_atm`, is entangled with stellar dominance, gas richness, stellar mass, and star-formation state. The proxy does not distinguish between a genuinely organized galaxy and a simply gas-poor one.

## Sample limitations

4. **SPARC selection**: SPARC is not volume-limited. The quality-1 subset and available scalar inputs may bias the analysis toward galaxies with better measured rotation curves and usable photometric/H I quantities.

5. **xGASS H I bias**: The H I-detected xGASS subsample over-represents gas-rich galaxies. Gas-poor galaxies, which may receive higher values under some organization-proxy definitions, are underrepresented.

6. **Overlapping samples**: SPARC and xGASS have minimal overlap. Cross-survey comparisons assume consistent proxy behavior across independent samples.

## Statistical limitations

7. **Modest sample sizes**: After quality cuts (SPARC Q=1, xGASS H I-detected with good flags), the samples are 87 SPARC galaxies and 363 xGASS H I-detected galaxies, with the main full-proxy analysis using 320 complete rows. Quartile bins have ~20-90 galaxies.

8. **Multiple comparisons**: The paper-facing ablation analysis tests seven proxy variants without formal multiple-testing correction.

9. **Causality**: Observed correlations between proxies and BTFR scatter do not establish a causal BDVR mechanism.

## Decisive test requirement

The scalar-proxy approach cannot distinguish between BDVR organization and mundane recoverability effects (inclination, projection, measurement precision). A decisive test requires resolved H I kinematics from interferometric observations (e.g., THINGS, VIVA, or new VLA/ASKAP/MeerKAT data) to compute kinematic asymmetry, lopsidedness, warp indices, and non-circular motion fractions.
