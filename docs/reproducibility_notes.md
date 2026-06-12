# Reproducibility Notes

## Random seed

All stochastic analyses use `RANDOM_SEED = 202606` (set in `src/bdvr1/config.py`). This seed controls:
- Bootstrap resampling
- Cross-validation fold splitting
- Any random number generator calls

## Bootstrap confidence intervals

Bootstrap Q4/Q1 ratio confidence intervals use:
- 1000 bootstrap replicates
- Bias-corrected percentile method (2.5th and 97.5th percentiles)
- Seed `RANDOM_SEED` via `numpy.random.default_rng`

## Cross-validation

Cross-validated BTFR fitting uses 5 folds with:
- Randomized fold assignment using `RANDOM_SEED`
- BTFR fitted on training folds: log V ~ a + b * log M_bar
- Residuals evaluated on held-out fold
- Coherence proxy computed using the full-sample min-max normalization

Note: fold-local min-max normalization is more rigorous but is reserved for the resolved-H I follow-up.

## Proxy definitions

### xGASS coherence proxy

C = 0.35 * (INCL / 90) + 0.35 * minmax(W50cor) + 0.30 * (1 - f_atm)

where:
- INCL = inclination (degrees)
- W50cor = corrected H I linewidth (km/s)
- f_atm = M_HI / M_bar (atomic gas fraction)

### SPARC demographic proxy

C = 0.50 * (1 - RHI / Rdisk_scale) + 0.50 * rank(SBdisk)

where:
- RHI / Rdisk_scale = normalized H I extent
- SBdisk = disk central surface brightness

## Data processing

1. SPARC input: quality-1 galaxies with Vflat, L36, MHI, Rdisk, RHI, SBdisk, inclination
2. xGASS input: H I-detected galaxies with W50cor, INCL, lgMstar, lgMHI, HI flags
3. BTFR fitting: OLS log Vflat ~ log Mbar, or cross-validated OLS
4. BTFR residual: dex offset = log V_obs - log V_pred

## Output formats

- Figures: PNG at 180 DPI
- Tables: CSV with headers
- Summary tables: CSV, one row per analysis variant
