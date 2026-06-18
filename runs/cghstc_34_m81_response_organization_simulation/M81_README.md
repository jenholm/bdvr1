CGHSTC-34 M81: Response-organization simulation — BTFR approach diagnostic
=====================================================================================

Status: complete diagnostic visual branch.

Purpose
-------
Build a visual simulation from the M69 layout while updating the science layer to the
response-organization / BTFR approach framework:
- f_star vs alpha_BTFR map replaces f_star vs log10_Sigma_b maturity map
- Coherence state components (BTFR offset, c_coherence, c_fstar, c_sigma, c_org, alpha_BTFR)
  replace organization score / A_gov components
- alpha_BTFR timeline replaces A_gov_current timeline

Claim boundary
--------------
This is a visual diagnostic only. It does not promote the governor into the M36 mature
velocity law, does not refit M36, does not promote proxy rows to Tier A direct labels,
and does not rewrite the manuscript.
UGC07125 remains quarantined follow-up only, not a clean scalar object or juvenile prototype.

Visual page guide
-----------------
The browser page is a three-view diagnostic dashboard:

View 1: BTFR approach map (upper-left)
----------------------------------------
f_star vs alpha_BTFR with SPARC state cloud, BTFR reference line (alpha=1),
organization transition zone (f_star ~0.20-0.45, alpha ~0.75-1.05), and
a moving formation-track tracker with trailing path.

View 2: Live disk response simulation (center/right)
------------------------------------------------------
Particle-disk visualization with coherence state component bars:
- BTFR_offset_dex: offset from the BTFR relation in dex
- c_coherence: combined coherence proxy
- c_fstar: f_star contribution to coherence
- c_sigma: surface-density contribution to coherence
- c_org: organization score contribution to coherence
- alpha_BTFR: BTFR approach metric

A velocity inset shows v_N, v_BDVR full, v_governed, and alpha_BTFR.

View 3: BTFR approach timeline (bottom)
-----------------------------------------
alpha_BTFR curve along the selected formation track with BTFR reference
line (alpha=1) and current-position marker.

Controls
--------
- Space: pause/resume
- ArrowLeft/ArrowRight: step timeline
- ArrowUp/ArrowDown: change formation run
- H: Historic initial-position mode
- N: Random initial-position mode
- R: restart
- S: save PNG snapshot

Outputs
-------
- M81_README.md
- VISUAL_SIMULATION_RUN_INSTRUCTIONS.md
- m81_random_initialization_sequence.csv
- m81_random_initialization_tracks.csv
- m81_response_organization_state_table.csv
- m81_response_organization_tracks.csv
- m81_summary.json
- m81_transition_zone_spec.json
- m81_visual_simulation.html
- m81_visual_simulation_data.json

Summary
-------
{
  "formation_track_rows": 3872,
  "governor_promoted": false,
  "initialization_mix": {
    "claim_boundary": "initialization_mix_for_visual_simulation_not_population_inference",
    "failed_low_activation_count": 4,
    "failed_low_activation_target_fraction": 0.3,
    "stable_spiral_count": 28,
    "stable_spiral_target_fraction": 0.7
  },
  "initialization_modes": [
    "historic",
    "random"
  ],
  "m36_refit": false,
  "manuscript_rewritten": false,
  "mature_velocity_law_changed": false,
  "milestone": "CGHSTC-34-M81",
  "outcome_classification": "visual_diagnostic_response_organization_updated_from_m69",
  "proxy_rows_promoted_to_direct_validation": false,
  "state_rows": 96,
  "status": "response_organization_visual_simulation_diagnostic",
  "target": {
    "BTFR_offset_dex": -0.34061317523521417,
    "alpha_BTFR": 0.3886403773950502,
    "c_coherence": 0.3272232599034426,
    "galaxy_name": "UGC07125",
    "phase_region": "measurement_limited",
    "role": "quarantined_follow_up_not_clean_scalar_or_juvenile_prototype"
  },
  "ugc07125_clean_scalar_object": false,
  "ugc07125_quarantined": true,
  "visual_style_reference": "M69 layout preserved; M69 files not edited"
}
