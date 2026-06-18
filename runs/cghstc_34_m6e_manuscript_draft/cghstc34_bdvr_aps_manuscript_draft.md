# A Bound-Domain Vacuum Response Model for SPARC Flat Rotation Velocities

Draft status: M6e manuscript scaffold

APS-facing expansion: Conformal Gravity Hilbert Space Time Current

Internal shorthand: CGHSTC

## Abstract

We present a phenomenological galaxy-sector response law motivated by the Conformal Gravity Hilbert Space Time Current framework. The model, called BDVR, interprets the dark-matter-like rotation signal as an effective bound-domain response of coherent galactic baryonic systems rather than as a freely tuned per-galaxy halo. The frozen implementation tested here combines a radial halo-shaped response envelope with observable baryonic-structure conditioning through stellar/gas composition and morphology. Using a SPARC quality-1 flat-velocity sample, we evaluate the frozen M4c response with no per-galaxy Q tuning, no retuning on the validation sample, and no outlier deletion. The frozen M4c model reaches a median absolute log10 velocity residual of 0.041613899469354995 dex on 87 galaxies, with 83 of 87 galaxies within 0.10 dex and 86 of 87 within 0.15 dex. Baseline and ablation comparisons show that radial halo activation and baryonic-structure conditioning improve the residual behavior relative to simpler forms. The leading residual object, UGC07125, is retained and treated as an external verification target for kinematic integrity, gas participation, and HI morphology rather than tuned away. We frame BDVR as a falsifiable galaxy-sector effective law, not as a complete replacement for dark matter or a first-principles derivation.

## 1. Introduction

Galaxy rotation curves remain one of the central empirical motivations for dark matter or modified gravitational dynamics. A successful phenomenological model must reproduce flat rotation behavior while avoiding excessive galaxy-by-galaxy freedom. The present work introduces BDVR as a galaxy-sector effective law motivated by the Conformal Gravity Hilbert Space Time Current framework.

The central idea is that bound coherent structures can couple to an underlying vacuum/time-current reservoir, while extended null propagation can remain nearly propagation-safe. In this paper we restrict attention to the galaxy sector and test whether a globally parameterized response law can reproduce SPARC flat-velocity behavior.

We do not claim a complete action-level derivation. The objective is narrower: define the effective response law, freeze its parameters, test it on a quality-controlled sample, compare it with baselines and ablations, and identify retained failure modes.

## 2. Conformal Gravity Hilbert Space Time Current sector picture

The parent framework distinguishes observational sectors. Propagation observables such as supernova, BAO, and CMB distances are treated as extended null or decohered paths that should remain nearly LCDM-safe. Local bound clocks and galaxies, by contrast, are treated as coherent bound domains that may couple to the time-current reservoir.

The sector hierarchy is:

```text
Conformal Gravity Hilbert Space Time Current
  propagation sector: SN / BAO / CMB nearly propagation-safe
  calibration sector: local bound-clock response
  galaxy sector: BDVR bound-domain vacuum response
```

In this paper, BDVR is the galaxy-sector realization of this idea.

## 3. BDVR effective law

The radial diagnostic acceleration form is

$$
a_{\rm obs}(r) = a_b(r) + a_{\rm BDVR}(r),
$$

with

$$
a_{\rm BDVR}(r) = Q_{\rm eff}(r,g)\sqrt{a_b(r)a_0}.
$$

The galaxy-sector response factor is

$$
Q_{\rm eff}(r,g) = Q_0 H(r/R_d) S_{\rm sg}(g) S_{\rm int}(g).
$$

The radial halo activation is

$$
H(r/R_d) = 1 + A_h \left[1 - \exp\left(-\frac{r}{k_h R_d}\right)\right].
$$

The stellar/gas structural factor is

$$
S_{\rm sg} = 1 + A_{\rm sg}\max\left[0, \log_{10}\left(\frac{M_*}{M_g}\right)-\log_{10}(5)\right].
$$

The morphology factor is

$$
S_{\rm int} = 1 + A_{\rm int}\max(0,5-T).
$$

For SPARC Table-1 flat-velocity comparisons we use

$$
v_{\rm flat}^{\rm BDVR} = \left(Q_{\rm eff}^2 G M_b a_0\right)^{1/4}.
$$

