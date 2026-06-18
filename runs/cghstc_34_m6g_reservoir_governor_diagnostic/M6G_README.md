CGHSTC-34 M6g: Reservoir Governor Diagnostic
=======================================================

Status: complete.

Purpose
-------
Test whether BDVR overprediction is associated with weak reservoir activation indicators.
This is inspired by the idea that the reservoir may require organized baryonic structure rather than raw baryonic mass.

This stage is diagnostic only.
No model term is accepted.
No parameters are retuned.
No outliers are deleted.

Core diagnostic quantities
--------------------------
A_source_required = (V_obs / V_pred)^4
A_Q_required      = (V_obs / V_pred)^2

Interpretation
--------------
A_source_required < 1 means the current frozen BDVR prediction is too high.
A_source_required << 1 suggests strong reservoir suppression would be needed.

Surface-density proxy
---------------------
Sigma_baryon = M_baryon / (2 pi Rdisk^2)
Sigma_star   = M_star / (2 pi Rdisk^2)
Sigma_gas    = M_gas / (2 pi Rdisk^2)

Summary
-------
{
  "best_diagnostic_governor_grid_rows": [
    {
      "delta_frac010_vs_base": -0.09195402298850575,
      "delta_median_abs_vs_base": -0.001426458170367302,
      "frac_within_010_dex": 0.8620689655172413,
      "frac_within_015_dex": 0.9770114942528736,
      "gate_name": "stellar_fraction_source_gate",
      "k": 4.0,
      "max_abs_log10_error": 0.1829600792249873,
      "mean_abs_log10_error": 0.04982340156648453,
      "median_abs_log10_error": 0.040187441298987596,
      "n_above_020_dex": 0,
      "placement": "source",
      "target_A": 0.5265199356691739,
      "target_new_abs_log10_error": 0.16249383468846126,
      "target_new_log10_error": 0.16249383468846126,
      "xcol": "star_frac",
      "xcrit": 0.15395263960754266
    },
    {
      "delta_frac010_vs_base": -0.06896551724137923,
      "delta_median_abs_vs_base": -0.0008311212003665747,
      "frac_within_010_dex": 0.8850574712643678,
      "frac_within_015_dex": 0.9655172413793104,
      "gate_name": "sigma_star_source_gate",
      "k": 2.0,
      "max_abs_log10_error": 0.18552470445040706,
      "mean_abs_log10_error": 0.050496449006261664,
      "median_abs_log10_error": 0.04078277826898832,
      "n_above_020_dex": 0,
      "placement": "source",
      "target_A": 0.614517402074651,
      "target_new_abs_log10_error": 0.17927367626514137,
      "target_new_log10_error": 0.17927367626514137,
      "xcol": "log10_Sigma_star",
      "xcrit": 7.043075821983066
    },
    {
      "delta_frac010_vs_base": -0.08045977011494243,
      "delta_median_abs_vs_base": -0.00014595770389719265,
      "frac_within_010_dex": 0.8735632183908046,
      "frac_within_015_dex": 0.9655172413793104,
      "gate_name": "sigma_baryon_source_gate",
      "k": 4.0,
      "max_abs_log10_error": 0.3618365439848468,
      "mean_abs_log10_error": 0.05308628046247452,
      "median_abs_log10_error": 0.041467941765457705,
      "n_above_020_dex": 2,
      "placement": "source",
      "target_A": 0.7698523780569888,
      "target_new_abs_log10_error": 0.20374199370748106,
      "target_new_log10_error": 0.20374199370748106,
      "xcol": "log10_Sigma_baryon",
      "xcrit": 7.717905802227163
    },
    {
      "delta_frac010_vs_base": -0.10344827586206895,
      "delta_median_abs_vs_base": 4.665816807723072e-05,
      "frac_within_010_dex": 0.8505747126436781,
      "frac_within_015_dex": 0.9770114942528736,
      "gate_name": "stellar_fraction_source_gate",
      "k": 4.0,
      "max_abs_log10_error": 0.19054881229384246,
      "mean_abs_log10_error": 0.0516266540499408,
      "median_abs_log10_error": 0.04166055763743213,
      "n_above_020_dex": 0,
      "placement": "source",
      "target_A": 0.472168556116077,
      "target_new_abs_log10_error": 0.1506643953058172,
      "target_new_log10_error": 0.1506643953058172,
      "xcol": "star_frac",
      "xcrit": 0.20835772756794368
    },
    {
      "delta_frac010_vs_base": -0.11494252873563215,
      "delta_median_abs_vs_base": 0.0007329777700336229,
      "frac_within_010_dex": 0.8390804597701149,
      "frac_within_015_dex": 0.9195402298850575,
      "gate_name": "sigma_baryon_source_gate",
      "k": 4.0,
      "max_abs_log10_error": 0.4266125920217396,
      "mean_abs_log10_error": 0.05926435578696992,
      "median_abs_log10_error": 0.04234687723938852,
      "n_above_020_dex": 2,
      "placement": "source",
      "target_A": 0.6417336142102738,
      "target_new_abs_log10_error": 0.18397882689044626,
      "target_new_log10_error": 0.18397882689044626,
      "xcol": "log10_Sigma_baryon",
      "xcrit": 7.874051142158947
    },
    {
      "delta_frac010_vs_base": -0.04597701149425282,
      "delta_median_abs_vs_base": 0.0009012850674155123,
      "frac_within_010_dex": 0.9080459770114943,
      "frac_within_015_dex": 0.9540229885057471,
      "gate_name": "sigma_baryon_source_gate",
      "k": 8.0,
      "max_abs_log10_error": 0.6555590487984563,
      "mean_abs_log10_error": 0.056554955089934945,
      "median_abs_log10_error": 0.04251518453677041,
      "n_above_020_dex": 2,
      "placement": "source",
      "target_A": 0.9179606627729087,
      "target_new_abs_log10_error": 0.22284614750935577,
      "target_new_log10_error": 0.22284614750935577,
      "xcol": "log10_Sigma_baryon",
      "xcrit": 7.717905802227163
    },
    {
      "delta_frac010_vs_base": -0.09195402298850575,
      "delta_median_abs_vs_base": 0.0009206916724779357,
      "frac_within_010_dex": 0.8620689655172413,
      "frac_within_015_dex": 0.9195402298850575,
      "gate_name": "sigma_star_source_gate",
      "k": 4.0,
      "max_abs_log10_error": 0.342233268129992,
      "mean_abs_log10_error": 0.057276750587251575,
      "median_abs_log10_error": 0.042534591141832834,
      "n_above_020_dex": 4,
      "placement": "source",
      "target_A": 0.5115218479527078,
      "target_new_abs_log10_error": 0.15935617676981914,
      "target_new_log10_error": 0.15935617676981914,
      "xcol": "log10_Sigma_star",
      "xcrit": 7.264722532602023
    },
    {
      "delta_frac010_vs_base": -0.12643678160919536,
      "delta_median_abs_vs_base": 0.0012773962933234906,
      "frac_within_010_dex": 0.8275862068965517,
      "frac_within_015_dex": 0.9540229885057471,
      "gate_name": "sigma_baryon_source_gate",
      "k": 2.0,
      "max_abs_log10_error": 0.2574530910548165,
      "mean_abs_log10_error": 0.0580800638638333,
      "median_abs_log10_error": 0.04289129576267839,
      "n_above_020_dex": 2,
      "placement": "source",
      "target_A": 0.572350649324228,
      "target_new_abs_log10_error": 0.17155567476223205,
      "target_new_log10_error": 0.17155567476223205,
      "xcol": "log10_Sigma_baryon",
      "xcrit": 7.874051142158947
    },
    {
      "delta_frac010_vs_base": -0.09195402298850575,
      "delta_median_abs_vs_base": 0.0015372958125116493,
      "frac_within_010_dex": 0.8620689655172413,
      "frac_within_015_dex": 0.9655172413793104,
      "gate_name": "stellar_fraction_source_gate",
      "k": 8.0,
      "max_abs_log10_error": 0.17120161029696765,
      "mean_abs_log10_error": 0.05171144227382154,
      "median_abs_log10_error": 0.04315119528186655,
      "n_above_020_dex": 0,
      "placement": "source",
      "target_A": 0.44450904303125743,
      "target_new_abs_log10_error": 0.14411027995394768,
      "target_new_log10_error": 0.14411027995394768,
      "xcol": "star_frac",
      "xcrit": 0.20835772756794368
    },
    {
      "delta_frac010_vs_base": -0.09195402298850575,
      "delta_median_abs_vs_base": 0.0016904589390550478,
      "frac_within_010_dex": 0.8620689655172413,
      "frac_within_015_dex": 0.9655172413793104,
      "gate_name": "sigma_star_source_gate",
      "k": 1.0,
      "max_abs_log10_error": 0.1964208566722057,
      "mean_abs_log10_error": 0.05342470607449316,
      "median_abs_log10_error": 0.043304358408409946,
      "n_above_020_dex": 0,
      "placement": "source",
      "target_A": 0.5580299705837988,
      "target_new_abs_log10_error": 0.16880451094353305,
      "target_new_log10_error": 0.16880451094353305,
      "xcol": "log10_Sigma_star",
      "xcrit": 7.043075821983066
    }
  ],
  "extreme_source_suppression_names": [
    "UGC07125"
  ],
  "governor_hypothesis": "BDVR coupling may require organized baryonic structure, not raw baryonic mass alone. Low surface density, low stellar fraction, or high gas fraction may suppress reservoir activation.",
  "interpretation_boundary": "M6g tests whether a reservoir-governor hypothesis is suggested by residual structure. It does not accept a new model term or retune BDVR.",
  "milestone": "CGHSTC-34-M6g",
  "n_extreme_source_suppression_A_lt_025": 1,
  "n_overpredicted_gt_010_dex": 2,
  "n_total": 87,
  "overpredicted_gt_010_names": [
    "NGC5371",
    "UGC07125"
  ],
  "status": "reservoir_governor_diagnostic_no_retuning",
  "target": {
    "A_Q_required": 0.3433363140664774,
    "A_source_required": 0.1178798245567548,
    "RHI_over_Rdisk": 6.816568047337278,
    "Sigma_baryon_Msun_kpc2": 104658682.36615317,
    "galaxy_name": "UGC07125",
    "gas_frac": 0.8195025137868931,
    "gas_participation_required_m5d": -0.0764093588523579,
    "log10_Sigma_baryon": 8.019775262749231,
    "log10_velocity_error": 0.2321401297980161,
    "participation_fraction_required_m5d": 0.1178798245567547,
    "sample_btfr_log10_v_residual": -0.23984685953499696,
    "star_frac": 0.1804974862131068,
    "stellar_to_gas_ratio": 0.2202525107324371
  },
  "top_correlations": {
    "A_Q_required": [
      {
        "abs_pearson_r": 0.8791484628736402,
        "abs_spearman_rho": 0.9003061894000146,
        "linear_intercept": 1.0038374391994402,
        "linear_slope": 3.7143485410150405,
        "n": 87,
        "pearson_r": 0.8791484628736402,
        "spearman_rho": 0.9003061894000146,
        "x_variable": "sample_btfr_log10_v_residual",
        "y_variable": "A_Q_required"
      },
      {
        "abs_pearson_r": 0.20568710961834177,
        "abs_spearman_rho": 0.2307173580228913,
        "linear_intercept": 2.0767693476869056,
        "linear_slope": -0.1351091967702598,
        "n": 87,
        "pearson_r": -0.20568710961834177,
        "spearman_rho": -0.2307173580228913,
        "x_variable": "log10_Sigma_gas",
        "y_variable": "A_Q_required"
      },
      {
        "abs_pearson_r": 0.14707164997150385,
        "abs_spearman_rho": 0.21689425938048365,
        "linear_intercept": 1.075219860299253,
        "linear_slope": -0.010578228781299394,
        "n": 87,
        "pearson_r": -0.14707164997150385,
        "spearman_rho": -0.21689425938048365,
        "x_variable": "RHI_over_Rdisk",
        "y_variable": "A_Q_required"
      },
      {
        "abs_pearson_r": 0.1953566566846359,
        "abs_spearman_rho": 0.20268657009495059,
        "linear_intercept": 2.372804027052315,
        "linear_slope": -1.0970426834788092,
        "n": 87,
        "pearson_r": -0.1953566566846359,
        "spearman_rho": -0.20268657009495059,
        "x_variable": "H_halo",
        "y_variable": "A_Q_required"
      },
      {
        "abs_pearson_r": 0.14648373329028375,
        "abs_spearman_rho": 0.20268657009495059,
        "linear_intercept": 1.08907671028603,
        "linear_slope": -0.02071554044242312,
        "n": 87,
        "pearson_r": -0.14648373329028375,
        "spearman_rho": -0.20268657009495059,
        "x_variable": "r_over_Rdisk_eval",
        "y_variable": "A_Q_required"
      },
      {
        "abs_pearson_r": 0.1940289432991171,
        "abs_spearman_rho": 0.19370124662827146,
        "linear_intercept": 1.6206163402053562,
        "linear_slope": -0.060981466704490624,
        "n": 87,
        "pearson_r": -0.1940289432991171,
        "spearman_rho": -0.19370124662827146,
        "x_variable": "log10_M_baryon_Msun",
        "y_variable": "A_Q_required"
      },
      {
        "abs_pearson_r": 0.11145729633311101,
        "abs_spearman_rho": 0.16866240183602185,
        "linear_intercept": 1.1938700028430815,
        "linear_slope": -0.15403552133102302,
        "n": 87,
        "pearson_r": -0.11145729633311101,
        "spearman_rho": -0.16866240183602185,
        "x_variable": "Q_eff",
        "y_variable": "A_Q_required"
      },
      {
        "abs_pearson_r": 0.1247374941721279,
        "abs_spearman_rho": 0.12085816805608528,
        "linear_intercept": 1.2937348228521834,
        "linear_slope": -0.271194326642893,
        "n": 87,
        "pearson_r": -0.1247374941721279,
        "spearman_rho": -0.12085816805608528,
        "x_variable": "S_internal",
        "y_variable": "A_Q_required"
      }
    ],
    "A_source_required": [
      {
        "abs_pearson_r": 0.8246481481368829,
        "abs_spearman_rho": 0.9003061894000146,
        "linear_intercept": 1.074310684658549,
        "linear_slope": 7.680580483597729,
        "n": 87,
        "pearson_r": 0.8246481481368829,
        "spearman_rho": 0.9003061894000146,
        "x_variable": "sample_btfr_log10_v_residual",
        "y_variable": "A_source_required"
      },
      {
        "abs_pearson_r": 0.20167504481625195,
        "abs_spearman_rho": 0.2307173580228913,
        "linear_intercept": 3.3934250789639133,
        "linear_slope": -0.2920350122447736,
        "n": 87,
        "pearson_r": -0.20167504481625195,
        "spearman_rho": -0.2307173580228913,
        "x_variable": "log10_Sigma_gas",
        "y_variable": "A_source_required"
      },
      {
        "abs_pearson_r": 0.13734744873500246,
        "abs_spearman_rho": 0.21689425938048365,
        "linear_intercept": 1.2212668562523206,
        "linear_slope": -0.021777574646412296,
        "n": 87,
        "pearson_r": -0.13734744873500246,
        "spearman_rho": -0.21689425938048365,
        "x_variable": "RHI_over_Rdisk",
        "y_variable": "A_source_required"
      },
      {
        "abs_pearson_r": 0.18410685010507258,
        "abs_spearman_rho": 0.20268657009495059,
        "linear_intercept": 3.918375604477641,
        "linear_slope": -2.2791356920696435,
        "n": 87,
        "pearson_r": -0.18410685010507258,
        "spearman_rho": -0.20268657009495059,
        "x_variable": "H_halo",
        "y_variable": "A_source_required"
      },
      {
        "abs_pearson_r": 0.1425913814907684,
        "abs_spearman_rho": 0.20268657009495059,
        "linear_intercept": 1.2572253503260928,
        "linear_slope": -0.044453408691154786,
        "n": 87,
        "pearson_r": -0.1425913814907684,
        "spearman_rho": -0.20268657009495059,
        "x_variable": "r_over_Rdisk_eval",
        "y_variable": "A_source_required"
      },
      {
        "abs_pearson_r": 0.1977737201333022,
        "abs_spearman_rho": 0.19370124662827146,
        "linear_intercept": 2.460225369821159,
        "linear_slope": -0.13702659103719508,
        "n": 87,
        "pearson_r": -0.1977737201333022,
        "spearman_rho": -0.19370124662827146,
        "x_variable": "log10_M_baryon_Msun",
        "y_variable": "A_source_required"
      },
      {
        "abs_pearson_r": 0.11846932939748599,
        "abs_spearman_rho": 0.16866240183602185,
        "linear_intercept": 1.5195878014849804,
        "linear_slope": -0.3609302085497027,
        "n": 87,
        "pearson_r": -0.11846932939748599,
        "spearman_rho": -0.16866240183602185,
        "x_variable": "Q_eff",
        "y_variable": "A_source_required"
      },
      {
        "abs_pearson_r": 0.12623482468337172,
        "abs_spearman_rho": 0.12085816805608528,
        "linear_intercept": 1.7210531610840758,
        "linear_slope": -0.6050171553658238,
        "n": 87,
        "pearson_r": -0.12623482468337172,
        "spearman_rho": -0.12085816805608528,
        "x_variable": "S_internal",
        "y_variable": "A_source_required"
      }
    ],
    "abs_log10_velocity_error": [
      {
        "abs_pearson_r": 0.25711919846300774,
        "abs_spearman_rho": 0.12460815047021942,
        "linear_intercept": 0.04572143797277043,
        "linear_slope": -0.14730388657914584,
        "n": 87,
        "pearson_r": -0.25711919846300774,
        "spearman_rho": -0.12460815047021942,
        "x_variable": "sample_btfr_log10_v_residual",
        "y_variable": "abs_log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.07222232317115986,
        "abs_spearman_rho": 0.1057188844108317,
        "linear_intercept": 0.08772692036868976,
        "linear_slope": -0.04098451004204679,
        "n": 87,
        "pearson_r": -0.07222232317115986,
        "spearman_rho": -0.1057188844108317,
        "x_variable": "S_star_gas",
        "y_variable": "abs_log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.13848027964789375,
        "abs_spearman_rho": 0.09745206677845009,
        "linear_intercept": 0.056145616933770924,
        "linear_slope": -0.017755474497912125,
        "n": 87,
        "pearson_r": -0.13848027964789375,
        "spearman_rho": -0.09745206677845009,
        "x_variable": "star_frac",
        "y_variable": "abs_log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.13848027964789372,
        "abs_spearman_rho": 0.09745206677845009,
        "linear_intercept": 0.038390142435858775,
        "linear_slope": 0.01775547449791223,
        "n": 87,
        "pearson_r": 0.13848027964789372,
        "spearman_rho": 0.09745206677845009,
        "x_variable": "gas_frac",
        "y_variable": "abs_log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.12850103054727424,
        "abs_spearman_rho": 0.09745206677845009,
        "linear_intercept": 0.04728645337123548,
        "linear_slope": -0.006965658471294324,
        "n": 87,
        "pearson_r": -0.12850103054727424,
        "spearman_rho": -0.09745206677845009,
        "x_variable": "log10_stellar_to_gas_ratio",
        "y_variable": "abs_log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.05742286951650786,
        "abs_spearman_rho": 0.09745206677845009,
        "linear_intercept": 0.04674926637188489,
        "linear_slope": -0.00021487975186267473,
        "n": 87,
        "pearson_r": -0.05742286951650786,
        "spearman_rho": -0.09745206677845009,
        "x_variable": "stellar_to_gas_ratio",
        "y_variable": "abs_log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.011387766357020674,
        "abs_spearman_rho": 0.08857539277791811,
        "linear_intercept": 0.0421326723509245,
        "linear_slope": 0.003357232355920557,
        "n": 87,
        "pearson_r": 0.011387766357020674,
        "spearman_rho": 0.08857539277791811,
        "x_variable": "S_internal",
        "y_variable": "abs_log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.13354308116778718,
        "abs_spearman_rho": 0.0839651527301888,
        "linear_intercept": 0.10214263820425919,
        "linear_slope": -0.006909370190695919,
        "n": 87,
        "pearson_r": -0.13354308116778718,
        "spearman_rho": -0.0839651527301888,
        "x_variable": "log10_Sigma_star",
        "y_variable": "abs_log10_velocity_error"
      }
    ],
    "log10_velocity_error": [
      {
        "abs_pearson_r": 0.906000935772257,
        "abs_spearman_rho": 0.9003061894000146,
        "linear_intercept": 0.006454327518613351,
        "linear_slope": -0.8485308849071332,
        "n": 87,
        "pearson_r": -0.906000935772257,
        "spearman_rho": -0.9003061894000146,
        "x_variable": "sample_btfr_log10_v_residual",
        "y_variable": "log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.195265160003953,
        "abs_spearman_rho": 0.2307173580228913,
        "linear_intercept": -0.2193376061240161,
        "linear_slope": 0.028432901053958973,
        "n": 87,
        "pearson_r": 0.195265160003953,
        "spearman_rho": 0.2307173580228913,
        "x_variable": "log10_Sigma_gas",
        "y_variable": "log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.1482147516524707,
        "abs_spearman_rho": 0.21689425938048365,
        "linear_intercept": -0.009492427236002446,
        "linear_slope": 0.0023631647332012905,
        "n": 87,
        "pearson_r": 0.1482147516524707,
        "spearman_rho": 0.21689425938048365,
        "x_variable": "RHI_over_Rdisk",
        "y_variable": "log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.19608113732298096,
        "abs_spearman_rho": 0.20268657009495059,
        "linear_intercept": -0.29813804727703425,
        "linear_slope": 0.24408984059800315,
        "n": 87,
        "pearson_r": 0.19608113732298096,
        "spearman_rho": 0.20268657009495059,
        "x_variable": "H_halo",
        "y_variable": "log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.1419873823842553,
        "abs_spearman_rho": 0.20268657009495059,
        "linear_intercept": -0.011861167270148836,
        "linear_slope": 0.004451180402917448,
        "n": 87,
        "pearson_r": 0.1419873823842553,
        "spearman_rho": 0.20268657009495059,
        "x_variable": "r_over_Rdisk_eval",
        "y_variable": "log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.17871024426096607,
        "abs_spearman_rho": 0.19370124662827146,
        "linear_intercept": -0.11947619753078147,
        "linear_slope": 0.012450860604755096,
        "n": 87,
        "pearson_r": 0.17871024426096607,
        "spearman_rho": 0.19370124662827146,
        "x_variable": "log10_M_baryon_Msun",
        "y_variable": "log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.09727156708070482,
        "abs_spearman_rho": 0.16866240183602185,
        "linear_intercept": -0.030309778617139616,
        "linear_slope": 0.029800041352435337,
        "n": 87,
        "pearson_r": 0.09727156708070482,
        "spearman_rho": 0.16866240183602185,
        "x_variable": "Q_eff",
        "y_variable": "log10_velocity_error"
      },
      {
        "abs_pearson_r": 0.1139172161100306,
        "abs_spearman_rho": 0.12085816805608528,
        "linear_intercept": -0.05223447104810718,
        "linear_slope": 0.054902424465642745,
        "n": 87,
        "pearson_r": 0.1139172161100306,
        "spearman_rho": 0.12085816805608528,
        "x_variable": "S_internal",
        "y_variable": "log10_velocity_error"
      }
    ]
  }
}

Outputs
-------
m6g_governor_diagnostics.csv
m6g_governor_correlations.csv
m6g_governor_grid_diagnostic.csv
m6g_summary.json
m6g_residual_vs_sigma_baryon.png
m6g_A_source_vs_sigma_baryon.png
m6g_A_source_vs_gas_frac.png
m6g_A_source_vs_star_frac.png
m6g_A_source_vs_btfr_residual.png

APS-facing language
-------------------
For external documentation, describe this as a Conformal Gravity Hilbert Space Time Current diagnostic.
Do not claim that the reservoir governor is established.
Phrase it as a testable hypothesis motivated by the retained outlier structure.
