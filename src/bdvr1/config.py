"""Paths, constants, random seed, and default configuration."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

RANDOM_SEED = 202606
N_BOOTSTRAP = 1000
N_FOLDS = 5
WTURB_KMS = 10.0
HELIUM_FACTOR = 1.33

SPARC_PATHS = {
    "raw": DATA_DIR / "raw" / "sparc" / "sparc_quality1_rich_inputs.csv",
    "processed": DATA_DIR / "processed" / "sparc_clean.csv",
    "proxy_table": DATA_DIR / "derived" / "sparc_proxy_table.csv",
    "btfr_residuals": DATA_DIR / "derived" / "btfr_residuals_sparc.csv",
}

XGASS_PATHS = {
    "raw": DATA_DIR / "raw" / "xgass" / "m75_xgass_coherence_scores.csv",
    "raw_representative_sample": DATA_DIR / "raw" / "xgass" / "xgass_representative_sample.csv",
    "processed": DATA_DIR / "processed" / "xgass_clean.csv",
    "proxy_table": DATA_DIR / "derived" / "xgass_proxy_table.csv",
    "btfr_residuals": DATA_DIR / "derived" / "btfr_residuals_xgass.csv",
}

OUTPUT_TABLES = OUTPUTS_DIR / "tables"
OUTPUT_FIGURES = OUTPUTS_DIR / "figures"

# Reference outputs from main analysis for reproducibility checks
DERIVED_DIR = DATA_DIR / "derived"
SPARC_SUMMARY_PATH = DERIVED_DIR / "sparc_btfr_summary.json"
ARXIV_REVISED_ANALYSIS_PATH = DERIVED_DIR / "arxiv_revised_analysis.json"
