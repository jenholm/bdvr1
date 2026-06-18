CGHSTC-34 M8: Juvenile-to-mature BDVR evolution simulation
======================================================================

Status: complete diagnostic run.

Purpose
-------
Implement the juvenile-to-mature reservoir activation hypothesis as a bounded diagnostic simulation.
The run uses SPARC-lite quality-1 table inputs to derive stellar fraction, gas fraction, baryonic surface density, implied reservoir activation, and toy evolution tracks.

Claim boundary
--------------
This is not an accepted BDVR model term, not a retuning of frozen M4c, and not a proof of a galaxy-evolution mechanism.
It is a falsifiable diagnostic layer for locating possible A_gov ~ 0.5 transition systems.

Outputs
-------
m8_evolution_inputs.csv
m8_evolution_galaxy_states.csv
m8_evolution_tracks.csv
m8_transition_candidates.csv
m8_summary.json
m8_activation_vs_maturity.png
m8_example_tracks.png
m8_visual_simulation.html
m8_visual_simulation_data.json
VISUAL_SIMULATION_RUN_INSTRUCTIONS.md

Summary
-------
{
  "activation_formula": "A_gov = sigmoid(f_star-fcrit) * sigmoid(log10Sigma_b-log10SigmaCrit) optionally times gas suppression",
  "claim_boundary": "juvenile_to_mature_governor_hypothesis_only",
  "class_counts": {
    "juvenile": 14,
    "mature": 41,
    "transition": 32
  },
  "implied_activation_formula": "A_implied = (V_obs^2 - V_N^2) / (V_full_BDVR^2 - V_N^2), clipped to [0,1]",
  "interpretation_boundary": "M8 is a diagnostic evolution simulation inspired by the juvenile-to-mature and enhanced-rotation-support notes. It does not accept a new BDVR term, does not retune frozen M4c, and does not claim a proven galaxy-evolution mechanism.",
  "median_A_gov_star_sigma": 0.7112971380206047,
  "median_A_implied": 1.0,
  "milestone": "CGHSTC-34-M8",
  "n_galaxies": 87,
  "n_near_half_activation_abs_lt_0_10": 4,
  "n_tracks": 4,
  "status": "diagnostic_evolution_simulation_not_accepted_model",
  "target": {
    "A_gov_star_sigma": 0.01970169080134811,
    "A_gov_star_sigma_gas": 0.0012464777138904944,
    "A_implied": 0.0,
    "f_gas": 0.8195025137868931,
    "f_star": 0.18049748621310685,
    "galaxy_name": "UGC07125",
    "log10_Sigma_b": 8.019775262749231,
    "maturity_class": "juvenile"
  }
}
