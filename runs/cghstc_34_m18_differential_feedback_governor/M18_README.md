# CGHSTC-34 M18 differential-feedback governor diagnostic

This run tests a bounded differential activation law with a feedback loop and maturity taper.
It is a diagnostic branch, not an accepted BDVR model term.

Status: diagnostic_differential_feedback_governor_not_accepted_model

Key results:

- M9 baseline RMSE: 0.428
- M18 full-fit RMSE: 0.353
- M18 out-of-fold RMSE: 0.363
- M9 baseline Spearman rho: 0.146
- M18 full-fit Spearman rho: 0.234
- M18 out-of-fold Spearman rho: 0.164

Interpretation:

The differential-feedback equation improves both error and rank ordering under cross-validation, so it is a candidate for a stronger diagnostic branch.

Pivot recommendation:

Promote M18 to a stricter validation pass with uncertainty-aware activation inference before changing the manuscript core law.
