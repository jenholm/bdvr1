# CGHSTC-34 / BDVR Response-Organization Formulation

**Project:** CGHSTC-34  
**Framework:** Bound Domain Vacuum Response (BDVR)  
**Status:** Falsifiable galaxy-evolution hypothesis; preliminary scalar-proxy diagnostics completed  
**Claim boundary:** Phenomenological galaxy-sector formulation; not a complete action-level derivation; not a manuscript claim of proof

---

## 0. Executive Thesis

The Bound Domain Vacuum Response (BDVR) framework proposes that a sufficiently organized baryonic disk galaxy can couple to a latent vacuum/time-current reservoir. That coupling appears as extra effective rotational support. The response does not turn on simply because baryons exist. It turns on when baryons have become organized enough to form a stable, long-lived disk.

The governor is the physical maturity gate:

```
juvenile gas-rich formation state
  -> weak or suppressed BDVR coupling
  -> baryons remain available for star formation and structural assembly

mature organized spiral disk
  -> strong BDVR coupling
  -> enhanced rotational support, disk survival, and regulated star formation
```

In one sentence:

> BDVR is a bound-domain response law, and the governor is the condition that prevents the response from turning on before the galaxy has earned the dynamical right to use it.

**Plain English:** A baby galaxy should not be handed the full stabilizing flywheel before it has built the disk that flywheel is supposed to preserve.

---

## 1. The Empirical Problem

### 1.1 Observed rotation exceeds baryonic prediction

For a test mass in circular orbit, Newtonian balance gives:

```
v^2 / r = G M(r) / r^2
```

where `v` is orbital speed, `G` is the gravitational constant, and `M(r)` is the mass enclosed within radius `r`. If only visible baryonic mass contributes:

```
v_baryon^2(r) = G M_b(r) / r
```

At large radius, where most baryonic mass is enclosed, this curve should fall. But observed disk galaxies show:

```
v_obs(r) approximately constant
```

across large radial ranges.

**Plain English:** The outer gas and stars in many spiral galaxies move faster than visible baryons alone would naively support. Something is organizing the outer disk as if there is additional rotational support.

### 1.2 The baryonic Tully-Fisher clue

Across many galaxies, the fourth power of the flat rotation speed tracks the baryonic mass:

```
v_flat^4 ∝ G M_b a0
```

or equivalently:

```
v_flat = (G M_b a0)^(1/4)
```

where `a0 ≈ 1.2 × 10^(-10) m/s^2` is a characteristic acceleration scale.

**Plain English:** That the flat rotation speed knows about baryonic mass is a clue that the response is not arbitrary. It is organized. It knows about baryons.

BDVR keeps this clue. The BTFR is the backbone clue: baryonic mass sets the basic scale.

### 1.3 The additional BDVR proposition

What BDVR adds is the hypothesis that BTFR scatter is not purely measurement noise. Part of it may reflect whether the galaxy has organized itself enough to express the full dynamical response as coherent rotation.

> At fixed baryonic mass, a dynamically settled disk may occupy a tighter, more reproducible BTFR channel than an unsettled gas-rich system.

---

## 2. Core BDVR Response Law

### 2.1 Baryonic acceleration

For a galaxy, the baryonic acceleration at radius `r` is:

```
a_b(r) = G M_b(r) / r^2
```

**Plain English:** The ordinary gravitational pull from stars and gas.

### 2.2 BDVR response acceleration

The BDVR response acceleration is:

```
a_BDVR(r) = Q_eff(r, g) sqrt[a_b(r) a0]
```

where:
- `a0 = 1.2 × 10^(-10) m/s^2` (the same acceleration scale that appears in the BTFR)
- `g` denotes galaxy-level structural properties
- `Q_eff(r, g)` is a nonnegative dimensionless response factor

The total effective radial acceleration is:

```
a_obs(r) = a_b(r) + a_BDVR(r)
```

**Plain English:** The galaxy has its ordinary baryonic pull, plus a reservoir-mediated response whose scale is the geometric mean of the baryonic acceleration and the universal galaxy acceleration scale. The response term is not an arbitrary fitted component per galaxy; it is tied to baryonic structure.

### 2.3 Flat-velocity scaling

