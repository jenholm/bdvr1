# M66: CDS/SIMBAD Source-Table Extraction Scout

M66 is a source-table scout, not label validation. It uses the M65 object identities and OIDs to query SIMBAD/CDS bibliography and measurement-table records, then records which same-object source leads are ready for future manual or parser-based extraction.

## Outcome

- outcome_classification: `source_table_extraction_scout_not_label_validation`
- resolved objects queried: 21
- bibliography candidate rows: 21
- measurement table hit rows: 0
- source-table extraction candidate rows: 189
- unresolved source-table target rows: 36
- readiness status counts: {"object_unresolved_no_source_table_route": 36, "source_lead_ready_for_manual_extraction": 189}

## Claim boundary

No Tier A promotions were made. Bibliography rows and SIMBAD measurement-table rows are source leads only until a future branch extracts a concrete same-object target-label measurement, checks source provenance, and audits whether the measurement is direct, proxy, or inventory.

UGC07125 remains quarantined follow-up only, not a clean scalar object and not a juvenile prototype.

No M36 refit. No mature velocity-law change. No manuscript rewrite. No governor promotion. No endpoint-residual or A_inferred training.

## Next action

Use `m66_source_table_extraction_candidates.csv` as the queue for M67 source-specific extraction. Prioritize rows whose label family is H I asymmetry, A/R mismatch, warp / PA twist, centroid offset, or Vrot/sigma and whose source title points to resolved H I, velocity-field, or rotation-curve literature.
