# CGHSTC-34 M44: Baryonic Maturity vs BDVR Endpoint Residual Audit

M44 tests whether the visible baryonic maturity ruler from M43 explains deviations from the mature M36 BDVR endpoint residual without circularity.

Key contract:

- visible baryonic maturity is an input from M43;
- BDVR endpoint residual is an outcome from the M36 no-governor mature endpoint;
- velocity residuals are not used to define the maturity score;
- M44 does not refit M36;
- measurement-limited/quarantined rows remain separate.

Outcome classification: `insufficient_clean_bridge_signal`

Clean direct bridge rows: 60
Measurement-limited/quarantined rows: 27

Clean Spearman(baryonic_maturity_score, abs endpoint residual): -0.02417338149485969
Clean Spearman(maturity_gap, abs endpoint residual): 0.02417338149485969

UGC07125 remains quarantined. This audit does not treat it as a clean scalar object or juvenile prototype.
