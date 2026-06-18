# M37 Juvenile / Failed-System Governor Test Set

No manuscript rewrite was performed.

Mature/control rows are not the primary governor fitting set. They are used as a control check only.

The hybrid velocity endpoint is the M36 hybrid halo-energy BDVR no-governor endpoint.

## Selected model claim

test_set_constructed_governor_not_promoted

## Stage performance

taxonomy_stage,n,median_A_inferred,median_A_pred_M37,rmse_A,spearman_A,median_hybrid_velocity_abs_error
disturbed_or_measurement_contaminated,3,0.6433123110527825,0.7488772601347756,0.19060508947272428,1.0,0.0688587219551644
failed_stalled,5,0.5876019195241267,0.25495078361845136,0.3824788807176652,0.3,0.086732754937078
juvenile_forming,24,1.0,0.3785074292317147,0.5992407067349055,-0.13269099076359303,0.03435225461539585
mature_or_control,46,1.0,0.9245403170876312,0.16914819723332258,0.04397750629030859,0.0316077460430163
true_falsifier_candidate,9,0.6044754277243196,0.8396457371851015,0.3770802195900188,-0.5,0.0617213353931001


## Selected row

f_star_c,log10_sigma_c,f_gas_c,RHI_Rd_c,k_star,k_sigma,k_gas,k_HI,n_primary_fit,n_mature_control,primary_fit_rmse,primary_fit_spearman,mature_control_median_A_pred,mature_control_fraction_A_pred_gt_0p5,ugc07125_A_pred,rank_score,selected_model_claim
0.15,7.6,0.82,12.0,12.0,6.0,12.0,0.5,41,46,0.5117710280218453,-0.340956191201548,0.9245403170876312,0.9782608695652174,0.25495078361845136,0.5219997137578917,test_set_constructed_governor_not_promoted
