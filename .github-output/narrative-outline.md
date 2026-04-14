# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Diamagnetic Susceptibility Signal

1. **13C Isotope Effect** (prior: 0.75 → belief: 0.75)
   - → supports: original_sc_evidence

2. **Magnetic Field Suppression of Tc** (prior: 0.80 → belief: 0.80)
   - → supports: original_sc_evidence

3. **Zero Resistance at 287.7 K ★** (prior: 0.85 → belief: 0.77)
   - → supports: original_sc_evidence, room_temperature_sc

4. **Diamagnetic Susceptibility Signal ★** (prior: 0.80 → belief: 0.80)
   - → supports: original_sc_evidence

## Combined SC Evidence as Reported

5. **Combined SC Evidence as Reported ★** (prior: 0.50 → belief: 0.68)
   - ← infer(field_suppression, isotope_effect_observed, resistance_observation, susceptibility_observation) [0.27 bits]
   - → supports: room_temperature_sc

## Room-Temperature Superconductivity in C-S-H

6. **Room-Temperature Superconductivity in C-S-H ★** (prior: 0.50 → belief: 0.77)
   - ← infer(original_sc_evidence, resistance_observation) [0.15 bits]