The adaptive radius enters only through $Q_{\rm eff}$. The SPARC flat-velocity comparison is not computed as $\sqrt{r a_{\rm total}}$.

## 4. Frozen parameter set

Table I lists the frozen parameter set used for the validation.

| parameter | value | description |\n| --- | --- | --- |\n| q_base | 0.9002495108803148 | Global baseline BDVR galaxy-sector response amplitude |\n| a0_m_s2 | 1.2e-10 | Reference acceleration scale |\n| halo_amplitude | 0.35 | Amplitude of radial halo activation |\n| halo_k | 3.0 | Halo scale length in units of Rdisk |\n| r_eval_mode | transition | Adaptive radius mode used to evaluate Q_eff |\n| velocity_mode | flat_response | Flat-response estimator for SPARC Table-1 Vflat |\n| r_eval_multiple | 4.0 | Fallback r_eval/Rdisk |\n| min_r_eval_multiple | 1.5 | Minimum clipped r_eval/Rdisk |\n| max_r_eval_multiple | 12.0 | Maximum clipped r_eval/Rdisk |\n| structural_mode | star_gas_hinge | Star/gas structural response mode |\n| structural_amplitude | 0.3 | Star/gas hinge amplitude |\n| star_gas_threshold | 5.0 | Threshold for stellar-to-gas ratio hinge |\n| internal_mode | early_type_hinge | Internal morphology response mode |\n| internal_amplitude | 0.1 | Early-type morphology hinge amplitude |\n| early_type_threshold | 5.0 | Morphological T threshold for early-type response |

## 5. Data and validation protocol

The validation uses a SPARC quality-1 sample with positive $V_{\rm flat}$, $L_{3.6}$, $M_{\rm HI}$, and $R_d$. The frozen model is evaluated with no per-galaxy $Q$ adjustment, no retuning on the validation sample, and no deletion of the leading outlier.

The stellar and gas masses are constructed as

$$
M_* = 0.5 L_{3.6} \times 10^9 M_\odot,
$$

and

$$
M_g = 1.33 M_{\rm HI} \times 10^9 M_\odot.
$$

## 6. Frozen M4c validation result

The frozen M4c validation summary is shown in Table II.

| metric | value | description |\n| --- | --- | --- |\n| n_galaxies | 87 | SPARC quality-1 galaxies in frozen M5 validation |\n| median_abs_log10_velocity_error | 0.041613899469354995 | Median absolute log10(pred/obs) |\n| mean_abs_log10_velocity_error | 0.04572143797277067 | Mean absolute log10(pred/obs) |\n| max_abs_log10_velocity_error | 0.23214012979801618 | Maximum absolute log10(pred/obs) |\n| median_velocity_ratio_pred_over_obs | 1.0215021046046753 | Median predicted/observed velocity ratio |\n| frac_within_010_dex | 0.9540229885057471 | Fraction within 0.10 dex |\n| frac_within_015_dex | 0.9885057471264368 | Fraction within 0.15 dex |\n| frac_within_020_dex | 0.9885057471264368 | Fraction within 0.20 dex |\n| n_within_010_dex | 83 | Count within 0.10 dex |\n| n_within_015_dex | 86 | Count within 0.15 dex |\n| n_within_020_dex | 86 | Count within 0.20 dex |\n| n_above_030_dex | 0 | Count above 0.30 dex |\n| strong_pass | False | Draft strong-pass gate |\n| soft_pass | True | Draft soft-pass gate |\n| fail | False | Draft fail gate |

In compact form, the model gives:

- \(n = 87\) galaxies
- median absolute log10 residual = `0.041613899469354995` dex
- mean absolute log10 residual = `0.04572143797277067` dex
- maximum absolute log10 residual = `0.23214012979801618` dex
- fraction within 0.10 dex = `0.9540229885057471`
- fraction within 0.15 dex = `0.9885057471264368`
- number above 0.30 dex = `0`

Figure 3 shows predicted versus observed flat velocities.

## 7. Baseline and ablation comparison

The baseline comparison evaluates Newtonian baryons, a simple BTFR/MOND-like estimator, scalar-Q, halo-only, halo plus star/gas, and full frozen M4c variants on the same sample.

Table III gives the comparison.

