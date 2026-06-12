# Data directory

## Structure

```
data/
├── raw/         User-downloaded source files (not committed)
├── external/    Manually downloaded external catalogs (not committed)
├── processed/   Cleaned intermediate tables
└── derived/     Paper-specific derived products
```

## Obtaining data

### SPARC

Download the SPARC catalog from http://astroweb.cwru.edu/SPARC/

Place the file in `data/raw/sparc/` and run:

```bash
python scripts/01_prepare_inputs.py
```

This will produce `data/processed/sparc_clean.csv`.

### xGASS

Download the xGASS representative sample from https://xgass.astro.umd.edu/

Place the file in `data/raw/xgass/` and run:

```bash
python scripts/01_prepare_inputs.py
```

This will produce `data/processed/xgass_clean.csv`.

## Derived tables

The following derived tables are committed and redistributable:

- `data/derived/sparc_proxy_table.csv` — SPARC proxy scores
- `data/derived/xgass_proxy_table.csv` — xGASS proxy scores
- `data/derived/btfr_residuals_sparc.csv` — SPARC BTFR residuals
- `data/derived/btfr_residuals_xgass.csv` — xGASS BTFR residuals
- `data/derived/proxy_ablation_results.csv` — Ablation results
- `data/derived/inclination_restricted_results.csv` — Inclination controls
- `data/derived/mass_control_results.csv` — Mass controls
- `data/derived/measurement_quality_controls.csv` — Quality controls

## License notes

Original survey data remain subject to their original licenses and citation requirements:

- SPARC: Cite Lelli, McGaugh & Schombert (2016, AJ, 152, 157)
- xGASS: Cite Catinella et al. (2018, MNRAS, 476, 875)
