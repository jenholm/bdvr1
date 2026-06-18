# M70 equation specification

Status: diagnostic reformulation only; not an accepted governor law and not independent validation.

M70 uses the corrected A_inferred target generated after the dimensional repair of the full-velocity normalization. The branch responds to the reduced M9 product-gate Spearman correlation by replacing the strict product gate with a latent activation coordinate:

```text
z_i = beta_0 + beta · x_i
A_rank_m70 = z_i
A_bounded_m70 = clip(z_i, 0, 1)
```

Endpoint clipping is handled as censored target construction:

```text
A_latent = A_inferred             for 0 < A_inferred < 1
A_latent = -delta                 for A_inferred = 0
A_latent = 1 + delta              for A_inferred = 1
```

The feature vector uses prior-branch lessons: M20-style maturity/reservoir/angular-momentum proxy coordinates, optional M59 composition/H I backbone context, and interactions. The angular-momentum term is a proxy (`J_lambda_z`), not direct observed j_star, j_gas, j_bar, or halo spin.

Because the model is selected against corrected A_inferred, a higher Spearman is a successful reparameterization diagnostic, not independent direct validation. Do not promote proxy/context rows to Tier A and do not rewrite the manuscript from this result alone.
