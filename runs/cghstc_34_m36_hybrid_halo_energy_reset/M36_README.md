# M36 Hybrid halo-energy BDVR reset

No manuscript rewrite was performed.

UGC07125 quarantined from the clean scalar sample based on independent H I geometry/audit evidence, not because of numerical residual size alone.

## Comparison branches

- without governor: original hybrid halo-energy BDVR response, `Q_eff = Q_base H_halo S_star_gas S_internal`.
- with governor: same full-response endpoint multiplied by a bounded product-gate activation before converting back to velocity.

## Metric comparison

| sample | branch | n_galaxies | median_abs_log10_velocity_error | mean_abs_log10_velocity_error | max_abs_log10_velocity_error | frac_within_010_dex | n_within_010_dex | frac_within_015_dex | n_within_015_dex | frac_within_020_dex | n_within_020_dex | median_velocity_ratio_pred_over_obs | worst_galaxy | worst_abs_log10_velocity_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reference_87 | hybrid_no_governor | 87 | 0.0416139 | 0.0457214 | 0.23214 | 0.954023 | 83 | 0.988506 | 86 | 0.988506 | 86 | 1.0215 | UGC07125 | 0.23214 |
| reference_87 | hybrid_with_governor | 87 | 0.101917 | 0.136486 | 0.419754 | 0.494253 | 43 | 0.632184 | 55 | 0.689655 | 60 | 0.795184 | UGC06667 | 0.419754 |
| clean_86_quarantine_UGC07125 | hybrid_no_governor | 86 | 0.0410299 | 0.0435538 | 0.144578 | 0.965116 | 83 | 1 | 86 | 1 | 86 | 1.01677 | UGC07399 | 0.144578 |
| clean_86_quarantine_UGC07125 | hybrid_with_governor | 86 | 0.102179 | 0.136919 | 0.419754 | 0.488372 | 42 | 0.627907 | 54 | 0.686047 | 59 | 0.792531 | UGC06667 | 0.419754 |

## Best clean-86 governor fit

| sample | f_star_c | log10_sigma_c | f_gas_c | RHI_Rd_c | k_star | k_sigma | k_gas | k_HI | activation_mse | spearman_A_pred_A_inferred | rank_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clean_86_quarantine_UGC07125 | 0.25 | 7.8 | 0.7 | 8 | 14 | 6 | 12 | 0.75 | 0.297622 | 0.0930824 | 0.294829 |
| clean_86_quarantine_UGC07125 | 0.25 | 7.8 | 0.7 | 8 | 14 | 6 | 12 | 1.5 | 0.307002 | 0.112242 | 0.303635 |
| clean_86_quarantine_UGC07125 | 0.25 | 7.8 | 0.7 | 8 | 8 | 6 | 12 | 0.75 | 0.308714 | 0.0768873 | 0.306407 |
| clean_86_quarantine_UGC07125 | 0.25 | 7.8 | 0.7 | 8 | 14 | 6 | 6 | 0.75 | 0.311301 | 0.0709683 | 0.309172 |
| clean_86_quarantine_UGC07125 | 0.25 | 7.8 | 0.7 | 8 | 14 | 3 | 12 | 0.75 | 0.313158 | 0.0650294 | 0.311207 |

## Primary readout

hybrid_no_governor_preferred_for_clean_scalar_sample