The square-root form leads to a flat-velocity scaling. In the outer regime where most mass is enclosed and `Q_eff` has converged to an outer constant:

```
v_flat^4 = Q_eff^2 G M_bar a0
```

so:

```
v_flat = (Q_eff^2 G M_bar a0)^(1/4)
```

**Plain English:** The model naturally connects baryonic mass to flat rotation speed, but the coefficient is controlled by the galaxy's response state. Variation in `Q_eff` contributes BTFR scatter:

```
Δ log v_flat = (1/2) Δ log Q_eff
```

---

## 3. The Governor Layer

The governor is the central physical concept. It prevents full BDVR response from activating before the galaxy is organized enough to benefit from it.

### 3.1 Physical motivation

A juvenile galaxy needs its gas to build stars and assemble a disk:

```
gas accumulation -> star formation -> disk settling -> mature organization
```

If full BDVR response activates too early, it can over-stabilize the gas:

```
A_gov too high too early
  -> excessive rotational support
  -> gas stays too spread out
  -> inefficient structural assembly
  -> delayed or suppressed maturation
```

A mature spiral needs the opposite:

```
preserve disk -> regulate collapse -> sustain star formation -> survive perturbations
```

**Plain English:** A young galaxy has to become a galaxy. A mature spiral has to remain a galaxy. The governor exists because the optimal response changes across this sequence.

### 3.2 Governor equation

Introduce the activation factor `A_gov`, bounded between 0 and 1:

```
v_BDVR,gov^2 = v_N^2 + A_gov (v_full^2 - v_N^2)
```

where:
- `v_N` is the Newtonian baryonic circular speed
- `v_full` is the full mature BDVR prediction (Q_eff fully active)
- `A_gov` controls how much reservoir support is active

Limits:

```
A_gov = 0 -> v_BDVR,gov = v_N        (juvenile / reservoir off)
A_gov = 1 -> v_BDVR,gov = v_full     (mature / reservoir fully on)
```

**Plain English:** The governor is a dimmer switch between baryons-only rotation and full mature BDVR support.

### 3.3 Implied activation from observed galaxies

Given an observed flat velocity `v_obs`, we can ask what activation each galaxy appears to need:

```
A_implied = (v_obs^2 - v_N^2) / (v_full^2 - v_N^2)
```

then clip to physical bounds:

```
A_implied = clip(A_implied, 0, 1)
```

**Plain English:** Ask each galaxy: how much of the full BDVR support do you appear to be using?

Interpretation:

| A_implied | Meaning |
|-----------|---------|
| Near 0 | Reservoir mostly off; galaxy rotates like baryons alone |
| ~0.5 | Transitional; partial activation |
| Near 1 | Full mature reservoir response active |

### 3.4 Product-gate governor

The governor should not be a free per-galaxy knob. It is predicted from observable maturity variables:

```
A_gov = A_star × A_Sigma × A_gas × A_HI
```

Each gate is a logistic function bounded between 0 and 1, producing a smooth switch rather than a hard threshold.

---

## 4. Maturity Variables and Gates

### 4.1 Stellar fraction gate

```
f_star = M_star / M_bar
A_star = 1 / [1 + exp(-k_star (f_star - f_star,crit))]
```

Threshold: `f_star,crit = 0.25`, slope `k_star = 10`

**Plain English:** The more baryons have been converted into stars, the more the galaxy has built a stable stellar disk that can couple to the reservoir.

### 4.2 Baryonic surface-density gate

```
Sigma_b = M_bar / (2π R_d^2)
A_Sigma = 1 / [1 + exp(-k_Sigma (log10 Sigma_b - log10 Sigma_b,crit))]
```

Threshold: `log10 Sigma_b,crit = 7.8`, slope `k_Sigma = 4`

**Plain English:** A galaxy can have a lot of baryons, but if those baryons are too spread out, the domain may not be compact enough to activate strong coupling.

### 4.3 Gas suppression gate

```
f_gas = M_gas / M_bar
A_gas = 1 / [1 + exp(k_gas (f_gas - f_gas,crit))]
```

Threshold: `f_gas,crit = 0.75`, slope `k_gas = 8`

