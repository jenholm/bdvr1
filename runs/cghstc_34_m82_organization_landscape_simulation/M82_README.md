CGHSTC-34 M82: Projected A_gov landscape simulation — BDVR diagnostic visualization
===============================================================================================

Status: complete diagnostic visual branch.

BDVR Theoretical Background
---------------------------
The Bound Domain Vacuum Response (BDVR) hypothesis proposes that a sufficiently
organized bound baryonic galaxy can couple to a latent vacuum/time-current
reservoir, producing effective rotational support beyond Newtonian expectations.
The **governor** is the physical maturity gate that prevents full BDVR coupling
in juvenile, gas-rich, unorganized galaxies.

Core velocity equation (the governor interpolation):

    v_governed^2 = v_N^2 + A_gov * (v_BDVR_full^2 - v_N^2)

Limits:
  A_gov = 0  -->  v = v_N       (juvenile, reservoir off)
  A_gov = 1  -->  v = v_BDVR_full  (mature, reservoir fully on)

The full BDVR acceleration law at radius r:

    a_obs(r) = a_b(r) + Q_eff(r) * sqrt(a_b(r) * a0)

where a0 = 1.2e-10 m/s^2 is the universal acceleration scale, a_b(r) = G M_b / r^2
is the Newtonian baryonic acceleration, and Q_eff is the effective response
amplitude (Q_base * H_halo * S_star_gas * S_internal).

This visualization uses the **min-gate** approximation of the governor:

    A_gov = min(A_star, A_gas, A_sigma, A_HI)

The formal BDVR framework instead uses a product of logistic sigmoid gates.
The min-gate is a visual diagnostic proxy only.

Variables and Their BDVR Formulation
-------------------------------------

A_gov  — Governor activation factor [0, 1].
  Fraction of full BDVR reservoir support that is active.
  M82: A_gov = min(A_star, A_gas, A_sigma, A_HI). Consistently applied across
  the landscape grid, galaxy states, formation tracks, and all panels.

A_star  — Stellar fraction gate [0, 1].
  Measures stellar mass buildup. M82: clip(f_star / 0.35, 0, 1).
  Reaches 1 at f_star >= 0.35.

A_gas  — Gas depletion gate [0, 1].
  Suppresses activation in gas-rich galaxies. M82: clip(f_star, 0, 1) —
  uses f_star as proxy for gas depletion (f_gas = 1 - f_star).

A_sigma  — Baryonic surface density gate [0, 1].
  Compact baryons couple more efficiently.
  M82: clip((log10_Sigma_b - 5.5) / 3.5, 0, 1). Reaches 1 at log10_Sigma_b = 9.0.

A_HI  — H I compactness gate [0, 1].
  An extended H I envelope suppresses activation.
  M82: clip(2.0 / (0.8*RHI_Rd + 0.2), 0, 1).

limiting_gate — The weakest gate, argmin(A_star, A_gas, A_sigma, A_HI).
  Identifies the primary bottleneck. For UGC07125: A_gas.

f_star  — Stellar mass fraction [0, 1].
  f_star = M_star / M_bar. Primary x-axis of the landscape.
  Grows from ~0.04 (juvenile) to ~0.78-0.90 (mature spiral).

f_gas  — Gas mass fraction [0, 1].
  f_gas = M_gas / M_bar = 1 - f_star.

log10_Sigma_b  — Log baryonic surface density [Msun/kpc^2], range ~5.5-10.5.
  log10_Sigma_b = log10(M_bar / (2*pi*R_d^2)). Secondary y-axis of the landscape.

organization_score — Composite dynamical settlement proxy [0, 1].
  0.50 * organization_label_score + 0.30 * rhi_extent_organization_score
  + 0.20 * best_m58_footprint_score.

alpha_BTFR  — BTFR activation coefficient [typically 0-1.5].
  alpha_BTFR = sqrt(v_obs^4 / (G * M_bar * a0)). alpha_BTFR = 1 means on the BTFR.

v_N  — Newtonian baryonic speed [km/s]. sqrt(G * M_bar / r_eval).
  The lower baseline of the governor interpolation.

v_BDVR_full  — Full mature BDVR rotation speed [km/s].
  (Q_eff^2 * G * M_bar * a0)^(1/4). Upper target of the governor interpolation.

v_governed  — Governed BDVR speed [km/s].
  sqrt(v_N^2 + A_gov * (v_BDVR_full^2 - v_N^2)). Model prediction at the
  galaxy's actual maturity state.

Q_eff  — Effective BDVR response amplitude [~0.9-2.0].
  Q_base * H_halo(r) * S_star_gas * S_internal. Captures the radial envelope
  and structural corrections for stellar/gas ratio and morphology.

Governor Gate Variants
----------------------
This visualization uses the **min-gate**:

    A_star  = clip(f_star / 0.35,                    0, 1)
    A_gas   = clip(f_star,                           0, 1)
    A_sigma = clip((log10_Sigma_b - 5.5) / 3.5,      0, 1)
    A_HI    = clip(2.0 / (0.8*RHI_Rd + 0.2),         0, 1)
    A_gov   = min(A_star, A_gas, A_sigma, A_HI)

