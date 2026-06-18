# M40 Onset Label Acquisition and Quality-Stratified Governor Audit

Status: `onset_label_acquisition_quality_stratified_audit`

This run separates direct SPARC-like rows into clean juvenile/failed candidates,
measurement-contaminated candidates, and mature controls before interpreting the
negative rank signal. It asks whether the negative rank signal is physical,
observational, or both. It also carries external proxy rows separately.

Interpretation of the negative rank signal: `observational_quality_axis`.

This is a diagnostic label-acquisition audit. It does not change the mature velocity
law, does not rewrite the manuscript, and does not promote a new governor law.

Required boring outputs:

- `m40_quality_labels.csv`
- `m40_onset_candidate_labels.csv`
- `m40_resolved_HI_crossmatch_needs.csv`
- `m40_priority_followup_table.csv`
- `m40_stratified_m38_m39_metrics.csv`

External proxy rows are follow-up priorities only unless direct activation endpoints
and resolved quality labels are acquired.
