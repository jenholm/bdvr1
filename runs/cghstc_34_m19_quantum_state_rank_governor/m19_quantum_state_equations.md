# M19 quantum-state rank-governor equations

Status: diagnostic only. This is not literal galaxy-scale quantum mechanics and is not an accepted BDVR law.

## Bloch/Lindblad candidate

```text
du/dtau = -Delta(g) v - gamma_phi u
dv/dtau =  Delta(g) u - gamma_phi v + Omega(g) w
dw/dtau = -Omega(g) v - gamma_relax [w - w_eq(g)]
A_pred = (1 + w_final) / 2
```

This candidate treats activation as a two-state channel with coherence variables `u`, `v` and population coordinate `w`.

## two-channel master equation candidate

```text
dA/dtau = k_on(g) (1-A) - k_off(g) A + k_coh(g) sqrt(A(1-A)) (1-A)
```

This was the selected M19 family. `k_on(g)` is the state drive, `k_off(g)` is reservoir detuning/loss, and `k_coh(g)` is a coherence-like transfer term.

## Rank-ordering selection

The rank-ordering repair is explicit: the deterministic grid uses:

```text
rank_score = MSE - 0.55 * Spearman(A_pred, A_inferred) + saturation_penalty
```

Full-fit Spearman: 0.323
Out-of-fold Spearman: 0.199

Pivot note: Use M19 as the next latent activation candidate, then test it in a censored/uncertainty-weighted activation likelihood and velocity-domain likelihood before manuscript promotion.
