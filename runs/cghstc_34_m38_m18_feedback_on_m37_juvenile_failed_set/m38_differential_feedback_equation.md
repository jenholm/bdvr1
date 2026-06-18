# M38 differential-feedback governor equation

Status: diagnostic/onset-candidate test on the M37 juvenile/failed set; not a mature-galaxy velocity law.

M38 reuses the M18 differential-feedback structure and applies it to the M37 non-mature governor test set with the M36 hybrid halo-energy no-governor endpoint as the velocity endpoint.

```text
dA/dtau = lambda_seed D(g)(1-A) + lambda_feedback D(g) A(1-A) - lambda_reservoir R(g) A
```

`D(g)` is a bounded maturity/settling drive from stellar conversion, baryonic compactness, reduced gas/H I reservoir dominance, and resolved H I settling where available.

`R(g)` is a reservoir/unsettled suppressor from gas-richness, H I extension, low surface density, H I disturbance, and failed/stalled flags.

Mature/control rows are not part of the primary fit. They are used only to check whether the ODE incorrectly suppresses settled systems.

Selected claim: `differential_feedback_diagnostic_not_promoted`.
