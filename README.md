# BDVR1: Disk Organization and BTFR Scatter

## Paper

This repository supports the arXiv paper:

*"Disk Organization and BTFR Scatter: A Preliminary Test of the Bound Domain Vacuum Response Hypothesis"*

The analysis tests whether unresolved scalar proxies for disk organization and velocity recoverability are associated with observed BTFR residual scatter in selected SPARC and H I-detected xGASS galaxies.

The repository does not provide evidence for a physical BDVR organization coordinate. It reproduces the preliminary scalar-proxy analysis and documents why resolved H I kinematics are required for a decisive test.

## Claim boundary

This repository supports a **preliminary scalar-proxy analysis**. The analysis does not measure the proposed BDVR organization coordinate directly and does not establish BDVR as a physical theory. The main result is that unresolved organization proxies show endpoint BTFR scatter differences, but those proxies are not independent of inclination, linewidth, and measurement recoverability. The decisive test requires resolved H I kinematics.

## Summary

| Question | Result |
|----------|--------|
| Do galaxies with higher organization proxies have less BTFR scatter? | Q4/Q1 scatter ratio < 1 (consistent with proxy-gradient) |
| Is the proxy effect independent of inclination and mass? | Partially — inclination and linewidth are entangled |
| Does the analysis establish BDVR? | No — it motivates resolved H I follow-up |

## Repository structure

```
bdvr1/
├── README.md                  This file
├── LICENSE                    MIT License
├── CITATION.cff               Citation metadata
├── .gitignore                 Ignored files
├── requirements.txt           Python dependencies
├── pyproject.toml             Project metadata
├── environment.yml            Conda environment
├── Makefile                   Build targets
├── paper/                     arXiv paper PDF, LaTeX, figures, tables
│   ├── cghstc34_arxiv.pdf
│   ├── cghstc34_arxiv.tex
│   ├── figures/
│   └── tables/
├── docs/                      Documentation
├── data/                      Input data (raw/processed/derived)
│   ├── raw/                   Reduced input files used by the pipeline; full external catalogs not committed
│   ├── external/              Optional user-downloaded full survey catalogs, not committed
│   ├── processed/             Cleaned intermediate tables
│   └── derived/               Paper-specific derived products
├── src/bdvr1/                 Analysis Python package
├── scripts/                   Reproducible analysis pipeline
├── notebooks/                 Jupyter notebooks
├── outputs/                   Generated figures, tables, logs
└── tests/                     Unit and reproducibility tests
```

## Data sources

The analysis uses two galaxy samples:

- **SPARC** (Spitzer Photometry and Accurate Rotation Curves): 175 disk galaxies with Spitzer 3.6 um photometry and H I/H-alpha rotation curves. See Lelli, McGaugh & Schombert (2016, AJ, 152, 157).
- **xGASS** (Extended GALEX Arecibo SDSS Survey): a stellar-mass-selected nearby-galaxy survey with H I measurements and upper limits. This repository uses the H I-detected subset carried through the M75 preprocessing table. See Catinella et al. (2018, MNRAS, 476, 875).

External survey data remain subject to their original licenses and citation requirements.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or with conda:

```bash
conda env create -f environment.yml
conda activate bdvr1
```

## Reproducing the analysis

```bash
# Check environment
make check

# Prepare processed input tables from committed reduced inputs
make prepare

# Run analysis pipeline
make analysis

# Reproduce figures and tables
make figures
make tables

# Validate paper-facing numbers
make validate
```

Or step by step:

```bash
python scripts/00_check_environment.py
python scripts/01_prepare_inputs.py
python scripts/02_fit_btfr.py
python scripts/03_compute_proxies.py
python scripts/04_run_ablation.py
python scripts/05_run_controls.py
python scripts/06_make_figures.py
python scripts/07_make_tables.py
python scripts/08_validate_paper_numbers.py
```

## Outputs used in the paper

### Figures

| File | Description |
|------|-------------|
| `outputs/figures/fig1_cross_survey_quartiles.png` | Cross-survey quartile scatter comparison |
| `outputs/figures/fig2_xgass_velocity_variants.png` | xGASS velocity recovery variants |
| `outputs/figures/fig3_proxy_variant_comparison.png` | Proxy variant comparison |
| `outputs/figures/fig4_mass_bin_quartiles.png` | Mass-bin quartile analysis |
| `outputs/figures/fig5_q4_q1_ratio_summary.png` | Q4/Q1 ratio summary |

### Tables

| File | Description |
|------|-------------|
| `outputs/tables/table1_sparc_sample_selection.csv` | SPARC sample selection |
| `outputs/tables/table2_xgass_proxy_ablation.csv` | xGASS proxy ablation |
| `outputs/tables/xgass_controls_summary.csv` | xGASS control variable summary |
| `outputs/tables/mass_controls_summary.csv` | Mass control summary |
| `outputs/tables/inclination_restricted_summary.csv` | Inclination-restricted analysis |

### Paper-facing SPARC M74 data products

The paper-facing SPARC result is reproduced from the M74 file set in `data/derived/`:
`sparc_m74_proxy_table.csv`, `sparc_m74_quartile_scatter.csv`, and
`sparc_m74_btfr_summary.json`. The diagnostic `sparc_proxy_table.csv` uses a
different proxy definition and does not reproduce the M74 SPARC Q4/Q1 value.

## Limitations

1. The organization proxies are unresolved scalars — they do not measure the proposed BDVR organization coordinate directly.
2. The SPARC sample is not volume-limited; selection effects may influence scatter patterns.
3. The xGASS H I-detected sample is biased toward gas-rich galaxies.
4. Inclination and linewidth are entangled with the proxy definition.
5. The analysis does not establish a causal physical mechanism.

## Citation

If you use this repository, please cite the associated arXiv paper:

```bibtex
@software{bdvr1,
  author = {Jake Enholm},
  title = {BDVR1: Disk Organization and BTFR Scatter},
  year = {2026},
  url = {https://github.com/jenholm/bdvr1}
}
```

For software citation metadata, see `CITATION.cff`.

## Contact

Jake Enholm — [GitHub](https://github.com/jenholm)
