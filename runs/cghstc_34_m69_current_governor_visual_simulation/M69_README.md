CGHSTC-34 M69: Current governor visual simulation
======================================================================

Status: complete diagnostic visual branch.

Purpose
-------
Build a new visual simulation from the M8 look while updating the science layer to the current governor framework:
A_gov = A_star * A_Sigma * A_gas * A_settle, with dynamic organization score readouts.

Claim boundary
--------------
This is a visual diagnostic only. It does not promote the product-gate governor into the M36 mature velocity law, does not refit M36, does not promote proxy rows to Tier A direct labels, and does not rewrite the manuscript.
UGC07125 remains quarantined follow-up only, not a clean scalar object or juvenile prototype.

Visual page guide
-----------------
The browser page is a three-view diagnostic dashboard. It is meant to show how a selected formation track moves through baryonic maturity space, how the live disk visualization responds as the current-governor quantities evolve, and how A_gov_current rises or stays suppressed along the selected track. The page is descriptive and diagnostic: it is not a validated evolutionary reconstruction and it is not a new velocity-law fit.

All simulated formation tracks start in the juvenile low-f_star/high-gas sector. The stable-spiral versus failed/low-activation distinction is an outcome track distinction, not a statement that some galaxies are initialized as already mature high-f_star objects.

Initialization switch
---------------------
The display includes two initial-position controls in the control strip below the SPARC-lite maturity map.

Initialization buttons:

- Historic button: selects Historic mode, which uses the current data-anchored strategy. Initial positions are estimated from selected source galaxies in the current artifact pool, while still forcing visual formation tracks to begin in the juvenile low-f_star/high-gas sector. Historic mode keeps the data-anchored visible seed labels, so stable-spiral outcome labels retain the galaxy identifier after the track counter.
- Random button: selects Random mode. Random mode samples initial f_star and log10_Sigma_b positions within the empirical two-sigma envelope of the historic estimated initial positions. The sampled mass is mildly perturbed, and Rdisk_kpc is computed from the sampled log10_Sigma_b using the same Sigma_b formula, M_baryon/(2*pi*Rdisk^2). Random stable-spiral visible labels omit the seed galaxy identifier because the displayed initial position is a random draw; the seed/provenance fields remain in JSON/CSV for audit.

Random mode is a visual initialization option only. It is not population inference, not source-backed evolutionary reconstruction, and not a model-promotion result.

Cycling through simulations:

- ArrowUp/ArrowDown cycle through the selected mode's formation tracks.
- Historic cycling steps through data-anchored historic tracks; those labels keep the visible source-galaxy identifier.
- Random cycling steps through independently sampled random-initialization tracks; stable-spiral labels show only the generic random outcome-track counter.
- When the current track reaches its end, the display automatically advances to the next track in the selected mode.
- Switching between Historic and Random resets the displayed track index and animation clock to the first track for that selected initialization mode.

View 1: SPARC-lite maturity map
-------------------------------
The upper-left panel is the SPARC-lite maturity map: f_star vs log10 Sigma_b. It places the current M69 formation track on top of the SPARC-lite state cloud and the M42 current transition zone.

SPARC-lite maturity-map axes
----------------------------
Horizontal axis: f_star (horizontal axis).
  f_star is the stellar baryon fraction, M_star / M_baryon. Low f_star (low f_star) on the left means a gas-rich juvenile or weakly converted baryonic state. High f_star (high f_star) on the right means a stellar-rich, more mature baryonic state. Because f_gas = 1 - f_star in this visual track construction, moving right generally also means moving out of the high-gas reservoir-dominated sector.

Vertical axis: log10_Sigma_b (vertical axis).
  log10_Sigma_b is the base-10 logarithm of baryonic surface density, with Sigma_b computed dynamically at every track row as M_baryon/(2*pi*Rdisk^2) in Msun/kpc^2. Low values near the bottom are diffuse, low-surface-density systems. High values near the top are compact, high-surface-density systems. In the governor visualization, high surface density supports the Sigma gate; diffuse low-Sigma states suppress it. Upward tracker motion comes from the evolving baryonic mass and, mainly, the synthetic disk-radius compaction in the visual formation track; this is an M69 simulation-track correction, not a change to the BDVR framework formula.

