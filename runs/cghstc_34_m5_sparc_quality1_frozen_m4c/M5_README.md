# CGHSTC-34 M5: Frozen M4c SPARC Quality-1 Validation

## Status

M5 soft pass.

The frozen M4c model was evaluated on a larger SPARC quality-1 sample with no retuning, no per-galaxy Q adjustment, and no deletion of bad cases.

## Sample

- Input: `data/sparc_lite/sparc_quality1_rich_inputs.csv`
- Source: `data/sparc_lite/SPARC_Lelli2016c.mrt`
- Quality cut: Q = 1
- Required positive fields: Vflat, L36, MHI, Rdisk
- Number of galaxies: 87

## Frozen M4c Parameters

```text
q_base = 0.9002495108803148
a0_m_s2 = 1.2e-10

halo_amplitude = 0.35
halo_k = 3.0
r_eval_mode = transition
velocity_mode = flat_response
r_eval_multiple = 4.0
min_r_eval_multiple = 1.5
max_r_eval_multiple = 12.0

structural_mode = star_gas_hinge
structural_amplitude = 0.30
star_gas_threshold = 5.0

internal_mode = early_type_hinge
internal_amplitude = 0.10
early_type_threshold = 5.0