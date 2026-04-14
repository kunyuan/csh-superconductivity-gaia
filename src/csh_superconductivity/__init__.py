"""C-S-H Room-Temperature Superconductivity — Gaia Knowledge Package

Formalization of: Snider, E. et al. "Room-temperature superconductivity in
a carbonaceous sulfur hydride." Nature 586, 373-377 (2020).
DOI:10.1038/s41586-020-2801-z

This package formalizes the internal reasoning of the original paper,
taken at face value. For post-publication critique and retraction analysis,
see the hirsch-csh-critique package.
"""

# Section 1: Background and Context
from .background import (
    bcs_theory,
    csh_design_rationale,
    diamond_anvil_cell,
    h3s_precedent,
    hydride_route_validated,
    lah10_precedent,
    main_question,
    photochemical_synthesis,
)

# Section 2: Experimental Claims
from .experiment import (
    field_suppression,
    isotope_effect_observed,
    original_sc_evidence,
    pressure_tc_relationship,
    resistance_observation,
    room_temperature_sc,
    susceptibility_observation,
)

# Exported conclusions — cross-package interface
__all__ = [
    "room_temperature_sc",
    "susceptibility_observation",
    "resistance_observation",
    "original_sc_evidence",
]
