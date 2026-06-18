# M38 M18-feedback governor on M37 juvenile/failed set

No manuscript rewrite was performed. The governor is not part of the mature-galaxy velocity prediction.

Selected claim: differential_feedback_diagnostic_not_promoted

## Summary

{
  "milestone": "CGHSTC-34-M38",
  "status": "m18_differential_feedback_retested_on_m37_set",
  "governor_role": "M18_differential_feedback_retested_as_onset_hypothesis",
  "mature_disks_used_as_primary_fit_set": false,
  "primary_dataset": "M37 juvenile/failed/disturbed direct SPARC set",
  "hybrid_velocity_endpoint": "M36 hybrid halo-energy BDVR no-governor endpoint",
  "equation": {
    "dA_dtau": "lambda_seed D(g)(1-A) + lambda_feedback D(g) A(1-A) - lambda_reservoir R(g) A"
  },
  "n_direct_sparc": 87,
  "n_primary_fit": 41,
  "n_mature_control": 46,
  "n_external_proxy": 78,
  "selected_model_claim": "differential_feedback_diagnostic_not_promoted",
  "primary_fit_rmse": 0.3517568056977246,
  "primary_fit_spearman": -0.42508613772804,
  "primary_cv_rmse": 0.37926032745689264,
  "primary_cv_spearman": -0.5116613652786487,
  "m37_static_primary_rmse": 0.5117710280218454,
  "m37_static_primary_spearman": -0.3627661375280108,
  "mature_control_median_A_pred": 0.9971340129808922,
  "mature_control_fraction_A_pred_gt_0p5": 1.0,
  "ugc07125_A_pred": 0.8427145490592466,
  "claim_boundaries": [
    "The governor is not part of the mature-galaxy velocity prediction.",
    "Mature/control SPARC rows are controls, not the primary threshold-discovery dataset.",
    "External rows are proxy prioritization only unless they have a direct M36 endpoint and independent onset observables.",
    "M38 tests the M18 ODE as a governor-onset mechanism, not as a first-principles accepted BDVR law."
  ],
  "artifact_dir": "/home/jenholm/photonland/cghs/cghstc_34/runs/cghstc_34_m38_m18_feedback_on_m37_juvenile_failed_set",
  "m18_equation_source_exists": true
}

## Stage performance

taxonomy_stage,n,median_A_inferred,median_A_pred_m38_feedback,rmse_full,spearman_full,rmse_cv_primary_only,median_m37_static_A_pred
disturbed_or_measurement_contaminated,3,0.6433123110527825,0.9386387062464125,0.3163171995899531,1.0,0.32139202117283916,0.7488772601347756
failed_stalled,5,0.5876019195241267,0.8427145490592466,0.42067730862387476,0.3,0.44121951756777267,0.2549507836184513
juvenile_forming,24,1.0,0.8851573187857815,0.2721581446202549,-0.06634549538179652,0.3284584819853059,0.3785074292317147
mature_or_control,46,1.0,0.9971340129808922,0.16469689093852574,-0.0783586650541605,,0.9245403170876312
true_falsifier_candidate,9,0.6044754277243196,0.9981267547347478,0.48423465683506545,-0.5,0.47432795063032906,0.8396457371851015


## Selected model

f_star_c,k_star,log10_sigma_c,k_sigma,f_gas_c,k_gas,RHI_Rd_c,k_HI,drive_power,A0,lambda_seed,lambda_feedback,lambda_reservoir,disturbance_weight,failed_weight,n_steps,tau_final,n_primary_fit,n_mature_control,primary_fit_rmse,primary_fit_spearman,primary_cv_rmse,primary_cv_spearman,train_fit_rmse,train_fit_spearman,m37_static_primary_rmse,m37_static_primary_spearman,mature_control_median_A_pred,mature_control_fraction_A_pred_gt_0p5,ugc07125_A_pred,rank_score,selected_model_claim
0.25,8.0,8.0,4.0,0.75,8.0,12.0,1.0,0.35,0.1,4.0,4.0,0.5,0.4,0.4,80,1.0,41,46,0.3517568056977246,-0.42508613772804,0.37926032745689264,-0.5116613652786487,0.3517568056977246,-0.42508613772804,0.5117710280218454,-0.3627661375280108,0.9971340129808922,1.0,0.8427145490592466,0.3645093898295658,differential_feedback_diagnostic_not_promoted
