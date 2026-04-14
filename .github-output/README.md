# csh-superconductivity-gaia

Gaia knowledge package: Room-temperature superconductivity in a carbonaceous sulfur hydride (Snider et al., Nature 586, 373, 2020; RETRACTED 2022)

<!-- badges:start -->
<!-- badges:end -->

## Overview

> [!TIP]
> **Reasoning graph information gain: `0.4 bits`**
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
    resistance_observation["★ Zero Resistance at 287.7 K\n(0.85 → 0.77)"]:::exported
    susceptibility_observation["★ Diamagnetic Susceptibility Signal\n(0.80 → 0.80)"]:::exported
    field_suppression["Magnetic Field Suppression of Tc\n(0.80 → 0.80)"]:::premise
    isotope_effect_observed["13C Isotope Effect\n(0.75 → 0.75)"]:::premise
    original_sc_evidence["★ Combined SC Evidence as Reported\n(0.50 → 0.68)"]:::exported
    room_temperature_sc["★ Room-Temperature Superconductivity in C-S-H\n(0.50 → 0.77)"]:::exported
    strat_0(["infer\n0.27 bits"]):::weak
    field_suppression --> strat_0
    isotope_effect_observed --> strat_0
    resistance_observation --> strat_0
    susceptibility_observation --> strat_0
    strat_0 --> original_sc_evidence
    strat_1(["infer\n0.15 bits"]):::weak
    original_sc_evidence --> strat_1
    resistance_observation --> strat_1
    strat_1 --> room_temperature_sc

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| original_sc_evidence | The original paper presented four lines of evidence for room-temperature supe... | 0.50 | 0.68 |
| resistance_observation | Four-probe electrical resistance measurements in the DAC showed sharp drops t... | 0.85 | 0.77 |
| room_temperature_sc | Room-temperature superconductivity was achieved in a carbonaceous sulfur hydr... | 0.50 | 0.77 |
| susceptibility_observation | AC magnetic susceptibility measurements up to 190 GPa showed a diamagnetic si... | 0.80 | 0.80 |

<!-- content:start -->
<!-- content:end -->
