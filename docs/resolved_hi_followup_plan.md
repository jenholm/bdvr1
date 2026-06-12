# Resolved H I Follow-up Plan

## Motivation

The scalar-proxy analysis in this paper reveals BTFR scatter differences associated with unresolved disk organization proxies. However, the decisive test of the BDVR hypothesis requires **resolved H I kinematics** — specifically, direct measurement of:

1. Kinematic asymmetry (lopsidedness, warps)
2. Non-circular motion fraction
3. H I morphological organization
4. Kinematic axis twists

## Proposed path

### Step 1: Identify suitable resolved H I data

| Survey | Resolution | Coverage | Galaxies | Status |
|--------|-----------|----------|----------|--------|
| THINGS | ~6" | Nearby | 34 | Available |
| VIVA | ~15" | Virgo cluster | 45 | Available |
| LITTLE THINGS | ~6" | Dwarf | 41 | Available |
| New VLA/ASKAP/MeerKAT | Variable | Various | Ongoing | Future |

Note: VIVA is cluster-specific. Virgo environmental effects should be treated as a confounder rather than as a clean field-galaxy comparison.

### Step 2: Compute structure metrics

From resolved H I moment maps (MOM0, MOM1, MOM2), compute:

- **Asymmetry index**: 180-degree flux asymmetry of MOM0
- **Lopsidedness index**: flux-weighted centroid offset relative to emission radius
- **Warp index**: inner-vs-outer kinematic axis twist
- **Non-circular motion index**: residual velocity structure after tilted-ring or disk-model subtraction, supplemented by MOM2 dispersion relative to velocity span
- **Approach-recede mismatch**: side-to-side velocity asymmetry

### Step 3: Test response-organization predictions

1. Do galaxies with higher lopsidedness/warp indices have larger BTFR scatter?
2. Are non-circular motions systematically higher in low-proxy galaxies?
3. Does Q4/Q1 scatter ratio persist when resolved structure metrics are used instead of unresolved proxies?
4. Do resolved organization metrics add held-out explanatory power after controlling for mass, inclination, linewidth, distance uncertainty, and measurement quality?

### Step 4: Control for recoverability

Resolved metrics should reduce, diagnose, or explicitly model:
- Global inclination dependence (unlike W50-based proxies)
- Line-of-sight projection effects
- Beam smearing
- Confusion between linewidth broadening and ordered rotation

## Expected outcome

If the endpoint contrast persists with resolved organization metrics measured independently of the BTFR velocity, the response-organization interpretation becomes more plausible. It would still need to be compared against conventional disk-settling explanations. If the scatter difference disappears when resolved metrics are substituted, the scalar-proxy result was driven by unresolved recoverability effects.