The formal BDVR framework uses the product of sigmoid gates:

    A_star  = sigmoid(f_star;           0.25, 10)
    A_Sigma = sigmoid(log10_Sigma_b;    7.8,   4)
    A_gas   = 1 - sigmoid(f_gas;        0.75,  8)
    A_HI    = 1 - sigmoid(R_HI/R_d;     7.5,   1)
    A_gov   = A_star * A_Sigma * A_gas * A_HI

The min-gate is a visual diagnostic approximation; the product-gate is the
formal hypothesis documented in the BDVR formulation papers.

Landscape Grid (Projected)
--------------------------
A 40x40 regular grid spanning f_star [0, 1] vs log10 Sigma_b [5.5, 10.5].
R_HI/R_d is estimated from f_star via RHI_Rd = clip(3.5 - 2.5*f_star, 1, 4),
making this a **projected** 2D slice, not a full 4D governor surface.
The grid is bilinearly interpolated to 400x400 for smooth rendering.

Formation Tracks
----------------
40 sequences (120 steps each) evolving juvenile→mature:
- Stable spiral (70%): f_target ~ 0.78-0.90
- Failed/low-activation (30%): f_target ~ 0.28

At each step, gate components are recomputed from evolving baryonic properties
and A_gov = min of gates. The governed velocity v_governed uses the same
min-gate A_gov, ensuring panel-to-panel consistency.

Organization Regions (Landscape Zones)
--------------------------------------
| Zone                  | A_gov range | Description                     |
|-----------------------|-------------|---------------------------------|
| dormant/pre-activation| 0.00-0.10   | Reservoir off. Diffuse systems  |
| weak response         | 0.10-0.30   | Activation beginning            |
| organization corridor | 0.30-0.50   | Transitional turn-on zone       |
| settling disk channel | 0.50-0.70   | Moderate activation, settling   |
| mature response basin | 0.70-1.00   | Full activation, settled        |

Claim Boundary
--------------
This is a visual diagnostic only. It does not promote the governor, refit M36,
promote proxy rows to Tier A, or rewrite the manuscript.

Key boundary statements:
- A_gov = min(gates) is a phenomenological visual diagnostic proxy, not the
  formal product-gate governor model.
- Gate components are illustrative, not validated direct dynamical measurements.
- The landscape is a projected 2D slice (R_HI/R_d estimated from f_star).
- Formation tracks are illustrative evolutionary paths, not N-body simulations.
- UGC07125 remains a quarantined follow-up target.

Visual Page Guide
-----------------
The browser page is a three-view diagnostic dashboard:

View 1: Projected A_gov landscape (upper-left)
-----------------------------------------------
Smooth heatmap (400x400 bilinear, 4-14% opacity) with:
- Four faint contour lines at A_gov = 0.10, 0.30, 0.50, 0.70
- Five organization region labels
- 96 SPARC-lite galaxies colored by A_gov (full opacity to pop)
- Dashed illustrative organization path
- Color legend (right side)

View 2: Visual disk proxy + governor gates (center/right)
----------------------------------------------------------
Particle disk animation responding to f_star, alpha_BTFR, and
organization_score. Four gate bars (A_star, A_gas, A_sigma, A_HI)
with limiting gate marked. Velocity inset showing v_N, v_BDVR_full,
v_governed, alpha_BTFR, and A_gov.

View 3: Organization + A_gov timeline (bottom)
-----------------------------------------------
Dual-line plot of organization_score (green) and A_gov (gold) over the
120-step formation track with four regime bands.

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
- M82_README.md
- VISUAL_SIMULATION_RUN_INSTRUCTIONS.md
- m82_random_initialization_sequence.csv
- m82_random_initialization_tracks.csv
- m82_response_organization_state_table.csv
- m82_response_organization_tracks.csv
- m82_summary.json
- m82_visual_simulation.html
- m82_visual_simulation_data.json

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
  "milestone": "CGHSTC-34-M82",
  "outcome_classification": "visual_diagnostic_landscape_updated_from_m81",
  "proxy_rows_promoted_to_direct_validation": false,
  "state_rows": 96,
  "status": "response_organization_landscape_visual_simulation_diagnostic",
  "target": {
    "A_gov": 0.18049748621310685,
    "alpha_BTFR": 0.3886403773950502,
    "c_coherence": 0.3272232599034426,
    "galaxy_name": "UGC07125",
    "limiting_gate": "A_gas",
    "phase_region": "measurement_limited",
    "role": "quarantined_follow_up_not_clean_scalar_or_juvenile_prototype"
  },
  "ugc07125_clean_scalar_object": false,
  "ugc07125_quarantained": true,
  "visual_style_reference": "M81 layout updated to response landscape; M81 files not edited"
}