**Plain English:** If the galaxy is still overwhelmingly gas, the reservoir stays suppressed. Gas-rich infancy should not look like mature disk coupling.

### 4.4 H I extent gate

```
R_HI/R_d = H I radius / disk scale length
A_HI = 1 / [1 + exp(k_HI (R_HI/R_d - (R_HI/R_d),crit))]
```

Threshold: `(R_HI/R_d),crit = 7.5`, slope `k_HI = 1.0`

**Plain English:** A highly extended H I envelope suggests the galaxy has not yet settled into a compact organized disk. The reservoir gate remains partially shut.

### 4.5 Combined product gate

```
A_gov = A_star × A_Sigma × A_gas × A_HI
```

**Plain English:** The reservoir turns on only when multiple conditions are satisfied simultaneously. A galaxy needs enough stars, enough compactness, not too much diffuse gas dominance, and not too extended H I.

---

## 5. Current Numerical Diagnostics

### 5.1 SPARC sample

The SPARC quality-1 diagnostic sample contains 87 galaxies with available baryonic mass variables, flat velocities, and all four maturity coordinates.

### 5.2 Governor product-gate results

| Metric | Value |
|--------|-------|
| Sample size | 87 |
| Model variant | product_star_sigma_gas_hi |
| MSE | 0.183 |
| Spearman ρ (A_pred vs A_inferred) | 0.146 |
| Juvenile median A_pred | 0.042 |
| Transition median A_pred | 0.349 |
| Mature median A_pred | 0.555 |

**Plain English:** The model orders galaxies from low to high predicted activation, but with substantial scatter. The ordering is modest: juvenile galaxies receive low predicted activation, mature galaxies higher predicted activation, but individual predictions are not precise.

### 5.3 Clipping audit

A_inferred has a severe endpoint-clipping problem:

| A_inferred value | Count |
|------------------|-------|
| Exactly 0 | 12 galaxies |
| Between 0 and 1 | 69 galaxies |
| Exactly 1 | 6 galaxies |

Thus 18 of 87 galaxies are boundary-coded. The unclipped activation proxy spans -0.19 to 1.57.

**Plain English:** Because of how A_inferred is defined, many galaxies hit the floor or ceiling. The target is not a clean continuous variable for regression. This limits the strength of any correlation measurement.

### 5.4 Spearman correlations with A_inferred

| Variable | Spearman ρ |
|----------|------------|
| f_star | -0.014 |
| f_gas | 0.014 |
| log10 Sigma_b | -0.364 |
| T (morphology) | 0.082 |
| R_HI / R_d | -0.500 |

**Plain English:** H I extent and surface density show the strongest individual correlations with inferred activation. Stellar fraction and gas fraction alone carry almost no rank information. The product gate's value comes from combining multiple weak signals.

### 5.5 Baseline comparisons

| Model | MSE | Spearman ρ |
|-------|-----|------------|
| Constant mean baseline | 0.104 | — |
| Stellar fraction alone | 0.255 | -0.018 |
| Gas fraction alone | 0.255 | -0.018 |
| Surface density alone | 0.291 | -0.366 |
| H I extent alone | 0.157 | 0.497 |
| Selected product gate | 0.183 | 0.146 |
| Simple linear regression | 0.084 | 0.490 |

**Plain English:** The selected product gate has higher MSE than the constant-mean baseline, meaning the continuous regression is not successful. H I extent alone does nearly as well as the full product gate. The four-gate model is a target-selection hypothesis, not a demonstrated new scaling law.

---

## 6. Classification by Maturity Class

| Maturity class | N | Median A_pred | Meaning |
|---------------|---|---------------|---------|
| Juvenile | 12 | 0.042 | Strongly suppressed predicted activation |
| Transition | 39 | 0.349 | Intermediate predicted activation |
| Mature | 36 | 0.555 | Substantial predicted activation |

**Plain English:** The model assigns low predicted activation to gas-rich, extended juvenile systems and higher predicted activation to compact, stellar-rich mature disks. The transition systems sit in the middle of the activation switch.

---

## 7. Latent Angular-Momentum Formulation (M20)

### 7.1 The problem that led here