Map overlays and markers:
  - Background SPARC-lite cloud: current SPARC-lite state rows colored by A_gov_current and sized partly by organization_score. These are not direct evolutionary tracks; they are the static comparison cloud.
  - M42 current transition zone: dashed/shaded threshold bands using f_star_crit, f_gas_crit, and log10_Sigma_b_crit from M42. It visualizes the current transition threshold surface; it is not direct validation.
  - UGC07125 marker: highlighted and labeled as quarantined follow-up only. It is not treated as a clean scalar object or juvenile prototype.

Current maturity tracker
------------------------
The current-maturity tracker is the bright moving marker and trailing path drawn on the SPARC-lite maturity map. It follows the selected formation track as animation time advances. The tracker uses the interpolated current state, so it moves smoothly between adjacent track rows rather than snapping from row to row.

What it is doing:
  - At the beginning of a track it starts in the juvenile low-f_star/high-gas part of the map.
  - The trailing path shows the history of the selected track through maturity space.
  - For stable-spiral outcome tracks, the tracker moves toward higher f_star and upward toward higher log10_Sigma_b as the synthetic disk compacts, crossing toward the M42 transition zone and activated mature region.
  - For failed/low-activation outcome tracks, the tracker remains closer to the low-activation juvenile or weak-transition region.
  - The tracker is visualizing the synthetic diagnostic track only; it is not claiming that an observed galaxy has been time-resolved through that exact path.

View 2: live current-governor disk simulation
---------------------------------------------
The center/right panel renders a live disk-like visual response for the currently selected track. The star/ignition points brighten and rotate as the selected state becomes more stellar-rich, organized, and governor-active. The label above the component bars names the selected formation/outcome track. The stat line reports the current interpolated state at the animation time.

Live-disk readouts:
  - t: diagnostic track time in Gyr-like display units.
  - f_star: stellar baryon fraction at the current track state.
  - f_gas: gas baryon fraction at the current track state.
  - organization score: dynamic organization proxy assembled from available M59/M58/M35/M62-style context fields; it is proxy/context, not Tier A direct dynamical validation.
  - A_gov: the current product-gate governor activation used for the live visualization and velocity inset.
  - phase label: a plain-language state label derived from f_gas, organization_score, and A_gov_current, e.g. diffuse gas/reservoir mostly off, settling disk, M42 transition zone, or mature BDVR-coupled diagnostic state.

Organization score components panel:
  This panel intentionally shows organization and gate components, not the final A_gov_current product as an organization metric. A_gov_current is not an organization metric; it is the final product-gate activation and is shown in the velocity inset and bottom timeline instead.

Metric dictionary
-----------------
Page metrics and their meanings:
  - f_star: stellar baryon fraction, M_star/M_baryon. Low f_star marks a gas-rich juvenile start; high f_star marks a stellar-rich mature state.
  - f_gas: gas baryon fraction, M_gas/M_baryon. In these visual tracks f_gas = 1 - f_star. High f_gas suppresses the current gas gate.
  - M_baryon_Msun: total baryonic mass used in the synthetic track state.
  - M_star_Msun: stellar mass for the synthetic track state.
  - M_gas_Msun: gas mass for the synthetic track state.
  - Rdisk_kpc: disk scale radius used to compute Sigma_b and the velocity diagnostic. In the synthetic visual tracks it evolves through a disk_compaction_factor.
  - disk_compaction_factor: visual-track radius multiplier relative to the initial synthetic disk radius. Stable-spiral outcome tracks compact more strongly than failed/low-activation outcome tracks.
  - Sigma_baryon_Msun_kpc2: baryonic surface density, dynamically recomputed as M_baryon/(2*pi*Rdisk^2) at every track row.
  - sigma_b_formula: audit string recording the formula used for Sigma_baryon_Msun_kpc2.
  - log10_Sigma_b: base-10 logarithm of Sigma_baryon_Msun_kpc2; this is the maturity-map vertical coordinate.
  - organization_label_score: source/context organization score contribution from available direct/proxy label context.
  - rhi_extent_organization_score: contribution from H I extent/structure context.
  - best_m58_footprint_score: contribution from the best conformal-footprint/structural score available from prior M58-style context.
  - organization_score: combined dynamic organization proxy. It is displayed in the organization score panel and used as S_settle. It is not a direct Tier A dynamical label.
  - S_settle: settling score used by the current governor calculation; in this visual diagnostic it follows organization_score.
  - A_star: stellar-fraction gate. It increases as f_star crosses the M42-style stellar maturity threshold.
  - A_Sigma: surface-density gate. It increases as log10_Sigma_b crosses the M42-style compactness threshold.
  - A_gas: high-gas suppressor gate. It is low when f_gas is high and rises as the high-gas reservoir condition turns off.
  - A_settle: organization/settling gate. It rises as S_settle/organization_score passes the settling threshold.
  - A_gov_current: final current-governor product A_star * A_Sigma * A_gas * A_settle. It is shown in the bottom timeline and velocity inset, not inside the organization score panel.
  - v_N outer: Newtonian outer velocity diagnostic for the current synthetic state.
  - v_BDVR full: full hybrid BDVR outer velocity diagnostic before current-governor suppression.
  - v_governed: current-governed outer velocity diagnostic after interpolating between v_N outer and v_BDVR full using A_gov_current.

