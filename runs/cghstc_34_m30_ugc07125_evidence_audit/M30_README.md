# M30 UGC07125 evidence audit

M30 audits the M29 failed/stalled interpretation of UGC07125. It is not another residual model and does not rescue M20-M28.

## Decision

`failed_stalled_supported_by_scalar_evidence_resolved_data_missing`

Meaning: scalar evidence supports keeping UGC07125 out of the juvenile-prototype class, but the decisive resolved evidence is still missing.

## What changed

A SPARC Rotmod radial rotation curve for UGC07125 was obtained from the SPARC Rotmod LTG archive. The outer curve is flat in this artifact:

- points: 13
- radial extent: 18.68 kpc
- outer mean Vobs: 65.22 km/s
- outer Vobs std: 0.24 km/s
- outer slope: -0.134 km/s/kpc

This strengthens the statement that UGC07125's severe mismatch is not simply because the SPARC radial curve is obviously non-flat. But Rotmod is not a 2D H I velocity-field or surface-density map, so it cannot establish nonparticipating gas.

## Claim boundary

UGC07125 remains provisional. Failed/stalled is the best current triage label, not an established physical explanation. True falsifier language is also premature until resolved H I/geometry checks are done.

## Highest-priority missing evidence

 priority                            gate_id                                requested_evidence                                                      why_it_matters
        1         resolved_hi_velocity_field               Obtain/locate 2D H I velocity field                   needed to test warp/asymmetry/settled-disk status
        2   hi_surface_density_participation      Obtain/locate H I column-density map/profile                        direct test of nonparticipating extended gas
        3            outer_curve_reliability          Audit original rotation-curve extraction SPARC Rotmod is flat, but side/asymmetry/inclination details matter
        4          star_formation_efficiency                Find SFR and H I/H2 depletion time     distinguishes gas-rich young disk from stalled inefficient disk
        5 stellar_population_age_metallicity       Find age/metallicity/color population proxy                  distinguishes truly young from long-stalled system
        6          environment_tidal_history Check companions/group/tidal/asymmetry literature                                 rules in/out disturbance quarantine
