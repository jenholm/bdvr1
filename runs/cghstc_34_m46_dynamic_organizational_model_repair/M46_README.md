# CGHSTC-34 M46 Dynamic Organizational Model Repair

Status: dynamic_organizational_model_repair_diagnostic

Outcome: quality_contamination_dominant
Failure layer: quality_contamination

M46 first trains a baryon-only dynamic organization coordinate from independent organization/settling labels. It then freezes that coordinate before joining M36/M44 endpoint residual and activation targets for held-out Tier 1 rows.

This branch does not train a scalar maturity score directly on endpoint residuals, does not use quality as a physical organization feature, does not refit M36, and does not rewrite the manuscript.

Key held-out dynamic model metrics:

- heldout_n: 29
- activation_balanced_accuracy: 0.308
- residual_direction_balanced_accuracy: 0.382
- activation_auc_like: 0.385
- residual_auc_like: 0.311

Artifacts are the CSV/JSON files in this run directory.
