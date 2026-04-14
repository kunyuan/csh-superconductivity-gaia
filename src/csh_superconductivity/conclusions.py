"""Section 4: Conclusions — Post-Retraction Assessment

Exported conclusions reflecting the current scientific consensus after
the retraction. The key insight: the evidence chain for room-temperature
SC in C-S-H is broken because the susceptibility data are invalid.
"""

from gaia.lang import claim, deduction, support

from .experiment import original_sc_claim
from .retraction import (
    nature_retraction,
    replication_failure,
    resistance_still_open,
    susceptibility_data_invalid,
)

# ---------------------------------------------------------------------------
# Exported conclusion 1: Susceptibility data are invalid
# ---------------------------------------------------------------------------

# susceptibility_data_invalid is defined in retraction.py and re-exported

# ---------------------------------------------------------------------------
# Exported conclusion 2: Room-temperature SC NOT confirmed
# ---------------------------------------------------------------------------

rtsc_not_confirmed = claim(
    "Room-temperature superconductivity in the C-S-H system, as claimed by "
    "Snider et al., has NOT been confirmed. The magnetic susceptibility "
    "evidence — essential for establishing bulk SC — was shown to be "
    "unreliable. Two independent replication attempts failed. The paper "
    "was retracted by Nature. The resistance data alone are insufficient "
    "to establish the claim.",
    title="Room-Temperature SC NOT Confirmed in C-S-H",
)

deduction(
    premises=[susceptibility_data_invalid, replication_failure, nature_retraction],
    conclusion=rtsc_not_confirmed,
    reason=(
        "Three independent lines of evidence converge: (1) the susceptibility "
        "data are invalid (@susceptibility_data_invalid), removing the key "
        "evidence for bulk SC; (2) independent groups failed to replicate "
        "(@replication_failure); (3) Nature retracted the paper "
        "(@nature_retraction). Together these establish that room-temperature "
        "SC in C-S-H has not been confirmed."
    ),
    prior=0.95,
)

# ---------------------------------------------------------------------------
# Exported conclusion 3: Data integrity failure
# ---------------------------------------------------------------------------

data_integrity_failure = claim(
    "The Snider et al. C-S-H paper exhibited data processing integrity "
    "failures: non-standard background subtraction that statistical analysis "
    "suggests was reversed (adding rather than subtracting background), "
    "'raw' data that were not actually raw, and anomalies present at all "
    "measured pressures. These issues represent a fundamental breakdown "
    "in scientific data reporting.",
    title="Data Processing Integrity Failures Identified",
)

deduction(
    premises=[susceptibility_data_invalid, nature_retraction],
    conclusion=data_integrity_failure,
    reason=(
        "The detailed statistical analysis showing data fabrication "
        "(@susceptibility_data_invalid) was sufficiently convincing to "
        "trigger Nature's editorial retraction (@nature_retraction), "
        "confirming data integrity failures at the institutional level."
    ),
    prior=0.95,
)

# ---------------------------------------------------------------------------
# Exported conclusion 4: Lessons for hydride SC field
# ---------------------------------------------------------------------------

hydride_sc_caution = claim(
    "The C-S-H retraction demonstrates that extraordinary claims "
    "(room-temperature superconductivity) require extraordinary evidence "
    "with full methodological transparency. Magnetic susceptibility "
    "measurements in DAC are particularly vulnerable to background "
    "subtraction artifacts, and the field must demand: (1) publication of "
    "complete raw data, (2) standard and documented processing procedures, "
    "(3) independent replication before acceptance.",
    title="Lessons for Hydride SC Field",
)

deduction(
    premises=[data_integrity_failure, rtsc_not_confirmed],
    conclusion=hydride_sc_caution,
    reason=(
        "The data integrity failures (@data_integrity_failure) that led to "
        "the non-confirmation of room-temperature SC (@rtsc_not_confirmed) "
        "expose systemic vulnerabilities in how high-pressure SC claims are "
        "validated. The lesson is that extraordinary claims require "
        "extraordinary methodological rigor."
    ),
    prior=0.90,
)

# ---------------------------------------------------------------------------
# Context: What the original claim's status is now
# ---------------------------------------------------------------------------

support(
    premises=[rtsc_not_confirmed],
    conclusion=resistance_still_open,
    reason=(
        "While room-temperature SC is not confirmed (@rtsc_not_confirmed), "
        "the resistance data were not directly implicated in the fraud, "
        "leaving open the possibility that some SC exists in C-S-H — "
        "just not at room temperature, as the Eremets group found Tc ~ 200 K."
    ),
    prior=0.80,
)
