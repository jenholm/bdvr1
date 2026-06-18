CGHSTC-34 M6f: REVTeX Scaffold
=======================================

Status: complete.

Purpose
-------
Create an APS/REVTeX-style LaTeX scaffold from the M6/M6e manuscript artifacts.
This stage introduces no new model logic, no retuning, and no outlier deletion.

Outputs
-------
- cghstc34_bdvr_aps_draft.tex
- refs_stub.bib
- figures/
- m6f_figure_copy_report.json

Compile
-------
From this directory:

pdflatex cghstc34_bdvr_aps_draft.tex
bibtex cghstc34_bdvr_aps_draft
pdflatex cghstc34_bdvr_aps_draft.tex
pdflatex cghstc34_bdvr_aps_draft.tex

APS-facing language rule
------------------------
Use `Conformal Gravity Hilbert Space Time Current` at first mention.
Do not rely on `CGHSTC` alone in external-facing text until the acronym is established.

Figure copy report
------------------
{
  "appendix_fig_m5d_pred_vs_obs_total_mass.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/appendix_fig_m5d_pred_vs_obs_total_mass.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/appendix_fig_m5d_pred_vs_obs_total_mass.png"
  },
  "appendix_fig_ugc07125_gas_participation_vs_rhi.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/appendix_fig_ugc07125_gas_participation_vs_rhi.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/appendix_fig_ugc07125_gas_participation_vs_rhi.png"
  },
  "appendix_fig_ugc07125_hi_extent.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/appendix_fig_ugc07125_hi_extent.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/appendix_fig_ugc07125_hi_extent.png"
  },
  "appendix_fig_ugc07125_participation_vs_rhi.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/appendix_fig_ugc07125_participation_vs_rhi.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/appendix_fig_ugc07125_participation_vs_rhi.png"
  },
  "fig_3_m5_pred_vs_obs.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/fig_3_m5_pred_vs_obs.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/fig_3_m5_pred_vs_obs.png"
  },
  "fig_4a_m5b_median_abs_error_by_model.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/fig_4a_m5b_median_abs_error_by_model.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/fig_4a_m5b_median_abs_error_by_model.png"
  },
  "fig_4b_m5b_fraction_within_010_by_model.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/fig_4b_m5b_fraction_within_010_by_model.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/fig_4b_m5b_fraction_within_010_by_model.png"
  },
  "fig_5_m5a_residual_dashboard.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/fig_5_m5a_residual_dashboard.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/fig_5_m5a_residual_dashboard.png"
  },
  "fig_6_m5b_pred_vs_obs_grid.png": {
    "copied": true,
    "dest": "runs/cghstc_34_m6f_revtex_scaffold/figures/fig_6_m5b_pred_vs_obs_grid.png",
    "source": "runs/cghstc_34_m6_paper_artifacts/figures/fig_6_m5b_pred_vs_obs_grid.png"
  }
}