The earlier governor diagnostics treated A_inferred as a continuous target. However, 18 of 87 galaxies, or about 21%, lie exactly at the clipping boundaries (0 or 1). In addition, the unclipped proxy spans beyond the physical interval, from –0.19 to 1.57. Treating the clipped value as an ordinary continuous response therefore loses information about censored objects near the floor and ceiling.

### 7.2 Latent/censored formulation

Treat A_inferred as a censored observation of a latent activation coordinate:

```
z_i = η_i + ε_i

A_inferred_i = 0      if z_i ≤ 0
A_inferred_i = z_i    if 0 < z_i < 1
A_inferred_i = 1      if z_i ≥ 1
```

**Plain English:** Instead of treating A_inferred = 0 as the true activation, we treat it as "activation is at or below zero." Galaxies at the boundary are not all the same; the model can assign them different latent values below the floor or above the ceiling.

### 7.3 Angular-momentum proxy

The retained angular-momentum proxy is a normalized compactness coordinate:

```
j_obs_proxy = 2 R_d v_flat
J_lambda = log10[j_obs_proxy / sqrt(M_bar R_d)]
```

This is a normalized angular-momentum/compactness state coordinate, not a direct observed spin parameter.

**Plain English:** The angular-momentum proxy captures how rotationally supported and compact the galaxy is. It is not measured from resolved kinematics; it is constructed from catalog quantities.

### 7.4 M20 results

| Metric | No angular momentum | With angular momentum |
|--------|-------------------|---------------------|
| Out-of-fold Spearman ρ | 0.256 | 0.757 |
| Out-of-fold bounded RMSE | 0.351 | 0.175 |

The gain from adding J_lambda is approximately 0.50 in Spearman ρ and -0.176 in bounded RMSE.

**Plain English:** Including the angular-momentum proxy dramatically improves the ordering of galaxies by inferred activation. This was the dominant improvement over earlier models.

### 7.5 Cautious interpretation

The M20 result is a diagnostic candidate, not a proven BDVR activation law. The angular-momentum variable is a proxy constructed from the same catalog quantities that enter the target. Cross-validation rank separation is encouraging but does not constitute independent physical validation.

---

## 8. Corrected Activation Rank Reparameterization (M70)

### 8.1 Purpose

M70 asks whether the corrected scalar target (after dimensional repair of the full-velocity normalization) can be ordered by a supervised latent coordinate.

### 8.2 Results

| Metric | Full fit | 5-fold out-of-fold |
|--------|----------|-------------------|
| Rank Spearman ρ | 0.981 | 0.968 |
| Bounded RMSE | 0.061 | 0.081 |

**Plain English:** Once endpoint clipping is treated as censoring, the corrected activation target contains substantial orderable structure. The latent coordinate can rank galaxies almost perfectly.

### 8.3 Claim boundary

M70 is diagnostic reparameterization only. The improvement over the product gate (ρ = 0.146 → 0.968) does not validate the governor hypothesis. It shows that the endpoint target has orderable structure when clipping is properly handled.

---

## 9. Scalar Proxy Cross-Survey Analysis (arXiv Pivot)

### 9.1 Design

The arXiv analysis shifts from the governor product gate to a broader question: can unresolved scalar proxies (combining inclination, H I linewidth, gas fraction) predict BTFR scatter reduction?

Three distinct coherence quantities:

1. **C_proxy** (empirical unresolved proxy) — the numerical score constructed from linewidth, inclination, and gas fraction
2. **C_dyn** (direct dynamical organization) — a future resolved-H I quantity
3. **C_BDVR** (latent theoretical coordinate) — the 0-to-1 degree to which BDVR response is expressed through regular rotation

These are not equivalent: `C_proxy ≠ C_dyn ≠ C_BDVR`.

### 9.2 SPARC results

In SPARC, galaxies in the highest scalar-coherence quartile (Q4) show 35% lower absolute BTFR residual scatter than the lowest quartile (Q1):

```
σ_Q1 = 0.0753 dex
σ_Q4 = 0.049 dex
Q4/Q1 = 0.65
```

**Plain English:** The highest-ranked SPARC galaxies by the scalar proxy have noticeably less BTFR scatter than the lowest-ranked ones. But the intermediate quartiles are not uniformly monotonic, and the sample is small (N=87).

