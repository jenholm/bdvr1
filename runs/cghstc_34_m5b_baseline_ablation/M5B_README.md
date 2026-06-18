CGHSTC-34 M5b: Baseline and Ablation Comparison
==========================================================

Status: complete.

Purpose
-------
Compare frozen M4c against simple baselines and ablations on the same 87-galaxy M5 Q=1 sample.
No retuning. No per-galaxy Q. No outlier deletion.

Models
------
newtonian_outer: baryonic Newtonian velocity at adaptive evaluation radius.
mond_simple_btfr: deep-MOND/BTFR v^4 = G M a0.
m3_scalar_q_only: v^4 = q_base^2 G M a0.
m4a_halo_only: q_base times halo radial activation.
m4b_halo_star_gas: M4a plus star/gas structural hinge.
m4c_full_frozen: M4b plus early-type internal hinge.

Best model by median absolute log10 velocity error
--------------------------------------------------
{
  "model": "m4b_halo_star_gas",
  "n": 87,
  "median_abs_log10_velocity_error": 0.04044580913763483,
  "mean_abs_log10_velocity_error": 0.046439185144479624,
  "max_abs_log10_velocity_error": 0.23214012979801618,
  "median_log10_velocity_error": -0.006183480835373096,
  "mean_log10_velocity_error": -0.006839692937082956,
  "median_velocity_ratio_pred_over_obs": 0.9858628900488806,
  "frac_within_010_dex": 0.9310344827586207,
  "frac_within_015_dex": 0.9885057471264368,
  "frac_within_020_dex": 0.9885057471264368,
  "n_within_010_dex": 81,
  "n_within_015_dex": 86,
  "n_within_020_dex": 86,
  "n_above_010_dex": 6,
  "n_above_015_dex": 1,
  "n_above_020_dex": 1,
  "n_above_030_dex": 0
}

Summary table
-------------
            model  n  median_abs_log10_velocity_error  mean_abs_log10_velocity_error  max_abs_log10_velocity_error  median_log10_velocity_error  mean_log10_velocity_error  median_velocity_ratio_pred_over_obs  frac_within_010_dex  frac_within_015_dex  frac_within_020_dex  n_within_010_dex  n_within_015_dex  n_within_020_dex  n_above_010_dex  n_above_015_dex  n_above_020_dex  n_above_030_dex
  newtonian_outer 87                         0.249744                       0.244856                      0.448825                    -0.249744                  -0.243381                             0.562673             0.068966             0.206897             0.344828                 6                18                30               81               69               57               31
 mond_simple_btfr 87                         0.047226                       0.056113                      0.205226                    -0.039505                  -0.036949                             0.913050             0.839080             0.965517             0.988506                73                84                86               14                3                1                0
 m3_scalar_q_only 87                         0.064131                       0.069255                      0.211354                    -0.062324                  -0.059768                             0.866316             0.758621             0.896552             0.988506                66                78                86               21                9                1                0
    m4a_halo_only 87                         0.041614                       0.050371                      0.232140                    -0.016528                  -0.011832                             0.962657             0.896552             0.977011             0.988506                78                85                86                9                2                1                0
m4b_halo_star_gas 87                         0.040446                       0.046439                      0.232140                    -0.006183                  -0.006840                             0.985863             0.931034             0.988506             0.988506                81                86                86                6                1                1                0
  m4c_full_frozen 87                         0.041614                       0.045721                      0.232140                     0.009239                   0.006454                             1.021502             0.954023             0.988506             0.988506                83                86                86                4                1                1                0

Outputs
-------
m5b_all_model_predictions.csv
m5b_model_comparison_summary.csv
m5b_residual_correlations_by_model.csv
m5b_median_abs_error_by_model.png
m5b_frac_within_010_by_model.png
m5b_pred_vs_obs_grid.png
m5b_residual_vs_mass_grid.png
m5b_ugc07125_model_comparison.txt

UGC07125 prediction-regime note
-------------------------------
UGC07125 should not be deleted or tuned away.
If similar late-type gas-dominated galaxies are also overpredicted, this may identify a missing conditioning regime.
That would turn the outlier into a testable prediction target.
