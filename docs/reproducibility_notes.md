# Reproducibility Notes

## Random seed

All stochastic analyses use `RANDOM_SEED = 202606` (set in `src/bdvr1/config.py`). This seed controls:
- Bootstrap resampling
- Cross-validation fold splitting
- Any random number generator calls

## Bootstrap confidence intervals

Bootstrap Q4/Q1 ratio confidence intervals use:
- 1000 bootstrap replicates
- Percentile interval using the 2.5th and 97.5th percentiles
- Seed `RANDOM_SEED` via `numpy.random.default_rng`

## Cross-validation

Cross-validated BTFR fitting uses 5 folds with:
- Randomized fold assignment using `RANDOM_SEED`
- BTFR fitted on training folds: log V ~ a + b * log M_bar
- Residuals evaluated on held-out fold
- xGASS organization proxy computed using full-sample min-max normalization

Note: fold-local min-max normalization would be more rigorous for a fully leakage-free scalar-proxy validation. The current paper reports this as a limitation.

## Proxy definitions

### xGASS organization proxy

C = 0.35 * (INCL / 90) + 0.35 * minmax(W50cor) + 0.30 * (1 - f_atm)

where:
- INCL = inclination (degrees)
- W50cor = corrected H I linewidth (km/s)
- f_atm is inherited from the M75 preprocessing column `f_atm_total`; it is not recomputed in the processed table from the visible `M_HI` and `Mbar_msun` columns.

### SPARC M74 coherence score (paper-facing)

The paper-facing SPARC result uses the historical M74 `coherence_score`, which is a 5-component average:

C = nanmean([1 - f_gas, f_star, clamp((log10_Sigma_b - 6.5) / 4.0, 0, 1), 1 / (1 + RHI_over_Rdisk), taxonomy_prior])

where:
- f_gas = gas fraction from M72 audit
- f_star = stellar fraction from M72 audit
- log10_Sigma_b = baryonic surface density
- RHI_over_Rdisk = HI-to-optical disk scale-length ratio
- taxonomy_prior = 0.8 if mature_or_control, else 0.3
- Plus radial-curve bonuses (+0.15 flatness, +0.10 curve_flatness) for 25 resolved galaxies

Quartiles via `pd.qcut(..., duplicates='drop')` give n=22/22/21/22.

### SPARC diagnostic demographic proxy (current pipeline)

The current pipeline also produces a separate diagnostic proxy:

D = (z_logSigma + z_fstar - z_RHI/Rd) / 3

where each z-score is robustly standardized using the median and MAD, then the final score is min-max normalized to [0,1]. This diagnostic proxy is **not** the paper-facing M74 proxy.

### xGASS BTFR residuals

The xGASS processed residuals are copied from the M75 `btfr_offset_dex` column. They reproduce as a global OLS fit (slope ≈ 0.279, intercept ≈ −0.689), **not** as the McGaugh 2012 calibration (Mbar = 50 × Vflat⁴). The cross-validated paper results refit BTFR inside folds downstream.

## Data processing

1. SPARC input: quality-1 galaxies with Vflat, L36, MHI, Rdisk, RHI, SBdisk, inclination
2. xGASS input: H I-detected galaxies with W50cor, INCL, lgMstar, lgMHI, HI flags
3. BTFR fitting: OLS log Vflat ~ log Mbar, or cross-validated OLS
4. BTFR residual: dex offset = log V_obs - log V_pred

## Output formats

- Figures: PNG at 180 DPI
- Tables: CSV with headers
- Summary tables: CSV, one row per analysis variant
