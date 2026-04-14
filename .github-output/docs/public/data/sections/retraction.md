# Module: retraction

### background_subtraction_fraud

**QID:** `github:csh_superconductivity::background_subtraction_fraud`
**Type:** claim
**Role:** independent
**Content:** Van der Marel and Hirsch (arXiv:2201.07686, 2022) performed a detailed statistical analysis of the magnetic susceptibility data in Snider et al. Their key finding: the published data are compatible with a REVERSED procedure in which a background signal was ADDED to a predetermined superconducting-like result, rather than subtracted from raw measurements. The 'measured voltage' data presented as raw data appeared to be artificially constructed.
**Prior:** 0.95
**Belief:** 0.85
**prior:** 0.95
**prior_justification:** Detailed statistical analysis by van der Marel & Hirsch; peer-reviewed methodology, reproducible findings.
**Referenced by:** support -> `github:csh_superconductivity::all_pressures_pathological`; support -> `github:csh_superconductivity::raw_data_not_raw`; deduction -> `github:csh_superconductivity::susceptibility_data_invalid`

### all_pressures_pathological

**QID:** `github:csh_superconductivity::all_pressures_pathological`
**Type:** claim
**Role:** derived
**Content:** The van der Marel & Hirsch analysis found that background-corrected susceptibility data at ALL SIX measured pressures showed statistical anomalies. Four different proposed data-processing methods were evaluated; NONE could reproduce the published results from the supposedly raw data. This indicates systematic data fabrication rather than an isolated error.
**Belief:** 0.86
**Derived from:** support
**Premises:** `github:csh_superconductivity::background_subtraction_fraud`
**gaia:** {'provenance': {'referenced_claims': ['background_subtraction_fraud']}}
**Referenced by:** deduction -> `github:csh_superconductivity::susceptibility_data_invalid`

### raw_data_not_raw

**QID:** `github:csh_superconductivity::raw_data_not_raw`
**Type:** claim
**Role:** derived
**Content:** The 'measured voltage' data that Snider et al. presented as unprocessed raw measurements were shown by van der Marel & Hirsch to be NOT raw data. These data appear to have been artificially constructed, calling into question the fundamental integrity of the susceptibility measurements.
**Belief:** 0.84
**Derived from:** support
**Premises:** `github:csh_superconductivity::background_subtraction_fraud`
**gaia:** {'provenance': {'referenced_claims': ['background_subtraction_fraud']}}
**Referenced by:** deduction -> `github:csh_superconductivity::susceptibility_data_invalid`

### susceptibility_data_invalid

**QID:** `github:csh_superconductivity::susceptibility_data_invalid`
**Type:** claim
**Role:** derived
**Content:** The magnetic susceptibility data in Snider et al. are unreliable and cannot be used as evidence for superconductivity. The non-standard, user-defined background subtraction procedure was not specified in the paper, the data show statistical signatures of fabrication, and no valid processing method can reproduce the published results from the reported raw measurements.
**Belief:** 0.85
**Derived from:** deduction
**Premises:** `github:csh_superconductivity::background_subtraction_fraud`, `github:csh_superconductivity::all_pressures_pathological`, `github:csh_superconductivity::raw_data_not_raw`
**Derived from:** support
**Premises:** `github:csh_superconductivity::dias_broader_issues`
**gaia:** {'provenance': {'referenced_claims': ['all_pressures_pathological', 'background_subtraction_fraud', 'dias_broader_issues', 'raw_data_not_raw']}}
**Referenced by:** deduction -> `github:csh_superconductivity::nature_retraction`; support -> `github:csh_superconductivity::resistance_still_open`; deduction -> `github:csh_superconductivity::rtsc_not_confirmed`; deduction -> `github:csh_superconductivity::data_integrity_failure`; unknown -> `github:csh_superconductivity::_anon_000`

### github:csh_superconductivity::_anon_000

**QID:** `github:csh_superconductivity::_anon_000`
**Type:** claim
**Role:** structural
**Content:** not_both_true(A, B)
**Prior:** 0.93
**Belief:** 1.00
**helper_kind:** contradiction_result
**prior:** 0.93

### eremets_failed_replication

**QID:** `github:csh_superconductivity::eremets_failed_replication`
**Type:** claim
**Role:** independent
**Content:** The Eremets group at the Max Planck Institute spent 6 months attempting to replicate the C-S-H results. They observed superconductivity in some C-S-H samples only up to approximately 200 K — far below the claimed 287.7 K room-temperature Tc. This is consistent with conventional hydride superconductivity in the pressure range but NOT with the room-temperature claims.
**Prior:** 0.90
**Belief:** 0.81
**prior:** 0.9
**prior_justification:** 6-month effort by leading high-pressure SC group; partial SC observed but far below claimed Tc.
**Referenced by:** deduction -> `github:csh_superconductivity::replication_failure`

