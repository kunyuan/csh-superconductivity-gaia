# csh-superconductivity-gaia

Gaia knowledge package: Room-temperature superconductivity in a carbonaceous sulfur hydride (Snider et al., Nature 586, 373, 2020; RETRACTED 2022)

<!-- badges:start -->
<!-- badges:end -->

## Overview

> [!TIP]
> **Reasoning graph information gain: `0.7 bits`**
>
> Total mutual information between leaf premises and exported conclusions — measures how much the reasoning structure reduces uncertainty about the results.

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    resistance_observation["Zero Resistance at 287.7 K\n(0.85 → 0.68)"]:::premise
    susceptibility_observation["Diamagnetic Susceptibility Signal\n(0.80 → 0.12)"]:::premise
    field_suppression["Magnetic Field Suppression of Tc\n(0.80 → 0.79)"]:::premise
    isotope_effect_observed["13C Isotope Effect Claimed\n(0.75 → 0.74)"]:::premise
    original_sc_claim["★ Original Room-Temperature SC Claim\n(0.50 → 0.20)"]:::exported
    background_subtraction_fraud["Background Subtraction Fraud Analysis\n(0.95 → 0.85)"]:::premise
    susceptibility_data_invalid["★ Susceptibility Data Invalid\n(0.50 → 0.85)"]:::exported
    eremets_failed_replication["Eremets Group Failed Replication\n(0.90 → 0.81)"]:::premise
    goncharov_failed_replication["Goncharov Group Failed Replication\n(0.90 → 0.81)"]:::premise
    dias_broader_issues["Dias Group Broader Data Integrity Issues\n(0.92 → 0.85)"]:::premise
    rtsc_not_confirmed["★ Room-Temperature SC NOT Confirmed in C-S-H\n(0.50 → 0.78)"]:::exported
    data_integrity_failure["★ Data Processing Integrity Failures Identified\n(0.50 → 0.92)"]:::exported
    x["?\n(0.93 → 1.00)"]:::premise
    x["?\n(0.85 → 1.00)"]:::premise
    replication_failure["Independent Replication Failures\n(0.50 → 0.72)"]:::premise
    strat_0(["infer\n0.03 bits"]):::weak
    background_subtraction_fraud --> strat_0
    dias_broader_issues --> strat_0
    strat_0 --> susceptibility_data_invalid
    strat_1(["infer\n0.25 bits"]):::weak
    eremets_failed_replication --> strat_1
    goncharov_failed_replication --> strat_1
    susceptibility_data_invalid --> strat_1
    strat_1 --> rtsc_not_confirmed
    strat_2(["infer\n0.11 bits"]):::weak
    field_suppression --> strat_2
    isotope_effect_observed --> strat_2
    resistance_observation --> strat_2
    susceptibility_observation --> strat_2
    strat_2 --> original_sc_claim
    strat_3(["infer\n0.30 bits"]):::weak
    susceptibility_data_invalid --> strat_3
    strat_3 --> data_integrity_failure
    oper_0{{"⊗"}}:::contra
    susceptibility_data_invalid --- oper_0
    susceptibility_observation --- oper_0
    oper_0 --- ?
    oper_1{{"⊗"}}:::contra
    replication_failure --- oper_1
    original_sc_claim --- oper_1
    oper_1 --- ?

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| data_integrity_failure | The Snider et al. C-S-H paper exhibited data processing integrity failures: n... | 0.50 | 0.92 |
| original_sc_claim | Room-temperature superconductivity was achieved in a carbonaceous sulfur hydr... | 0.50 | 0.20 |
| rtsc_not_confirmed | Room-temperature superconductivity in the C-S-H system, as claimed by Snider ... | 0.50 | 0.78 |
| susceptibility_data_invalid | The magnetic susceptibility data in Snider et al. are unreliable and cannot b... | 0.50 | 0.85 |

<!-- content:start -->
<!-- content:end -->
