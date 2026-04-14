"""Section 2: Experimental Claims — Resistance, Susceptibility, Isotope Effect

The original experimental evidence presented in Snider et al. (2020).
These claims represent what was REPORTED in the paper; their validity
is challenged in the retraction module.
"""

from gaia.lang import claim, deduction, support

from .background import diamond_anvil_cell, photochemical_synthesis

# ---------------------------------------------------------------------------
# Claims — Resistance measurements (not directly implicated in retraction)
# ---------------------------------------------------------------------------

resistance_observation = claim(
    "Four-probe electrical resistance measurements in the DAC showed sharp "
    "drops to zero resistance at multiple pressures in the C-S-H system. "
    "The maximum transition temperature observed was Tc = 287.7 +/- 1.2 K "
    "(approximately 15 C) at 267 +/- 10 GPa — room temperature.",
    title="Zero Resistance at 287.7 K",
    figure="[Nature Fig. 1 — R(T) at multiple pressures]",
    caption=(
        "Fig. 1 | Electrical resistance as a function of temperature at "
        "multiple pressures showing superconducting transitions up to 287.7 K."
    ),
)

pressure_tc_relationship = claim(
    "The superconducting Tc in C-S-H spans the pressure range 140-275 GPa. "
    "Below 220 GPa, Tc values are moderate (~150-200 K). Above 220 GPa, "
    "there is a sharp upturn in Tc reaching 287.7 K at 267 GPa, attributed "
    "to a structural phase transition in the C-S-H compound.",
    title="P-Tc Phase Diagram with Sharp Upturn",
    figure="[Nature Fig. 3 — P-Tc phase diagram]",
    caption=(
        "Fig. 3 | Pressure-temperature phase diagram showing sharp Tc "
        "upturn above 220 GPa reaching room temperature at 267 GPa."
    ),
)

support(
    premises=[resistance_observation],
    conclusion=pressure_tc_relationship,
    reason=(
        "The pressure-Tc relationship is constructed from the collection of "
        "R(T) measurements at different pressures (@resistance_observation). "
        "The sharp upturn above 220 GPa suggests a structural transition "
        "enhancing superconductivity."
    ),
    prior=0.85,
)

# ---------------------------------------------------------------------------
# Claims — Magnetic susceptibility (THIS IS THE KEY RETRACTED DATA)
# ---------------------------------------------------------------------------

susceptibility_observation = claim(
    "AC magnetic susceptibility measurements up to 190 GPa reportedly showed "
    "a diamagnetic signal consistent with the Meissner effect at temperatures "
    "matching the resistance-determined Tc. This was presented as independent "
    "confirmation of bulk superconductivity in C-S-H.",
    title="Diamagnetic Susceptibility Signal",
    figure="[Nature Fig. 2a — ac susceptibility, RETRACTED DATA]",
    caption=(
        "Fig. 2a | AC magnetic susceptibility vs temperature at multiple "
        "pressures. THIS DATA was the primary target of the retraction due "
        "to non-standard background subtraction."
    ),
)

# ---------------------------------------------------------------------------
# Claims — Magnetic field suppression
# ---------------------------------------------------------------------------

field_suppression = claim(
    "Application of external magnetic fields suppressed the superconducting "
    "transition temperature, consistent with the expected behavior of a "
    "type-II superconductor. The upper critical field Hc2(0) was estimated "
    "from the field-dependent Tc measurements.",
    title="Magnetic Field Suppression of Tc",
    figure="[Nature Extended Data Fig. 5 — field dependence]",
    caption=(
        "Extended Data Fig. 5 | Temperature dependence of resistance at "
        "different magnetic fields showing Tc suppression."
    ),
)

# ---------------------------------------------------------------------------
# Claims — Isotope effect
# ---------------------------------------------------------------------------

isotope_effect_observed = claim(
    "Carbon-13 isotope substitution (13C for 12C) showed a shift in Tc "
    "that the authors claimed was consistent with the BCS isotope effect, "
    "suggesting phonon-mediated superconductivity with carbon phonon modes "
    "contributing to the pairing mechanism.",
    title="13C Isotope Effect Claimed",
    figure="[Nature Fig. 4 — isotope effect]",
    caption=(
        "Fig. 4 | Resistance measurements comparing 12C and 13C samples "
        "showing isotope shift in Tc."
    ),
)

# ---------------------------------------------------------------------------
# Combined evidence — Original SC claim
# ---------------------------------------------------------------------------

original_sc_evidence = claim(
    "The original paper presented four lines of evidence for room-temperature "
    "superconductivity in C-S-H: (1) zero resistance at 287.7 K, "
    "(2) diamagnetic susceptibility signal, (3) magnetic field suppression "
    "of Tc, and (4) 13C isotope effect. Together these were claimed to "
    "establish bulk superconductivity at room temperature.",
    title="Combined SC Evidence as Reported",
)

deduction(
    premises=[
        resistance_observation,
        susceptibility_observation,
        field_suppression,
        isotope_effect_observed,
    ],
    conclusion=original_sc_evidence,
    background=[diamond_anvil_cell],
    reason=(
        "The standard criteria for confirming superconductivity are: "
        "zero resistance, Meissner effect (diamagnetic susceptibility), "
        "and Tc suppression by magnetic field. The paper presented all "
        "three (@resistance_observation, @susceptibility_observation, "
        "@field_suppression), plus a 13C isotope effect (@isotope_effect_observed) "
        "as evidence for the BCS mechanism."
    ),
    prior=0.90,
)

# ---------------------------------------------------------------------------
# The original headline claim
# ---------------------------------------------------------------------------

original_sc_claim = claim(
    "Room-temperature superconductivity was achieved in a carbonaceous sulfur "
    "hydride (C-S-H) system at Tc = 287.7 +/- 1.2 K under 267 GPa, as "
    "reported by Snider et al. in Nature 586, 373 (2020). This would "
    "represent a major milestone — the first observation of superconductivity "
    "above room temperature.",
    title="Original Room-Temperature SC Claim",
)

deduction(
    premises=[original_sc_evidence, pressure_tc_relationship],
    conclusion=original_sc_claim,
    reason=(
        "If the combined experimental evidence for SC in C-S-H is valid "
        "(@original_sc_evidence) and the P-Tc diagram shows maximum Tc = 287.7 K "
        "(@pressure_tc_relationship), then room-temperature superconductivity "
        "has been achieved in this system."
    ),
    prior=0.90,
)
