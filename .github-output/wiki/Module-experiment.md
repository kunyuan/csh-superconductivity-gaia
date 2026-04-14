# Module: experiment

### resistance_observation

**QID:** `github:csh_superconductivity::resistance_observation`
**Type:** claim
**Role:** independent
**Content:** Four-probe electrical resistance measurements in the DAC showed sharp drops to zero resistance at multiple pressures in the C-S-H system. The maximum transition temperature observed was Tc = 287.7 +/- 1.2 K (approximately 15 C) at 267 +/- 10 GPa — room temperature.
**Prior:** 0.85
**Belief:** 0.68
**figure:** [Nature Fig. 1 — R(T) at multiple pressures]
**caption:** Fig. 1 | Electrical resistance as a function of temperature at multiple pressures showing superconducting transitions up to 287.7 K.
**prior:** 0.85
**prior_justification:** Four-probe measurement in DAC, standard technique; but extraordinary claim warrants some skepticism.
**Referenced by:** support -> `github:csh_superconductivity::pressure_tc_relationship`; deduction -> `github:csh_superconductivity::original_sc_evidence`; support -> `github:csh_superconductivity::resistance_still_open`

### pressure_tc_relationship

**QID:** `github:csh_superconductivity::pressure_tc_relationship`
**Type:** claim
**Role:** derived
**Content:** The superconducting Tc in C-S-H spans the pressure range 140-275 GPa. Below 220 GPa, Tc values are moderate (~150-200 K). Above 220 GPa, there is a sharp upturn in Tc reaching 287.7 K at 267 GPa, attributed to a structural phase transition in the C-S-H compound.
**Belief:** 0.64
**Derived from:** support
**Premises:** `github:csh_superconductivity::resistance_observation`
**figure:** [Nature Fig. 3 — P-Tc phase diagram]
**caption:** Fig. 3 | Pressure-temperature phase diagram showing sharp Tc upturn above 220 GPa reaching room temperature at 267 GPa.
**gaia:** {'provenance': {'referenced_claims': ['resistance_observation']}}
**Referenced by:** deduction -> `github:csh_superconductivity::original_sc_claim`

### susceptibility_observation

**QID:** `github:csh_superconductivity::susceptibility_observation`
**Type:** claim
**Role:** independent
**Content:** AC magnetic susceptibility measurements up to 190 GPa reportedly showed a diamagnetic signal consistent with the Meissner effect at temperatures matching the resistance-determined Tc. This was presented as independent confirmation of bulk superconductivity in C-S-H.
**Prior:** 0.80
**Belief:** 0.12
**figure:** [Nature Fig. 2a — ac susceptibility, RETRACTED DATA]
**caption:** Fig. 2a | AC magnetic susceptibility vs temperature at multiple pressures. THIS DATA was the primary target of the retraction due to non-standard background subtraction.
**prior:** 0.8
**prior_justification:** AC susceptibility in DAC is complex; background subtraction introduces significant processing uncertainty.
**Referenced by:** deduction -> `github:csh_superconductivity::original_sc_evidence`; unknown -> `github:csh_superconductivity::_anon_000`

### field_suppression

**QID:** `github:csh_superconductivity::field_suppression`
**Type:** claim
**Role:** independent
**Content:** Application of external magnetic fields suppressed the superconducting transition temperature, consistent with the expected behavior of a type-II superconductor. The upper critical field Hc2(0) was estimated from the field-dependent Tc measurements.
**Prior:** 0.80
**Belief:** 0.79
**figure:** [Nature Extended Data Fig. 5 — field dependence]
**caption:** Extended Data Fig. 5 | Temperature dependence of resistance at different magnetic fields showing Tc suppression.
**prior:** 0.8
**prior_justification:** Standard magnetic field test, but depends on same DAC setup and sample quality as other measurements.
**Referenced by:** deduction -> `github:csh_superconductivity::original_sc_evidence`

### isotope_effect_observed

**QID:** `github:csh_superconductivity::isotope_effect_observed`
**Type:** claim
**Role:** independent
**Content:** Carbon-13 isotope substitution (13C for 12C) showed a shift in Tc that the authors claimed was consistent with the BCS isotope effect, suggesting phonon-mediated superconductivity with carbon phonon modes contributing to the pairing mechanism.
**Prior:** 0.75
**Belief:** 0.74
**figure:** [Nature Fig. 4 — isotope effect]
**caption:** Fig. 4 | Resistance measurements comparing 12C and 13C samples showing isotope shift in Tc.
**prior:** 0.75
**prior_justification:** 13C substitution is less conventional than H/D isotope effect; C phonon contribution to SC pairing is less established.
**Referenced by:** deduction -> `github:csh_superconductivity::original_sc_evidence`

### original_sc_evidence

**QID:** `github:csh_superconductivity::original_sc_evidence`
**Type:** claim
**Role:** derived
**Content:** The original paper presented four lines of evidence for room-temperature superconductivity in C-S-H: (1) zero resistance at 287.7 K, (2) diamagnetic susceptibility signal, (3) magnetic field suppression of Tc, and (4) 13C isotope effect. Together these were claimed to establish bulk superconductivity at room temperature.
**Belief:** 0.31
**Derived from:** deduction
**Premises:** `github:csh_superconductivity::resistance_observation`, `github:csh_superconductivity::susceptibility_observation`, `github:csh_superconductivity::field_suppression`, `github:csh_superconductivity::isotope_effect_observed`
**gaia:** {'provenance': {'referenced_claims': ['field_suppression', 'isotope_effect_observed', 'resistance_observation', 'susceptibility_observation']}}
**Referenced by:** deduction -> `github:csh_superconductivity::original_sc_claim`

### original_sc_claim

**QID:** `github:csh_superconductivity::original_sc_claim`
**Type:** claim
**Role:** derived
**Content:** Room-temperature superconductivity was achieved in a carbonaceous sulfur hydride (C-S-H) system at Tc = 287.7 +/- 1.2 K under 267 GPa, as reported by Snider et al. in Nature 586, 373 (2020). This would represent a major milestone — the first observation of superconductivity above room temperature.
**Belief:** 0.20
**Derived from:** deduction
**Premises:** `github:csh_superconductivity::original_sc_evidence`, `github:csh_superconductivity::pressure_tc_relationship`
**gaia:** {'provenance': {'referenced_claims': ['original_sc_evidence', 'pressure_tc_relationship']}}
**Referenced by:** unknown -> `github:csh_superconductivity::_anon_001`
