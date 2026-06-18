# M39 inverse-rank / disorder-axis diagnostic

Diagnostic branch only; not a mature-galaxy velocity law.

This run regenerated M39 from verified M36/M37/M38 source artifacts and does not rely on the disputed previous inverse-rank output set.

Primary outcome: `target_contamination_or_quality_axis`

Rank flip alone is not physical validation. UGC07125 behavior is necessary but not sufficient.

## Summary JSON

{
  "milestone": "CGHSTC-34-M39",
  "status": "inverse_rank_disorder_axis_diagnostic_regenerated_from_verified_sources",
  "primary_outcome": "target_contamination_or_quality_axis",
  "manuscript_rewritten": false,
  "mature_velocity_law_changed": false,
  "governor_promoted": false,
  "rank_flip_alone_is_validation": false,
  "input_schema_audit": {
    "m38_direct_exists": true,
    "m38_cv_exists": true,
    "m37_direct_exists": true,
    "m36_predictions_exists": true,
    "m38_summary_exists": true,
    "required_columns_present": true,
    "missing_required_m38_columns": [],
    "used_disputed_inverse_rank_outputs": false
  },
  "n_direct_rows": 87,
  "n_primary_rows": 41,
  "n_mature_controls": 46,
  "disorder_axis_interpretation": "insufficient_independent_disorder_data",
  "target_contamination_check": "quality_axis_plausible",
  "missing_decisive_disorder_columns": [
    "SFR_or_depletion_time",
    "direct_outer_curve_quality_flag",
    "direct_HI_warp_asymmetry_for_most_rows"
  ],
  "ugc07125_behavior": {
    "taxonomy_stage": "failed_stalled",
    "quarantine_flag": true,
    "D_unsettled_m39": 0.8427145490592466,
    "A_activation_flip_m39": 0.1572854509407534,
    "A_target_m39": 0.185688488795864,
    "necessary_but_not_sufficient": true
  },
  "artifacts": {
    "predictions": "/home/jenholm/photonland/cghs/cghstc_34/runs/cghstc_34_m39_inverse_rank_disorder_axis_diagnostic/m39_inverse_rank_predictions.csv",
    "flip_metrics": "/home/jenholm/photonland/cghs/cghstc_34/runs/cghstc_34_m39_inverse_rank_disorder_axis_diagnostic/m39_flip_metric_summary.csv",
    "disorder_cluster_summary": "/home/jenholm/photonland/cghs/cghstc_34/runs/cghstc_34_m39_inverse_rank_disorder_axis_diagnostic/m39_disorder_cluster_summary.csv",
    "target_contamination_summary": "/home/jenholm/photonland/cghs/cghstc_34/runs/cghstc_34_m39_inverse_rank_disorder_axis_diagnostic/m39_target_contamination_summary.csv",
    "priority_rows": "/home/jenholm/photonland/cghs/cghstc_34/runs/cghstc_34_m39_inverse_rank_disorder_axis_diagnostic/m39_priority_rows.csv"
  },
  "claim_boundaries": [
    "No mature velocity law changed; M36 hybrid halo-energy BDVR no-governor remains the mature/clean scalar velocity endpoint.",
    "No manuscript rewrite was performed or warranted by this diagnostic branch.",
    "Rank flip alone is not physical validation; RMSE, object behavior, and independent disorder indicators must also support the interpretation.",
    "UGC07125 behavior is necessary but not sufficient; it remains a quarantined failed/stalled boundary object, not a juvenile prototype or clean scalar object.",
    "External/proxy rows are follow-up priorities unless they contain direct activation diagnostics."
  ]
}