### 9.3 xGASS results

In xGASS (N=363 clean H I profiles), the scatter reduction is larger:

```
Full sample: Q4/Q1 = 0.38 (Spearman ρ = -0.238)
Cross-validated: Q4/Q1 = 0.365 (95% CI: [0.231, 0.572], ρ = -0.285)
```

**Plain English:** In xGASS, the highest-coherence quartile has 62% lower scatter than the lowest. The effect survives cross-validation.

### 9.4 Confounder audit results

This is the critical finding. When the proxy is dissected:

| Proxy variant | Spearman ρ | Q4/Q1 |
|---------------|-----------|-------|
| Full proxy (i + W50 + gas) | -0.213 | 0.411 |
| Inclination only | -0.352 | 0.459 |
| W50 only | -0.237 | 0.481 |
| Gas fraction only | +0.225 | 1.54 |
| Inclination + W50 only | — | strongest |

**Plain English:** The apparent scatter reduction is primarily driven by inclination and linewidth — the same quantities that make the BTFR velocity easier to measure reliably. Gas fraction alone even shows the opposite sign. This is consistent with measurement recoverability, not necessarily physical coherence.

### 9.5 Measurement-quality control

When the full proxy is added to a model already containing basic quality variables (baryonic mass, inclination, axis ratio, confusion flag):

```
Null model R² = 0.147
Full model R² = 0.151
ΔR² ≈ 0.0035
```

**Plain English:** The scalar coherence proxy adds essentially no predictive information beyond what standard observables already provide. This is the most important null result of the entire analysis. The proxy does not capture physically independent information.

### 9.6 Inclination-restricted analysis

In the mid-inclination range (removing edge-on and face-on galaxies):

```
45° < i < 75°: Q4/Q1 = 0.561 (CI: [0.331, 0.887])
50° < i < 80°: Q4/Q1 = 0.525 (CI: [0.333, 0.871])
```

**Plain English:** The scatter reduction persists after restricting inclination, but is substantially weaker than the full-sample result. Orientation contributes materially to the observed effect.

---

## 10. The Quarantine Principle: UGC07125

UGC07125 is excluded from clean scalar model tests after published geometry audit. Its H I and stellar structure are side-dependent: the W side is warped while the E side is not warped.

| Parameter | Value |
|-----------|-------|
| A_inferred | 0.000 |
| A_pred | 0.057 |
| f_star | 0.180 |
| f_gas | 0.820 |
| R_HI / R_d | 6.82 |
| α_BTFR | 0.389 |
| Status | Excluded from clean scalar test: side-dependent H I/stellar geometry |

**Plain English:** UGC07125 looks like a low-activation galaxy in its scalar coordinates, but its geometry is asymmetric. The gas on one side is not participating in organized rotation the same way as on the other side. It is kept as a quarantined follow-up target, not as a clean juvenile prototype.

The cleaner juvenile-forming contrast is DDO161 (A_inferred = 0.000, A_pred = 0.013, f_star = 0.130, R_HI/R_d = 8.76).

---

## 11. External Proxy Channels

External surveys provide proxy consistency checks and candidate-selection channels, not direct BDVR validation.

| Dataset | Context | Limitation |
|---------|---------|------------|
| THINGS | Resolved H I maps; N=8 overlap | Too small for a statistically meaningful test |
| MaNGA | IFU stellar/gas proxies | No outer H I rotation |
| ATLAS3D | Fast/slow rotator endpoint controls | Early-type systems, not disk-galaxy activation tests |
| xGASS/xCOLD GASS | Gas fraction and depletion tracking | Gas-fraction correlations partly definitional |

Total: 11,275 usable proxy measurements across stages, but none provide the decisive same-object resolved H I and kinematic measurements.

**Plain English:** These surveys provide context and help define targets, but none of them measure what the governor hypothesis actually predicts — resolved velocity-field symmetry, approaching/receding rotation curve match, and H I settling state.

---

## 12. Falsifiable Predictions

### 12.1 Threshold predictions (retrospective on SPARC)

