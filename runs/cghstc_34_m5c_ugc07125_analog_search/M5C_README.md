CGHSTC-34 M5c: UGC07125 Analog Search
==============================================

Status: complete.

Purpose
-------
Treat UGC07125 as a possible prediction target rather than deleting or tuning it away.
The search asks whether similar late-type, gas-dominated, HI-extended galaxies show similar overprediction.

Prediction hypothesis
---------------------
Late-type, gas-dominated, HI-extended galaxies with low Vflat for baryonic mass should be overpredicted by BTFR-like and frozen BDVR response models unless an additional gas-rich late-type conditioning regime is present.

Hard analog criteria
--------------------
T >= 8
gas_frac >= 0.70
stellar_to_gas_ratio <= 0.35
RHI / Rdisk >= 5.0

Summary
-------
{
  "milestone": "CGHSTC-34-M5c",
  "status": "UGC07125 analog search, no retuning",
  "n_total": 87,
  "n_hard_analogs": 8,
  "n_top_scored_reported": 15,
  "hard_analog_names": [
    "UGC07125",
    "F583-1",
    "F563-1",
    "UGC12632",
    "DDO161",
    "UGC00731",
    "DDO064",
    "NGC3741"
  ],
  "top_scored_names": [
    "UGC07125",
    "F583-1",
    "F563-1",
    "UGC12632",
    "DDO161",
    "UGC00731",
    "DDO064",
    "NGC3741",
    "UGC06446",
    "UGCA442",
    "NGC3109",
    "D631-7",
    "UGC01230",
    "UGC05005",
    "UGC00128"
  ],
  "hard_analog_m4c_log10_error_stats": {
    "n": 8,
    "median": 0.052947626856057695,
    "mean": 0.06265138528307826,
    "min": -0.0343972706855351,
    "max": 0.2321401297980161,
    "n_overpredicted": 6,
    "n_underpredicted": 2,
    "n_abs_gt_010": 1,
    "n_abs_gt_015": 1,
    "n_abs_gt_020": 1
  },
  "hard_analog_mond_log10_error_stats": {
    "n": 8,
    "median": 0.03166241368327505,
    "mean": 0.03505835178874623,
    "min": -0.061313869546994,
    "max": 0.2052260404052944,
    "n_overpredicted": 5,
    "n_underpredicted": 3,
    "n_abs_gt_010": 1,
    "n_abs_gt_015": 1,
    "n_abs_gt_020": 1
  },
  "hard_analog_newtonian_log10_error_stats": {
    "n": 8,
    "median": -0.2577322540285273,
    "mean": -0.28491508115858993,
    "min": -0.4395794962022725,
    "max": -0.124411165192023,
    "n_overpredicted": 0,
    "n_underpredicted": 8,
    "n_abs_gt_010": 8,
    "n_abs_gt_015": 7,
    "n_abs_gt_020": 7
  },
  "top_scored_m4c_log10_error_stats": {
    "n": 15,
    "median": 0.0248825125352315,
    "mean": 0.035518985959528945,
    "min": -0.0383771483298666,
    "max": 0.2321401297980161,
    "n_overpredicted": 10,
    "n_underpredicted": 5,
    "n_abs_gt_010": 1,
    "n_abs_gt_015": 1,
    "n_abs_gt_020": 1
  },
  "prediction_hypothesis": "Late-type, gas-dominated, HI-extended galaxies with low Vflat for baryonic mass should be overpredicted by BTFR-like and frozen BDVR response models unless an additional gas-rich late-type conditioning regime is present."
}

UGC07125 row
------------
                                                       73
galaxy_name                                      UGC07125
T                                                     9.0
v_flat_obs_km_s                                      65.2
M_baryon_Msun                           7512569999.999999
star_frac                                        0.180497
gas_frac                                         0.819503
stellar_to_gas_ratio                             0.220253
Rdisk                                                3.38
RHI                                                 23.04
RHI_over_Rdisk                                   6.816568
sample_btfr_log10_v_residual                    -0.239847
log10_velocity_error__newtonian_outer           -0.124411
log10_velocity_error__mond_simple_btfr           0.205226
log10_velocity_error__m4c_full_frozen             0.23214

