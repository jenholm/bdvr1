CGHSTC-34 M5a: Data Audit and Outlier Report
======================================================

Status: M5a complete.

This audit checks the M5 frozen-M4c validation data and residual population.
It does not retune parameters, delete galaxies, or alter the M4c model.

Inputs
------
Raw SPARC source: data/sparc_lite/SPARC_Lelli2016c.mrt
Q1 rich input: data/sparc_lite/sparc_quality1_rich_inputs.csv
M5 rich output: runs/cghstc_34_m5_sparc_quality1_frozen_m4c/m5_quality1_rich_inputs.csv
M5 prediction output: runs/cghstc_34_m5_sparc_quality1_frozen_m4c/m5_frozen_m4c_predictions.csv
M5 summary: runs/cghstc_34_m5_sparc_quality1_frozen_m4c/m5_frozen_m4c_summary.json

Row counts
----------
Q1 input rows: 87
M5 rich rows: 87
M5 prediction rows: 87
M5 summary n: 87

M5 metrics reconfirmed
----------------------
median_abs_log10_velocity_error: 0.041613899469354995
mean_abs_log10_velocity_error: 0.04572143797277067
max_abs_log10_velocity_error: 0.23214012979801618
frac_within_010_dex: 0.9540229885057471
frac_within_015_dex: 0.9885057471264368
frac_within_020_dex: 0.9885057471264368

Outlier counts
--------------
abs error > 0.10 dex: 4
abs error > 0.15 dex: 1
abs error > 0.20 dex: 1

Worst 10 residuals
------------------
galaxy_name  v_flat_obs_km_s  v_m5_bdvr_km_s  velocity_ratio_pred_over_obs  log10_velocity_error  abs_log10_velocity_error    T  M_baryon_Msun  Rdisk  S_star_gas  S_internal  S_struct    Q_eff
   UGC07125             65.2      111.272469                      1.706633              0.232140                  0.232140  9.0   7.512570e+09   3.38    1.000000         1.0  1.000000 1.131952
   UGC07399            103.0       73.834479                      0.716840             -0.144578                  0.144578  8.0   1.568850e+09   1.64    1.000000         1.0  1.000000 1.090623
    NGC5371            209.5      268.082121                      1.279628              0.107084                  0.107084  4.0   1.850659e+11   7.44    1.107906         1.1  1.218697 1.323791
     F571-8            139.7      110.550427                      0.791342             -0.101636                  0.101636  5.0   7.452060e+09   3.56    1.000000         1.0  1.000000 1.121837
   UGC09133            226.8      285.311438                      1.257987              0.099676                  0.099676  2.0   1.859222e+11   6.97    1.000000         1.3  1.300000 1.495959
   UGC06614            199.8      250.637343                      1.254441              0.098450                  0.098450  1.0   9.128604e+10   5.10    1.000000         1.4  1.400000 1.647542
    NGC5055            179.0      222.413144                      1.242532              0.094307                  0.094307  4.0   9.205126e+10   3.20    1.000000         1.1  1.100000 1.291972
     DDO161             66.3       81.969958                      1.236349              0.092141                  0.092141 10.0   2.106740e+09   1.22    1.000000         1.0  1.000000 1.159981
    NGC0024            106.3       86.670433                      0.815338             -0.088662                  0.088662  5.0   2.843580e+09   1.34    1.000000         1.0  1.000000 1.116236
   UGC12632             71.7       87.549145                      1.221048              0.086733                  0.086733  9.0   2.970020e+09   2.42    1.000000         1.0  1.000000 1.114477

Main outlier
------------
UGC07125 remains the formal strong-pass blocker.
It is retained in all metrics.
No model retuning was performed.

Generated outputs
-----------------
m5a_parser_audit.json
m5a_column_ranges.csv
m5a_outlier_report.csv
m5a_top_residuals.csv
m5a_residual_correlations.csv
m5a_ugc07125_audit.txt
m5a_input_histograms.png
m5a_residual_dashboard.png

Interpretation boundary
-----------------------
M5a is an audit stage only.
It does not prove CGHSTC, replace dark matter, or establish a final physical theory.
It supports or challenges the reliability of the M5 frozen-M4c validation pipeline.
