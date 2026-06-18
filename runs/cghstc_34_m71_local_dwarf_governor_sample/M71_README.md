# M71 Local Dwarf Governor Sample

Status: local_dwarf_governor_sample_design_and_current_artifact_audit

Claim boundary: sample_design_and_settling_state_audit_not_model_validation

Run from project root:

```bash
./venv/bin/python src/run_cghstc34_m71_local_dwarf_governor_sample.py
```

This branch implements the selection-paradox response: Branch A keeps clean rotational-response rows; Branch B records settling-state targets without fabricating `Vflat`, `Vrot/sigma`, asymmetry, warp, offset, or lopsidedness values.

Key outputs:

- `m71_branch_a_rotational_response_sample.csv`
- `m71_branch_b_settling_state_targets.csv`
- `m71_external_survey_target_registry.csv`
- `m71_correlation_fit_audit.csv`
- `m71_recommended_model_formulation.md`