| model | n | median_abs_log10_velocity_error | mean_abs_log10_velocity_error | max_abs_log10_velocity_error | median_log10_velocity_error | median_velocity_ratio_pred_over_obs | frac_within_010_dex | frac_within_015_dex | frac_within_020_dex | n_above_020_dex | n_above_030_dex |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| newtonian_outer | 87 | 0.249744254895621 | 0.244855937569254 | 0.4488248070936664 | -0.249744254895621 | 0.5626725713839824 | 0.0689655172413793 | 0.2068965517241379 | 0.3448275862068966 | 57 | 31 |\n| mond_simple_btfr | 87 | 0.0472257873570313 | 0.0561133985763764 | 0.2052260404052944 | -0.039505288087067 | 0.913050317677887 | 0.8390804597701149 | 0.9655172413793104 | 0.9885057471264368 | 1 | 0 |\n| m3_scalar_q_only | 87 | 0.0641311041319905 | 0.069254645624326 | 0.2113536326710781 | -0.0623238410448768 | 0.8663156479085586 | 0.7586206896551724 | 0.896551724137931 | 0.9885057471264368 | 1 | 0 |\n| m4a_halo_only | 87 | 0.0416138994693549 | 0.0503710092326627 | 0.2321401297980161 | -0.0165283895662435 | 0.96265708260826 | 0.896551724137931 | 0.9770114942528736 | 0.9885057471264368 | 1 | 0 |\n| m4b_halo_star_gas | 87 | 0.0404458091376348 | 0.0464391851444796 | 0.2321401297980161 | -0.006183480835373 | 0.9858628900488806 | 0.9310344827586208 | 0.9885057471264368 | 0.9885057471264368 | 1 | 0 |\n| m4c_full_frozen | 87 | 0.0416138994693549 | 0.0457214379727706 | 0.2321401297980161 | 0.0092392657479627 | 1.0215021046046753 | 0.9540229885057472 | 0.9885057471264368 | 0.9885057471264368 | 1 | 0 |

The best median absolute residual is obtained by:

```json
{
  "frac_within_010_dex": 0.9310344827586208,
  "frac_within_015_dex": 0.9885057471264368,
  "frac_within_020_dex": 0.9885057471264368,
  "max_abs_log10_velocity_error": 0.2321401297980161,
  "mean_abs_log10_velocity_error": 0.0464391851444796,
  "mean_log10_velocity_error": -0.0068396929370829,
  "median_abs_log10_velocity_error": 0.0404458091376348,
  "median_log10_velocity_error": -0.006183480835373,
  "median_velocity_ratio_pred_over_obs": 0.9858628900488806,
  "model": "m4b_halo_star_gas",
  "n": 87,
  "n_above_010_dex": 6,
  "n_above_015_dex": 1,
  "n_above_020_dex": 1,
  "n_above_030_dex": 0,
  "n_within_010_dex": 81,
  "n_within_015_dex": 86,
  "n_within_020_dex": 86
}
```

The best fraction within 0.10 dex is obtained by:

```json
{
  "frac_within_010_dex": 0.9540229885057472,
  "frac_within_015_dex": 0.9885057471264368,
  "frac_within_020_dex": 0.9885057471264368,
  "max_abs_log10_velocity_error": 0.2321401297980161,
  "mean_abs_log10_velocity_error": 0.0457214379727706,
  "mean_log10_velocity_error": 0.0064543275186143,
  "median_abs_log10_velocity_error": 0.0416138994693549,
  "median_log10_velocity_error": 0.0092392657479627,
  "median_velocity_ratio_pred_over_obs": 1.0215021046046753,
  "model": "m4c_full_frozen",
  "n": 87,
  "n_above_010_dex": 4,
  "n_above_015_dex": 1,
  "n_above_020_dex": 1,
  "n_above_030_dex": 0,
  "n_within_010_dex": 83,
  "n_within_015_dex": 86,
  "n_within_020_dex": 86
}
```

This indicates that the M4b variant gives the slightly sharper median model, while M4c gives the broader 0.10-dex containment. We therefore treat M4c as the primary frozen validation form and M4b as an important ablation comparison.

## 8. Residual structure

Table IV summarizes the largest residual correlations by model class.

