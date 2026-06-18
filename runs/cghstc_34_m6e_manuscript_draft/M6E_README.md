CGHSTC-34 M6e: Manuscript Draft Package
==================================================

Status: complete.

Purpose
-------
Generate a first APS-style manuscript draft from the frozen M6 paper artifacts.
No new model logic is introduced.
No model parameters are retuned.
No outliers are deleted.

Outputs
-------
- manuscript draft: runs/cghstc_34_m6e_manuscript_draft/cghstc34_bdvr_aps_manuscript_draft.md
- claim checklist: runs/cghstc_34_m6e_manuscript_draft/m6e_claim_boundary_checklist.md
- figure/table map: runs/cghstc_34_m6e_manuscript_draft/m6e_figure_table_map.csv
- manuscript plan: runs/cghstc_34_m6e_manuscript_draft/m6e_manuscript_plan.json

APS-facing language rule
------------------------
Use `Conformal Gravity Hilbert Space Time Current` at first mention.
Use `CGHSTC` internally.

Next implementation step
------------------------
Create a REVTeX/APS LaTeX scaffold from this markdown draft.
Do not submit until references, data availability, code availability, and claim-boundary language are completed.

