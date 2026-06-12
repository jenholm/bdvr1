# Data Sources

## SPARC

- **Reference**: Lelli, McGaugh & Schombert (2016, AJ, 152, 157)
- **Contents**: 175 disk galaxies with Spitzer 3.6 um photometry and H I/H-alpha rotation curves
- **Available at**: http://astroweb.cwru.edu/SPARC/
- **Columns used**: galaxy name, quality flag (Q), morphological type (T), flat velocity (Vflat), flat velocity uncertainty (e_Vflat), 3.6 um luminosity (L36), H I mass (MHI), disk scale length (Rdisk), H I radius (RHI), effective radius (Reff), effective surface brightness (SBeff), disk surface brightness (SBdisk), distance (D), inclination (Inc), reference (Ref)
- **License**: Available at the SPARC website; cite Lelli+2016

## xGASS

- **Reference**: Catinella et al. (2018, MNRAS, 476, 875)
- **Contents**: Stellar-mass-selected nearby-galaxy survey with H I measurements. This analysis uses the H I-detected subset carried through the M75 preprocessing table.
- **Available at**: https://xgass.astro.umd.edu/
- **Columns used**: GASS ID, SDSS photometry, stellar mass, inclination, W50 linewidth, H I mass, gas fraction, HI flags, weights
- **License**: Available at the xGASS website; cite Catinella+2018

## Usage notes

These catalogs contain survey data. Users should download directly from the original sources and cite the original survey papers.

This repository includes reduced input tables and derived analysis products needed to reproduce the paper results. It does not redistribute the full original SPARC or xGASS catalogs. The committed raw input files (`data/raw/sparc/sparc_quality1_rich_inputs.csv`, `data/raw/xgass/m75_xgass_coherence_scores.csv`, `data/raw/xgass/xgass_representative_sample.csv`) contain a subset of survey columns necessary for reproducibility.
