# CGHSTC-34-M4c Early-Type Internal Response Checkpoint

## Status

CGHSTC-34-M4c passed both basic and soft checks on the 12-galaxy SPARC-lite rich sample.

## Model

Q_eff(r, galaxy)
=
Q_base
* H_halo(r / R_d)
* S_star_gas(star_frac, gas_frac)
* S_internal(T)

Velocity estimator:

v_flat = (Q_eff^2 * G * M_baryon * a0)^(1/4)

## Parameters

q_base = 0.9002495108803148
a0_m_s2 = 1.2e-10

halo_amplitude = 0.35
halo_k = 3.0
r_eval_mode = transition
velocity_mode = flat_response

structural_mode = star_gas_hinge
structural_amplitude = 0.30
star_gas_threshold = 5.0

internal_mode = early_type_hinge
internal_amplitude = 0.10
early_type_threshold = 5.0

## Result

m4_passes_basic_checks = true
m4_passes_soft_checks = true

median_abs_log10_velocity_error = 0.027699
max_abs_log10_velocity_error = 0.081652
median_velocity_ratio_pred_over_obs = 1.004618
residual_vs_v_flat_obs = -0.305239
n_within_010_dex = 12
n_within_015_dex = 12

## Worst remaining residuals

NGC5055:
  ratio = 1.206847
  log10_error = +0.081652

NGC2841:
  ratio = 0.839957
  log10_error = -0.075743

NGC2403:
  ratio = 0.869972
  log10_error = -0.060495

NGC3521:
  ratio = 0.880657
  log10_error = -0.055193

## Interpretation

The best M4c model requires:

1. radial halo-response activation,
2. gas-poor / stellar-dominated structural response,
3. early-type internal morphology response.

This supports the working hypothesis that the halo-like BDVR response is controlled by internal baryonic source geometry, not total baryonic mass alone.

## Claim boundary

This is a 12-galaxy SPARC-lite pilot result.
This is not a full SPARC fit.
This is not a dark matter replacement claim.
This is not a per-galaxy Q tuning result.

All response parameters are global.
Galaxy-to-galaxy variation comes from observed SPARC-style structural fields.
