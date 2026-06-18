# CGHSTC-34-M3a SPARC-lite 12-Galaxy Checkpoint

## Status

CGHSTC-34-M3a passed the initial 12-galaxy observed-data SPARC-lite sanity test.

## Claim boundary

This is not a full SPARC fit.
This is not a dark matter replacement claim.
This is not a full rotation-curve decomposition.

This is a first observed-galaxy sanity test using SPARC Table1-style baryonic inputs.

## Model rule

No custom dark halos.
No per-galaxy Q tuning.
One global q_galaxy was used for all galaxies.

## Formula

v_bdvr = (q_galaxy^2 * G * M_baryon * a0)^(1/4)

## Constants

a0_m_s2 = 1.2e-10
q_galaxy = 0.9002495108803148
q_source = global_q_from_cghstc34_m2_domain_coupling_table

## Result summary

n_galaxies = 12
median_abs_log10_velocity_error = 0.05829996370826813
mean_abs_log10_velocity_error = 0.07105470210410737
max_abs_log10_velocity_error = 0.16942400798037563

frac_within_010_dex = 0.75
frac_within_015_dex = 0.8333333333333334
frac_within_030_dex = 1.0

n_within_010_dex = 9
n_within_015_dex = 10
n_within_030_dex = 12

median_velocity_ratio_pred_over_obs = 0.8744584559357234

m3_passes_basic_checks = true
m3_passes_soft_checks = true
m3_has_factor_two_problem = false

## Worst residuals

Worst galaxies by absolute log10 velocity error:

1. NGC2841: ratio = 0.676980, log10_error = -0.169424
2. NGC7814: ratio = 0.682897, log10_error = -0.165645
3. NGC3521: ratio = 0.738048, log10_error = -0.131916
4. NGC2403: ratio = 0.797268, log10_error = -0.098395

Best galaxies:

1. DDO154: ratio = 1.009255, log10_error = 0.004001
2. NGC5055: ratio = 1.037200, log10_error = 0.015862
3. NGC3198: ratio = 0.961384, log10_error = -0.017103
4. NGC6946: ratio = 0.952334, log10_error = -0.021211

## Interpretation

BDVR passed the initial observed-galaxy SPARC-lite sanity test under the conservative M3a criteria.

The residuals are mostly negative, so the model has a mild low-velocity bias. The largest underpredictions are NGC2841, NGC7814, and NGC3521. These are likely the first forensic targets for M3b.

The model performs especially well on DDO154, NGC5055, NGC3198, and NGC6946 under this simplified mass-only velocity formula.

## Next milestone

CGHSTC-34-M3b:

Inspect residual structure and determine whether the low-bias is tied to mass, scale length, morphology, bulge dominance, quality flag, or the simplified point-BTFR prediction formula.

Then:

CGHSTC-34-M3c:

Run a larger quality-1 SPARC-lite sample using the same fixed global q_galaxy and no per-galaxy tuning.