| model | variable | n | pearson_r | spearman_rho | linear_slope | abs_spearman_rho |\n| --- | --- | --- | --- | --- | --- | --- |\n| m3_scalar_q_only | stellar_to_gas_ratio | 87 | -0.4180715175228736 | -0.3770686010060508 | -0.0027541815249506 | 0.3770686010060508 |\n| m3_scalar_q_only | star_frac | 87 | -0.3865556337272846 | -0.3770686010060508 | -0.0872544801363712 | 0.3770686010060508 |\n| m3_scalar_q_only | gas_frac | 87 | 0.3865556337272844 | 0.3770686010060508 | 0.0872544801363712 | 0.3770686010060508 |\n| m3_scalar_q_only | v_flat_obs_km_s | 87 | -0.4210250832412153 | -0.3769956987679521 | -0.000354072541395 | 0.3769956987679521 |\n| m3_scalar_q_only | S_star_gas | 87 | -0.3952560403926445 | -0.3732981786635803 | -0.3948736791254579 | 0.3732981786635803 |\n| m4a_halo_only | S_star_gas | 87 | -0.4249079223320385 | -0.380005563292039 | -0.4338945321462296 | 0.380005563292039 |\n| m4a_halo_only | stellar_to_gas_ratio | 87 | -0.4440075043824109 | -0.3674272800174964 | -0.0029897988361787 | 0.3674272800174964 |\n| m4a_halo_only | star_frac | 87 | -0.3830924939907245 | -0.3674272800174964 | -0.0883871334649418 | 0.3674272800174964 |\n| m4a_halo_only | gas_frac | 87 | 0.3830924939907245 | 0.3674272800174964 | 0.0883871334649417 | 0.3674272800174964 |\n| m4a_halo_only | v_flat_obs_km_s | 87 | -0.412096218969169 | -0.3592440037909163 | -0.0003542359108042 | 0.3592440037909163 |\n| m4b_halo_star_gas | v_flat_obs_km_s | 87 | -0.3361339688412489 | -0.3054057009550193 | -0.0002702548904797 | 0.3054057009550193 |\n| m4b_halo_star_gas | star_frac | 87 | -0.3008954648012146 | -0.2836261573230298 | -0.0649334159791209 | 0.2836261573230298 |\n| m4b_halo_star_gas | gas_frac | 87 | 0.3008954648012145 | 0.2836261573230298 | 0.0649334159791209 | 0.2836261573230298 |\n| m4b_halo_star_gas | stellar_to_gas_ratio | 87 | -0.2839074215403102 | -0.2836261573230298 | -0.0017881156562029 | 0.2836261573230298 |\n| m4b_halo_star_gas | S_star_gas | 87 | -0.2506824918522772 | -0.2649774973683998 | -0.2394310962757869 | 0.2649774973683998 |\n| m4c_full_frozen | M_gas_Msun | 87 | 0.1876781753651001 | 0.3301772451952833 | 9.826288659189004e-13 | 0.3301772451952833 |\n| m4c_full_frozen | RHI | 87 | 0.2265959609164128 | 0.3198461735271609 | 0.0008746398046024 | 0.3198461735271609 |\n| m4c_full_frozen | H_halo | 87 | 0.196081137322981 | 0.2026865700949505 | 0.2440898405980032 | 0.2026865700949505 |\n| m4c_full_frozen | r_over_Rdisk_eval | 87 | 0.1419873823842553 | 0.2026865700949505 | 0.0044511804029174 | 0.2026865700949505 |\n| m4c_full_frozen | Reff | 87 | 0.117567792112308 | 0.1954826922094617 | 0.0024987011595632 | 0.1954826922094617 |\n| mond_simple_btfr | stellar_to_gas_ratio | 87 | -0.4180715175228737 | -0.3770686010060508 | -0.0027541815249506 | 0.3770686010060508 |\n| mond_simple_btfr | gas_frac | 87 | 0.3865556337272846 | 0.3770686010060508 | 0.0872544801363712 | 0.3770686010060508 |\n| mond_simple_btfr | star_frac | 87 | -0.3865556337272844 | -0.3770686010060508 | -0.0872544801363712 | 0.3770686010060508 |\n| mond_simple_btfr | v_flat_obs_km_s | 87 | -0.4210250832412153 | -0.3769956987679521 | -0.000354072541395 | 0.3769956987679521 |\n| mond_simple_btfr | S_star_gas | 87 | -0.3952560403926444 | -0.3732981786635803 | -0.3948736791254579 | 0.3732981786635803 |\n| newtonian_outer | log10_M_baryon_Msun | 87 | 0.6373356740777045 | 0.6520922942334328 | 0.0783836172088103 | 0.6520922942334328 |\n| newtonian_outer | M_baryon_Msun | 87 | 0.5059643829279826 | 0.6520922942334328 | 7.804457460434403e-13 | 0.6520922942334328 |\n| newtonian_outer | star_frac | 87 | 0.6092332384405329 | 0.6501786104833418 | 0.2254210139397219 | 0.6501786104833418 |\n| newtonian_outer | gas_frac | 87 | -0.6092332384405329 | -0.6501786104833418 | -0.2254210139397222 | 0.6501786104833418 |\n| newtonian_outer | stellar_to_gas_ratio | 87 | 0.3947929098126875 | 0.6501786104833418 | 0.0042633050202645 | 0.6501786104833418 |