1. **Mature systems:** Among galaxies with f_star > 0.3, log Σ_b > 8.0, f_gas < 0.5, and R_HI/R_d < 5.0, less than 5% should have A_inferred < 0.2.

2. **Juvenile systems:** Among galaxies with f_star < 0.2 and R_HI/R_d > 6.0, less than 10% should have A_inferred > 0.6.

**Plain English:** These define the expected activation zones. If mature-looking galaxies routinely have low inferred activation, or if juvenile-looking galaxies routinely have high inferred activation, the governor hypothesis fails.

### 12.2 Resolved H I predictions

3. **H I asymmetry:** In a sample of 20 low-A_pred galaxies and 20 matched high-A_pred controls, the median H I asymmetry should be at least 0.1 higher in the low-activation sample, with Mann-Whitney p < 0.05.

4. **High-redshift gas-rich disks:** In a mass-matched sample at z > 1, the median α_BTFR < 0.8 for galaxies with f_gas > 0.7.

**Plain English:** The decisive test requires actually looking at the H I structure. Low-activation candidates should look dynamically messy. High-activation controls should look settled.

### 12.3 Response-organization predictions

5. **Proxy validation:** Scalar high-coherence galaxies should show more regular resolved H I velocity fields than matched low-coherence galaxies.

6. **Resolved curves strengthen the pattern:** The Spearman correlation between coherence and BTFR scatter should increase when global linewidths are replaced by resolved rotation curves.

**Plain English:** If the scalar proxy means anything physically, it should predict the results of a resolved kinematic observation.

### 12.4 Failure criteria

The response-organization hypothesis fails if:

1. The scatter effect disappears after inclination and linewidth-quality matching
2. The scalar score does not predict resolved H I coherence
3. Resolved coherence adds no held-out information beyond ordinary quality flags
4. Low- and high-coherence galaxies have indistinguishable BTFR residual variance after measurement-error correction
5. The result depends on using the same velocity quantity in both predictor and target
6. Leave-one-survey-out validation fails

---

## 13. What Is Solid and What Remains Unproven

### Solid

- The galaxy-rotation problem is real: outer disk rotation exceeds baryonic prediction
- The BTFR is real: baryonic mass and flat rotation speed are tightly correlated
- BDVR provides a compact baryonic-response law with a clear acceleration scale
- The product-gate governor can weakly order galaxies by inferred activation
- The latent angular-momentum formulation shows that the endpoint target contains orderable structure
- Cross-survey scalar proxies show directional consistency (higher proxy → lower scatter)
- The confounder audits rigorously demonstrate that the scalar proxy cannot distinguish BDVR from measurement-quality effects
- UGC07125 is properly quarantined; DDO161 is the cleaner juvenile contrast
- The external proxy channels (THINGS, MaNGA, ATLAS3D, xGASS) provide context but are not decisive tests

### Remains unproven

- Whether A_gov is actually controlled by f_star, f_gas, Σ_b, and direct settling metrics
- Whether enough same-object resolved H I / velocity-field measurements support the predicted transition
- Whether a full action-level CGHSTC derivation can produce the BDVR effective law and governor gates
- Whether the scalar proxy association is physical or purely instrumental
- Whether the governor hypothesis survives when tested with resolved kinematics

---

## 14. The Decisive Observational Program

### Required measurements per target

1. Observed v_flat and uncertainty
2. Newtonian baryonic speed v_N
3. Full mature BDVR speed v_full
4. Inferred activation A_implied
5. f_star, f_gas, Σ_b
6. H I asymmetry index
7. Approaching/receding rotation-curve mismatch
8. Warp / position-angle twist
9. H I / stellar centroid offset
10. V_rot / σ (rotational support fraction)
11. Depletion time or star-formation efficiency
12. Interaction/morphology notes

### Target numbers

- ~20 low-A_pred galaxies (gas-rich, extended, low predicted activation)
- ~20 mass-matched high-A_pred controls (compact, stellar-rich, high predicted activation)
- Resolved H I maps for all 40

### Decisive test

```
A_implied = F(f_star, f_gas, Σ_b, H I organization, kinematic settling)
```

The hypothesis is confirmed if the activation boundary is physically organized and reproducible. It is falsified if direct measurements show no such boundary.

