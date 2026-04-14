# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Magnetic Field Suppression of Tc

1. **Diamagnetic Susceptibility Signal** (prior: 0.80 → belief: 0.12)
   - → supports: original_sc_claim, ?

2. **Zero Resistance at 287.7 K** (prior: 0.85 → belief: 0.68)
   - → supports: original_sc_claim

3. **13C Isotope Effect Claimed** (prior: 0.75 → belief: 0.74)
   - → supports: original_sc_claim

4. **Magnetic Field Suppression of Tc** (prior: 0.80 → belief: 0.79)
   - → supports: original_sc_claim

## Independent Replication Failures

5. **Independent Replication Failures** (prior: 0.50 → belief: 0.72)
   - → supports: ?

## Goncharov Group Failed Replication

6. **Eremets Group Failed Replication** (prior: 0.90 → belief: 0.81)
   - → supports: rtsc_not_confirmed

7. **Goncharov Group Failed Replication** (prior: 0.90 → belief: 0.81)
   - → supports: rtsc_not_confirmed

## Background Subtraction Fraud Analysis

8. **Dias Group Broader Data Integrity Issues** (prior: 0.92 → belief: 0.85)
   - → supports: susceptibility_data_invalid

9. **Background Subtraction Fraud Analysis** (prior: 0.95 → belief: 0.85)
   - → supports: susceptibility_data_invalid

## Original Room-Temperature SC Claim

10. **Original Room-Temperature SC Claim ★** (prior: 0.50 → belief: 0.20)
   - ← infer(field_suppression, isotope_effect_observed, resistance_observation, susceptibility_observation) [0.11 bits]
   - → supports: ?

## Susceptibility Data Invalid

11. **Susceptibility Data Invalid ★** (prior: 0.50 → belief: 0.85)
   - ← infer(background_subtraction_fraud, dias_broader_issues) [0.03 bits]
   - → supports: rtsc_not_confirmed, data_integrity_failure, ?

## Data Processing Integrity Failures Identified

12. **** (prior: 0.93 → belief: 1.00)

13. **Room-Temperature SC NOT Confirmed in C-S-H ★** (prior: 0.50 → belief: 0.78)
   - ← infer(eremets_failed_replication, goncharov_failed_replication, susceptibility_data_invalid) [0.25 bits]

14. **Data Processing Integrity Failures Identified ★** (prior: 0.50 → belief: 0.92)
   - ← infer(susceptibility_data_invalid) [0.30 bits]

## 

15. **** (prior: 0.85 → belief: 1.00)