### goncharov_failed_replication

**QID:** `github:csh_superconductivity::goncharov_failed_replication`
**Type:** claim
**Role:** independent
**Content:** The Goncharov group at the Carnegie Institution could not synthesize any C-S-H compound undergoing the structural transition at the pressure claimed by Snider et al. They were unable to reproduce even the starting material conditions for the claimed room-temperature superconductor.
**Prior:** 0.90
**Belief:** 0.81
**prior:** 0.9
**prior_justification:** Expert group could not synthesize claimed compound; independent negative evidence.
**Referenced by:** deduction -> `github:csh_superconductivity::replication_failure`

### replication_failure

**QID:** `github:csh_superconductivity::replication_failure`
**Type:** claim
**Role:** derived
**Content:** Two independent expert groups (Eremets and Goncharov), both with extensive experience in high-pressure hydride superconductivity, failed to replicate the room-temperature Tc claimed by Snider et al. The Eremets group found Tc limited to ~200 K, and the Goncharov group could not even synthesize the claimed compound.
**Belief:** 0.72
**Derived from:** deduction
**Premises:** `github:csh_superconductivity::eremets_failed_replication`, `github:csh_superconductivity::goncharov_failed_replication`
**gaia:** {'provenance': {'referenced_claims': ['eremets_failed_replication', 'goncharov_failed_replication']}}
**Referenced by:** deduction -> `github:csh_superconductivity::rtsc_not_confirmed`; unknown -> `github:csh_superconductivity::_anon_001`

### github:csh_superconductivity::_anon_001

**QID:** `github:csh_superconductivity::_anon_001`
**Type:** claim
**Role:** structural
**Content:** not_both_true(A, B)
**Prior:** 0.85
**Belief:** 1.00
**helper_kind:** contradiction_result
**prior:** 0.85

### nature_retraction

**QID:** `github:csh_superconductivity::nature_retraction`
**Type:** claim
**Role:** derived
**Content:** Nature editors retracted Snider et al. on 26 September 2022, stating that the non-standard, user-defined background subtraction procedure used for the magnetic susceptibility data 'undermines confidence in the published magnetic susceptibility data as a whole.' The retraction was issued over the objections of the authors.
**Prior:** 0.99
**Belief:** 1.00
**Derived from:** deduction
**Premises:** `github:csh_superconductivity::susceptibility_data_invalid`
**prior:** 0.99
**prior_justification:** Official editorial retraction by Nature; highest level of formal invalidation.
**gaia:** {'provenance': {'referenced_claims': ['susceptibility_data_invalid']}}
**Referenced by:** deduction -> `github:csh_superconductivity::rtsc_not_confirmed`; deduction -> `github:csh_superconductivity::data_integrity_failure`

### dias_broader_issues

**QID:** `github:csh_superconductivity::dias_broader_issues`
**Type:** claim
**Role:** independent
**Content:** A subsequent paper by Ranga Dias's group claiming superconductivity in nitrogen-doped lutetium hydride (Nature 2023) was also retracted. Dias faced investigations for data integrity issues across multiple publications, establishing a pattern of questionable data practices.
**Prior:** 0.92
**Belief:** 0.85
**prior:** 0.92
**prior_justification:** Second retraction (lutetium hydride) plus institutional investigations; documented pattern.
**Referenced by:** support -> `github:csh_superconductivity::susceptibility_data_invalid`; support -> `github:csh_superconductivity::isotope_questioned`

### resistance_still_open

**QID:** `github:csh_superconductivity::resistance_still_open`
**Type:** claim
**Role:** derived
**Content:** The resistance measurements in Snider et al. were NOT directly implicated in the retraction, which focused on the susceptibility data. However, without independent susceptibility confirmation of bulk superconductivity, the resistance data alone are insufficient to establish room-temperature SC — zero resistance can have other explanations (filamentary paths, measurement artifacts).
**Belief:** 0.84
**Derived from:** support
**Premises:** `github:csh_superconductivity::resistance_observation`, `github:csh_superconductivity::susceptibility_data_invalid`
**Derived from:** support
**Premises:** `github:csh_superconductivity::rtsc_not_confirmed`
**gaia:** {'provenance': {'referenced_claims': ['resistance_observation', 'rtsc_not_confirmed', 'susceptibility_data_invalid']}}

### isotope_questioned

**QID:** `github:csh_superconductivity::isotope_questioned`
**Type:** claim
**Role:** derived
**Content:** The 13C isotope effect was not directly addressed in the retraction, but the broader data integrity concerns and Dias group's pattern of issues cast doubt on all data in the paper. The isotope effect alone, without reliable susceptibility data, provides only weak evidence.
**Belief:** 0.71
**Derived from:** support
**Premises:** `github:csh_superconductivity::dias_broader_issues`
**gaia:** {'provenance': {'referenced_claims': ['dias_broader_issues']}}