**Plain English:** Two samples of 20 galaxies each, matched in mass but different in predicted activation. If the low-activation sample is systematically more asymmetric, warped, and dynamically unsettled, the governor hypothesis gains support. If they look the same, the hypothesis fails.

---

## 15. Complete Compact Formulation

### Base BDVR law

```
M_bar = M_star + M_gas
a_b(r) = G M_bar / r^2       (enclosed approximation)
a_BDVR(r) = Q_eff sqrt[a_b(r) a0]
a_obs(r) = a_b(r) + a_BDVR(r)
```

### Outer flat-velocity limit

```
v_flat^4 = Q_eff^2 G M_bar a0
Δ log v_flat = (1/2) Δ log Q_eff
```

### Governor activation

```
v_gov^2 = v_N^2 + A_gov (v_full^2 - v_N^2)
```

### Maturity gates

```
A_star  = σ(f_star;  f_star,crit=0.25,  k=10)
A_Sigma = σ(log Σ_b; log Σ_b,crit=7.8,   k=4)
A_gas   = 1 - σ(f_gas; f_gas,crit=0.75,   k=8)
A_HI    = 1 - σ(R_HI/R_d; (R_HI/R_d),crit=7.5, k=1.0)

A_gov = A_star × A_Sigma × A_gas × A_HI
```

where `σ(x; x_c, k) = 1 / [1 + exp(-k(x - x_c))]`.

### Inferred activation from data

```
A_implied = clip[(v_obs^2 - v_N^2) / (v_full^2 - v_N^2), 0, 1]
```

### Latent formulation (M20)

```
z_i = β · x_i + ε_i
A_inferred_i = 0      if z_i ≤ 0
A_inferred_i = z_i    if 0 < z_i < 1
A_inferred_i = 1      if z_i ≥ 1
```

### Response-organization scatter prediction

```
Var[Δ_BTFR | C_BDVR] = σ_floor² + σ_unsettled² exp(-γ C_BDVR)
```

---

## 16. One-Page Layman's Explanation

A spiral galaxy is like a giant rotating disk of gas and stars. If it rotates too slowly, material falls inward too fast, gas piles up, and the galaxy burns through its star-forming fuel too violently. If it has enough rotational support, it can stay wide, graceful, organized, and alive with star formation for billions of years.

BDVR proposes that once a galaxy becomes a sufficiently organized bound structure, it couples to a hidden reservoir of effective rotational support. That reservoir does not replace the galaxy's baryons — it responds to them. The baryons are the source. The reservoir is the stabilizing response.

But the response cannot turn on for every gas cloud. A juvenile galaxy needs its gas to build stars and organize itself. If full support turns on too early, it keeps the gas too spread out and prevents normal maturation. That is why the governor is necessary.

The governor asks four questions:
1. Have enough baryons been converted into stars? (stellar fraction gate)
2. Are the baryons concentrated enough? (surface density gate)
3. Is the galaxy still overwhelmingly gas? (gas suppression gate)
4. Is the H I disk compact relative to the stellar disk? (H I extent gate)

Only when all four conditions are satisfied does the reservoir fully activate.

The current scalar diagnostics provide modest support for this ordering. Galaxies that pass all four gates show higher inferred activation. Those that fail sit in a lower-response channel. But the scalar data cannot distinguish this from measurement-quality effects — galaxies that are easier to observe also score higher on the proxy.

The decisive test requires resolved H I maps of 40 galaxies: 20 predicted to have weak activation and 20 matched controls predicted to have strong activation. If the low-activation sample is systematically more asymmetric, warped, and dynamically unsettled, the governor hypothesis gains real support. If they look the same, the hypothesis fails.

---

## 17. Document Version

**Last updated:** 2026-06-10  
**Based on:** CGHSTC-34 M9 governor model, M20 latent angular-momentum formulation, M70 corrected activation rank reparameterization, arXiv pivot manuscript (response-organization analysis)  
**Key runs consulted:** M9 (governor product gate), M20 (latent rank + angular momentum), M22 (permutation null), M26 (nonleaky angular momentum), M58 (conformal footprint), M61–M62 (independent label audit), M70 (corrected activation rank), M74–M79 (cross-survey synthesis)