Hard analog table
-----------------
galaxy_name  ugc07125_regime_score  ugc07125_analog_distance    T  v_flat_obs_km_s  M_baryon_Msun  gas_frac  stellar_to_gas_ratio  RHI_over_Rdisk  sample_btfr_log10_v_residual  log10_velocity_error__newtonian_outer  log10_velocity_error__mond_simple_btfr  log10_velocity_error__m4c_full_frozen
   UGC07125                    5.5                  0.000000  9.0             65.2   7.512570e+09  0.819503              0.220253        6.816568                     -0.239847                              -0.124411                                0.205226                               0.232140
     F583-1                    4.5                  4.542106  9.0             85.8   3.320580e+09  0.851532              0.174354        6.631356                     -0.028501                              -0.349367                               -0.002657                               0.024883
     F563-1                    4.5                  5.747685  9.0            109.9   5.207500e+09  0.817283              0.223567        6.667614                      0.028247                              -0.439579                               -0.061314                              -0.034397
   UGC12632                    4.0                  3.222063  9.0             71.7   2.970020e+09  0.780978              0.280446        5.206612                     -0.093882                              -0.261105                                0.063197                               0.086733
     DDO161                    4.0                  3.387054 10.0             66.3   2.106740e+09  0.869941              0.149503        8.762295                     -0.089144                              -0.244820                                0.059916                               0.092141
   UGC00731                    4.0                  3.818442 10.0             73.3   2.564810e+09  0.937032              0.067199        5.030435                     -0.067749                              -0.249744                                0.037686                               0.056845
     DDO064                    4.0                  4.365672 10.0             46.1   3.591300e+08  0.781416              0.279728        5.057971                     -0.047362                              -0.254359                                0.025638                               0.049050
    NGC3741                    4.0                  8.356662 10.0             50.1   2.560600e+08  0.945325              0.057837       21.000000                      0.026937                              -0.355934                               -0.047226                              -0.006183

Top 15 scored analog candidates
-------------------------------
galaxy_name  ugc07125_regime_score  ugc07125_analog_distance  ugc07125_hard_analog    T  v_flat_obs_km_s  M_baryon_Msun  gas_frac  stellar_to_gas_ratio  RHI_over_Rdisk  sample_btfr_log10_v_residual  log10_velocity_error__newtonian_outer  log10_velocity_error__mond_simple_btfr  log10_velocity_error__m4c_full_frozen
   UGC07125                    5.5                  0.000000                  True  9.0             65.2   7.512570e+09  0.819503              0.220253        6.816568                     -0.239847                              -0.124411                                0.205226                               0.232140
     F583-1                    4.5                  4.542106                  True  9.0             85.8   3.320580e+09  0.851532              0.174354        6.631356                     -0.028501                              -0.349367                               -0.002657                               0.024883
     F563-1                    4.5                  5.747685                  True  9.0            109.9   5.207500e+09  0.817283              0.223567        6.667614                      0.028247                              -0.439579                               -0.061314                              -0.034397
   UGC12632                    4.0                  3.222063                  True  9.0             71.7   2.970020e+09  0.780978              0.280446        5.206612                     -0.093882                              -0.261105                                0.063197                               0.086733
     DDO161                    4.0                  3.387054                  True 10.0             66.3   2.106740e+09  0.869941              0.149503        8.762295                     -0.089144                              -0.244820                                0.059916                               0.092141
   UGC00731                    4.0                  3.818442                  True 10.0             73.3   2.564810e+09  0.937032              0.067199        5.030435                     -0.067749                              -0.249744                                0.037686                               0.056845
     DDO064                    4.0                  4.365672                  True 10.0             46.1   3.591300e+08  0.781416              0.279728        5.057971                     -0.047362                              -0.254359                                0.025638                               0.049050
    NGC3741                    4.0                  8.356662                  True 10.0             50.1   2.560600e+08  0.945325              0.057837       21.000000                      0.026937                              -0.355934                               -0.047226                              -0.006183
   UGC06446                    3.0                  5.055832                 False  7.0             82.2   2.328070e+09  0.787807              0.269346        6.932886                     -0.007055                              -0.310607                               -0.022596                               0.005195
    UGCA442                    3.0                  5.879654                 False  9.0             56.4   4.197900e+08  0.833250              0.200120        3.703390                      0.022609                              -0.364413                               -0.044995                              -0.027913
    NGC3109                    3.0                  5.975357                 False  9.0             66.2   7.314100e+08  0.867379              0.152898        3.846154                      0.029551                              -0.363022                               -0.054291                              -0.038377
     D631-7                    3.0                  6.288759                 False 10.0             57.7   4.837000e+08  0.797395              0.254083        0.000000                      0.016519                              -0.112695                               -0.039505                              -0.034307
   UGC01230                    2.5                  3.163259                 False  9.0            103.7   1.236190e+10  0.691795              0.445515        6.057604                     -0.094502                              -0.259973                                0.057769                               0.083484
   UGC05005                    2.5                  4.397275                 False 10.0             98.9   6.163690e+09  0.667407              0.498336        6.753125                     -0.036572                              -0.345659                                0.002790                               0.030598
   UGC00128                    2.5                  4.672542                 False  8.0            129.3   1.589323e+10  0.621852              0.608101        5.255462                     -0.027030                              -0.349552                               -0.010769                               0.012895

Interpretation guide
--------------------
If hard analogs are also overpredicted by MOND/BTFR and M4c, the UGC07125 regime may be real.
If hard analogs are not overpredicted, UGC07125 is more likely a special kinematic/data case.
Do not retune from this stage. Use this only to define the next validation question.

