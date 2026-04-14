"""C-S-H Room-Temperature Superconductivity — Gaia Knowledge Package

Formalization of: Snider, E. et al. "Room-temperature superconductivity in
a carbonaceous sulfur hydride." Nature 586, 373-377 (2020).
DOI:10.1038/s41586-020-2801-z

**RETRACTED** by Nature on 26 September 2022.
Retraction note: DOI:10.1038/s41586-022-05294-9

This package formalizes the reasoning graph for the C-S-H room-temperature
superconductivity claim AND its retraction. It demonstrates how the evidence
chain breaks down when key data (magnetic susceptibility) are shown to be
unreliable through independent statistical analysis and failed replications.
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

# Section 2: Experimental Claims (as originally reported)
from .experiment import (
    field_suppression,
    isotope_effect_observed,
    original_sc_claim,
    original_sc_evidence,
    pressure_tc_relationship,
    resistance_observation,
    susceptibility_observation,
)

# Section 3: Retraction Evidence
from .retraction import (
    all_pressures_pathological,
    background_subtraction_fraud,
    dias_broader_issues,
    eremets_failed_replication,
    goncharov_failed_replication,
    isotope_questioned,
    nature_retraction,
    raw_data_not_raw,
    replication_failure,
    resistance_still_open,
    susceptibility_data_invalid,
)

# Section 4: Conclusions
from .conclusions import (
    data_integrity_failure,
    hydride_sc_caution,
    rtsc_not_confirmed,
)

# Exported conclusions — cross-package interface
__all__ = [
    "original_sc_claim",
    "susceptibility_data_invalid",
    "rtsc_not_confirmed",
    "data_integrity_failure",
]
