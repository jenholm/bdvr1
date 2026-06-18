# M18 differential-feedback governor equation

Status: diagnostic only; this is not an accepted BDVR law.

The tested core equation is:

```text
dA/dtau = lambda_seed D(g)(1-A) + lambda_feedback D(g) A(1-A) - lambda_reservoir R(g) A
```

`D(g)` is a bounded maturity drive from stellar conversion, compact baryonic surface density,
low gas fraction, non-extended H I structure, and a stellar-dynamical accelerator. `R(g)` is a
reservoir suppressor from gas-rich and H I-extended conditions.

The feedback term `lambda_feedback D(g) A(1-A)` strengthens the response after activation begins.
The same `A(1-A)` factor tapers the growth as the galaxy approaches maturity, so the model cannot
grow without bound.

Overfitting controls used here:

- global parameters only;
- no per-galaxy tuning;
- deterministic predeclared grid;
- five-fold out-of-fold predictions;
- direct comparison against the M9 product-gate baseline.

Full-fit RMSE: 0.353
Out-of-fold RMSE: 0.363
M9 RMSE: 0.428

Pivot note: Promote M18 to a stricter validation pass with uncertainty-aware activation inference before changing the manuscript core law.