View 3: A_gov_current timeline
------------------------------
The bottom panel plots A_gov_current along the selected formation track. The gold curve is the final current-governor activation product. The vertical white marker is the current animation time. This timeline is the correct place to read the final A_gov_current trend; the organization score panel is intentionally reserved for organization/gate components.

Page metrics
------------
The page also includes:
  - Formation label: identifies whether the selected track is a stable-spiral outcome track or failed/low-activation outcome track and names the seed object used to parameterize that track.
  - M42 transition-zone text: reports the displayed f_star/log10_Sigma_b/gas thresholds used for the shaded transition region.
  - Diagnostic-only banner: preserves the visual claim boundary on the page.
  - Keyboard controls: Space pause/resume, ArrowLeft/ArrowRight step, ArrowUp/ArrowDown change selected track, R restart, and S save PNG.

Claim-boundary interpretation
-----------------------------
The visual simulation is a diagnostic animation built from current CGHSTC-34 artifacts. It should be read as a guide to the hypothesized baryonic-organization/onset geometry, not as a proof that the governor is a mature velocity law. The M69 log10_Sigma_b motion uses the same surface-density formula as the framework; the correction here is local to the synthetic visual-track radius evolution. The M36 clean scalar branch remains the mature velocity reference; UGC07125 remains quarantined follow-up; M69 does not promote proxy labels to direct validation.

Outputs
-------
- M69_README.md
- VISUAL_SIMULATION_RUN_INSTRUCTIONS.md
- m69_current_governor_state_table.csv
- m69_current_governor_tracks.csv
- m69_random_initialization_sequence.csv
- m69_random_initialization_tracks.csv
- m69_summary.json
- m69_transition_zone_spec.json
- m69_visual_simulation.html
- m69_visual_simulation_data.json

Summary
-------
{
  "dynamic_organization_proxy_not_direct_label": true,
  "formation_track_rows": 4840,
  "governor_promoted": false,
  "initialization_mix": {
    "claim_boundary": "initialization_mix_for_visual_simulation_not_population_inference",
    "failed_low_activation_count": 12,
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
  "milestone": "CGHSTC-34-M69",
  "outcome_classification": "visual_diagnostic_current_governor_updated_from_m8",
  "proxy_rows_promoted_to_direct_validation": false,
  "random_formation_track_rows": 4840,
  "random_initialization_distribution": {
    "claim_boundary": "random_initialization_visualization_not_population_inference",
    "initial_f_star": {
      "mean": 0.17310045596646967,
      "std": 0.04810150304652121,
      "two_sigma_high": 0.2693034630595121,
      "two_sigma_low": 0.07689744887342725
    },
    "initial_log10_Sigma_b": {
      "mean": 8.546363648514756,
      "std": 0.3869951278966158,
      "two_sigma_high": 9.320353905307988,
      "two_sigma_low": 7.7723733917215245
    },
    "initial_organization_score": {
      "mean": 0.2946104740994072,
      "std": 0.09394255398773069,
      "two_sigma_high": 0.4824955830748686,
      "two_sigma_low": 0.10672536512394584
    },
    "sample_count": 40,
    "source_mode": "historic"
  },
  "state_rows": 96,
  "status": "current_governor_visual_simulation_diagnostic",
  "target": {
    "A_gov_current": 0.0008419542968684071,
    "S_settle": 0.4806866000399894,
    "galaxy_name": "UGC07125",
    "organization_score": 0.4806866000399894,
    "phase_region": "measurement_limited",
    "role": "quarantined_follow_up_not_clean_scalar_or_juvenile_prototype"
  },
  "transition_zone_source": "M42",
  "ugc07125_clean_scalar_object": false,
  "ugc07125_quarantined": true,
  "visual_style_reference": "M8 look preserved; M8 files not edited"
}