The residual-correlation diagnostics are used as structure tests rather than as new tuning inputs. In the current results, earlier baselines show stronger residual structure tied to stellar/gas composition, morphology, and velocity scale, while the full frozen response suppresses several of those trends.

## 9. Retained outlier and verification target

UGC07125 is retained in all metrics and is not tuned away. It is the leading residual object.

For UGC07125, the M5d inversion gives:

```json
{
  "M_baryon_Msun": 7512569999.999999,
  "M_gas_Msun": 6156569999.999999,
  "M_part_required_Msun": 885580433.570339,
  "M_star_Msun": 1356000000.0,
  "RHI_over_Rdisk": 6.816568047337278,
  "T": 9.0,
  "galaxy_name": "UGC07125",
  "gas_frac": 0.8195025137868931,
  "gas_participation_required": -0.0764093588523579,
  "gas_participation_required_status": "stellar_mass_alone_exceeds_required_participating_mass",
  "log10_velocity_error": 0.2321401297980161,
  "participation_fraction_required": 0.11787982455675476,
  "stellar_to_gas_ratio": 0.2202525107324371,
  "v_flat_obs_km_s": 65.2,
  "v_m5_bdvr_km_s": 111.27246923349932
}
```

This object is interpreted as a verification target rather than a resolved case. The required participating mass is substantially below its catalogued baryonic mass and even below its nominal stellar mass estimate. Therefore the appropriate next checks are external: resolved HI kinematics, inclination and warp reliability, approaching/receding asymmetry, gas surface-density structure, and mass-estimate systematics.

## 10. Discussion

The current result supports BDVR as a nontrivial galaxy-sector effective law inside the Conformal Gravity Hilbert Space Time Current framework. The model is not a complete replacement for dark matter and is not a full rotation-curve fit. Its significance is that a frozen globally parameterized response law produces competitive flat-velocity residuals and meaningful retained failure modes.

The main theoretical task is to derive $Q_0$, $H$, $S_{\rm sg}$, $S_{\rm int}$, and $a_0$ from deeper bound-domain current variables rather than treating them as effective phenomenological factors.

## 11. Conclusions

We have defined BDVR as a galaxy-sector response law motivated by Conformal Gravity Hilbert Space Time Current bound-domain coupling. In frozen validation on a SPARC quality-1 flat-velocity sample, the model achieves low residuals without per-galaxy Q tuning. Baseline and ablation comparisons show that radial halo activation and baryonic-structure conditioning are not merely decorative terms; they alter the residual behavior relative to simpler baselines. The leading residual object, UGC07125, is retained as a verification target and motivates external kinematic checks.

## Appendix A. UGC07125

See `appendix_table_ugc07125.csv` and `appendix_table_ugc07125_hard_analogs.csv` in the M6 paper artifacts package.

## Appendix B. Reproducibility

The M6 artifact package records source file paths and hashes in `m6_source_artifacts_manifest.json`. The manuscript draft uses gathered outputs from M5 through M5d and introduces no new model logic.

## References placeholder

- SPARC data paper: TODO
- MOND / BTFR reference: TODO
- Conformal Gravity Hilbert Space Time Current internal formulation memo: TODO
- Logarithmic BEC dark matter comparison paper: TODO
- UGC07125 / SN 2020qmp / HI morphology references: TODO
