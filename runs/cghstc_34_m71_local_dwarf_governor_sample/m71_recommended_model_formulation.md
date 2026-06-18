# M71 Recommended Model Formulation

## Selection paradox

The quality-1 / clean-rotation cut is not neutral for the governor question. It preferentially selects galaxies whose H I velocity fields are already orderly enough for conventional circular-speed modeling. That makes the current SPARC-like sample strong for the mature rotational branch and weak for the low-organization population.

## Branch A: clean rotational-response test

Use only systems classified `R`, where rotation is a defensible tracer of circular velocity. In this branch, `A_inferred` and corrected/rank activation diagnostics may be compared against `f_star`, `f_gas`, `log10_Sigma_b`, `R_HI/R_d`, angular-momentum context, and quality flags.

Pearson is secondary here because `A_inferred` is bounded and clipped; Spearman and Kendall are preferred for monotonic ordering and ties, with Pearson retained only as an audit statistic.

## Branch B: settling-state test

Use `T`, `D`, and `X` rows plus external local-dwarf acquisition targets. Do not force Vflat or circular-speed activation onto these rows. The test is whether low predicted activation and low baryonic organization predict low `Vrot/sigma`, H I asymmetry, centroid offsets, A/R mismatch, PA twists/warps, lopsidedness, and dispersion support once source-level same-object measurements are acquired.

## Observation classes

- `R`: rotation dominated and usable for rotational-response / `A_inferred` analysis.
- `T`: transition or rotation-dispersion comparable; settling-state target.
- `D`: dispersion dominated or circular speed unresolved; pressure/settling endpoint target.
- `X`: severe geometry/quarantine/interacting/measurement-limited; audit/follow-up only.
- `needs_source_measurement`: survey target or identity route without source-level settling measurement.

## Claim boundary

M71 is a sample-design and current-artifact audit. It does not promote the governor, does not change the mature velocity law, does not refit M36, and does not promote proxy/context rows to Tier A direct validation.
