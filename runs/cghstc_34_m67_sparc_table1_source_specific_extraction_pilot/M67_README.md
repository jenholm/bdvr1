# M67: SPARC Table-1 Source-Specific Extraction Pilot

M67 is source-specific extraction, not Tier A validation. It joins the M65/M66 minimum-pool acquisition targets to the local SPARC Table-1 rich-input schema and extracts only fields that are actually present in that source.

## Outcome

- outcome_classification: `sparc_table1_source_specific_extraction_not_tier_a_validation`
- minimum-pool objects: 25
- SPARC-crossmatched objects: 25
- same-object external morphology candidates: 25
- context/inventory measurement rows: 175
- unsupported/unresolved extraction target rows: 200

## Claim boundary

External morphology is direct same-object morphology, not map-level dynamics. SPARC `T` can support external morphology only; it does not supply H I asymmetry, A/R mismatch, lopsidedness, centroid offset, burstiness, SFE/depletion, or warp/PA twist.

SPARC Vflat is not Vrot/sigma because the sigma component is absent. SPARC RHI/Rdisk is H I extent context/inventory, not H I asymmetry or lopsidedness.

No Tier A promotions were made. UGC07125 remains quarantined. No M36 refit. No mature velocity-law change. No manuscript rewrite. No governor promotion. No endpoint-residual or A_inferred training.

## Next action

M68 should target the unresolved M67 rows with real source-specific H I or velocity-field literature extraction, especially for H I asymmetry, A/R mismatch, warp/PA twist, centroid offset, and Vrot/sigma. Each future promotion candidate must carry source title/year/URL or bibcode, extracted field/value, extraction note, and direct/proxy/inventory classification.
