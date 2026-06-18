# M20 equation specification

Status: diagnostic only; not an accepted BDVR-law replacement.

## Censored latent activation

M20 treats the clipped target as a censored latent activation:

```text
z_i = eta(g_i, J_i) + epsilon_i
A_inferred = 0   if z_i <= 0
A_inferred = z_i if 0 < z_i < 1
A_inferred = 1   if z_i >= 1
```

The implemented diagnostic uses ridge-regularized global linear state scores on a latent endpoint-expanded target as a computational approximation to the censored likelihood. Predictions are evaluated both as unbounded latent rank scores and as bounded `clip(eta, 0, 1)` responses.

## Pairwise rank loss

The rank-augmented branch uses a pairwise rank penalty during deterministic grid selection:

```text
L_rank = mean log(1 + exp[-sign(A_i-A_k)(eta_i-eta_k)])
```

## Angular momentum

The retained artifact-backed proxy is:

```text
J_lambda = log10[(2 * Rdisk_kpc * Vflat) / sqrt(M_baryon_Msun * Rdisk_kpc)]
```

Direct observed stellar/gas/baryonic angular momentum is not available in the current local artifacts. `J_lambda` is therefore a proxy state variable, not an observed `j_*`, `j_gas`, or halo spin measurement.

## Rho target

`rho > 0.60` is a target, not a show-stopper. If the diagnostic improves the science but misses rho > 0.60, the result is recorded and the next pivot remains available.

## Velocity-domain pivot

If censored/rank activation still plateaus, the next plan is a velocity-domain latent BDVR likelihood:

```text
log Vflat ~ Normal(log V_BDVR(A_latent, g, J), sigma_logV)
```
