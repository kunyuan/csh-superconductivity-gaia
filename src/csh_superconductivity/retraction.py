"""Section 3: Retraction Evidence — Data Integrity Failures

This is the critical module: it formalizes the evidence that led to
the retraction of Snider et al. (2020) by Nature on 26 September 2022.

The key findings are:
1. Van der Marel & Hirsch analysis showing background subtraction fraud
2. Failed replication attempts by Eremets and Goncharov groups
3. Nature's editorial retraction
4. Broader data integrity concerns with Dias group publications
"""

from gaia.lang import claim, contradiction, deduction, support

from .experiment import (
    original_sc_claim,
    resistance_observation,
    susceptibility_observation,
)

# ---------------------------------------------------------------------------
# Claims — Van der Marel & Hirsch analysis (arXiv:2201.07686)
# ---------------------------------------------------------------------------

background_subtraction_fraud = claim(
    "Van der Marel and Hirsch (arXiv:2201.07686, 2022) performed a detailed "
    "statistical analysis of the magnetic susceptibility data in Snider et al. "
    "Their key finding: the published data are compatible with a REVERSED "
    "procedure in which a background signal was ADDED to a predetermined "
    "superconducting-like result, rather than subtracted from raw measurements. "
    "The 'measured voltage' data presented as raw data appeared to be "
    "artificially constructed.",
    title="Background Subtraction Fraud Analysis",
)

all_pressures_pathological = claim(
    "The van der Marel & Hirsch analysis found that background-corrected "
    "susceptibility data at ALL SIX measured pressures showed statistical "
    "anomalies. Four different proposed data-processing methods were "
    "evaluated; NONE could reproduce the published results from the "
    "supposedly raw data. This indicates systematic data fabrication "
    "rather than an isolated error.",
    title="All Six Pressures Show Pathological Data",
)

support(
    premises=[background_subtraction_fraud],
    conclusion=all_pressures_pathological,
    reason=(
        "If the background subtraction procedure was reversed (adding rather "
        "than subtracting), as the analysis suggests (@background_subtraction_fraud), "
        "then the anomalies should appear at every pressure where the same "
        "procedure was applied — which is exactly what was found."
    ),
    prior=0.92,
)

raw_data_not_raw = claim(
    "The 'measured voltage' data that Snider et al. presented as unprocessed "
    "raw measurements were shown by van der Marel & Hirsch to be NOT raw "
    "data. These data appear to have been artificially constructed, calling "
    "into question the fundamental integrity of the susceptibility "
    "measurements.",
    title="Raw Data Are Not Raw",
)

support(
    premises=[background_subtraction_fraud],
    conclusion=raw_data_not_raw,
    reason=(
        "The statistical analysis revealing reversed background subtraction "
        "(@background_subtraction_fraud) implies that what were presented as "
        "raw measurements were actually derived from the predetermined result "
        "by adding (not subtracting) a background — making the 'raw' data "
        "a fabricated intermediate."
    ),
    prior=0.90,
)

# ---------------------------------------------------------------------------
# Susceptibility data invalidated
# ---------------------------------------------------------------------------

susceptibility_data_invalid = claim(
    "The magnetic susceptibility data in Snider et al. are unreliable and "
    "cannot be used as evidence for superconductivity. The non-standard, "
    "user-defined background subtraction procedure was not specified in the "
    "paper, the data show statistical signatures of fabrication, and no "
    "valid processing method can reproduce the published results from the "
    "reported raw measurements.",
    title="Susceptibility Data Invalid",
)

deduction(
    premises=[background_subtraction_fraud, all_pressures_pathological, raw_data_not_raw],
    conclusion=susceptibility_data_invalid,
    reason=(
        "Three independent findings — reversed background procedure "
        "(@background_subtraction_fraud), anomalies at all pressures "
        "(@all_pressures_pathological), and fabricated raw data "
        "(@raw_data_not_raw) — establish beyond reasonable doubt that the "
        "susceptibility data are unreliable."
    ),
    prior=0.95,
)

# Contradiction: susceptibility data invalid vs original susceptibility claim
contradiction(
    susceptibility_data_invalid,
    susceptibility_observation,
    reason=(
        "The demonstrated invalidity of the susceptibility data "
        "(@susceptibility_data_invalid) — with reversed background subtraction, "
        "anomalies at all pressures, and fabricated raw data — directly "
        "contradicts the reliability of the diamagnetic signal reported in the "
        "original paper (@susceptibility_observation)."
    ),
    prior=0.93,
)

# ---------------------------------------------------------------------------
# Claims — Failed replication attempts
# ---------------------------------------------------------------------------

eremets_failed_replication = claim(
    "The Eremets group at the Max Planck Institute spent 6 months attempting "
    "to replicate the C-S-H results. They observed superconductivity in "
    "some C-S-H samples only up to approximately 200 K — far below the "
    "claimed 287.7 K room-temperature Tc. This is consistent with "
    "conventional hydride superconductivity in the pressure range but "
    "NOT with the room-temperature claims.",
    title="Eremets Group Failed Replication",
)

goncharov_failed_replication = claim(
    "The Goncharov group at the Carnegie Institution could not synthesize "
    "any C-S-H compound undergoing the structural transition at the "
    "pressure claimed by Snider et al. They were unable to reproduce "
    "even the starting material conditions for the claimed "
    "room-temperature superconductor.",
    title="Goncharov Group Failed Replication",
)

replication_failure = claim(
    "Two independent expert groups (Eremets and Goncharov), both with "
    "extensive experience in high-pressure hydride superconductivity, "
    "failed to replicate the room-temperature Tc claimed by Snider et al. "
    "The Eremets group found Tc limited to ~200 K, and the Goncharov "
    "group could not even synthesize the claimed compound.",
    title="Independent Replication Failures",
)

deduction(
    premises=[eremets_failed_replication, goncharov_failed_replication],
    conclusion=replication_failure,
    reason=(
        "Two independent failures to replicate — one achieving only Tc ~ 200 K "
        "(@eremets_failed_replication) and the other unable to synthesize the "
        "compound at all (@goncharov_failed_replication) — constitute strong "
        "negative evidence against the room-temperature SC claim."
    ),
    prior=0.90,
)

# Contradiction: replication failure vs original SC claim
contradiction(
    replication_failure,
    original_sc_claim,
    reason=(
        "If room-temperature SC in C-S-H were real, expert groups with "
        "extensive high-pressure experience should be able to reproduce it. "
        "Two independent failures (@replication_failure) — one finding "
        "Tc limited to ~200 K and the other unable to even make the compound — "
        "directly contradict the original claim."
    ),
    prior=0.85,
)

# ---------------------------------------------------------------------------
# Claims — Nature's official retraction
# ---------------------------------------------------------------------------

nature_retraction = claim(
    "Nature editors retracted Snider et al. on 26 September 2022, stating "
    "that the non-standard, user-defined background subtraction procedure "
    "used for the magnetic susceptibility data 'undermines confidence in the "
    "published magnetic susceptibility data as a whole.' The retraction was "
    "issued over the objections of the authors.",
    title="Nature Editorial Retraction",
)

deduction(
    premises=[susceptibility_data_invalid],
    conclusion=nature_retraction,
    reason=(
        "The established invalidity of the susceptibility data "
        "(@susceptibility_data_invalid) provided sufficient grounds for Nature "
        "to retract the paper. An editorial retraction from Nature represents "
        "the highest level of formal invalidation of published results."
    ),
    prior=0.99,
)

# ---------------------------------------------------------------------------
# Claims — Broader data integrity context
# ---------------------------------------------------------------------------

dias_broader_issues = claim(
    "A subsequent paper by Ranga Dias's group claiming superconductivity in "
    "nitrogen-doped lutetium hydride (Nature 2023) was also retracted. Dias "
    "faced investigations for data integrity issues across multiple "
    "publications, establishing a pattern of questionable data practices.",
    title="Dias Group Broader Data Integrity Issues",
)

support(
    premises=[dias_broader_issues],
    conclusion=susceptibility_data_invalid,
    reason=(
        "A pattern of data integrity issues across multiple Dias group "
        "publications (@dias_broader_issues) increases the prior probability "
        "that the C-S-H susceptibility data were also unreliable."
    ),
    prior=0.80,
)

# ---------------------------------------------------------------------------
# What remains of the evidence after retraction
# ---------------------------------------------------------------------------

resistance_still_open = claim(
    "The resistance measurements in Snider et al. were NOT directly "
    "implicated in the retraction, which focused on the susceptibility data. "
    "However, without independent susceptibility confirmation of bulk "
    "superconductivity, the resistance data alone are insufficient to "
    "establish room-temperature SC — zero resistance can have other "
    "explanations (filamentary paths, measurement artifacts).",
    title="Resistance Data Not Directly Retracted But Insufficient",
)

support(
    premises=[resistance_observation, susceptibility_data_invalid],
    conclusion=resistance_still_open,
    reason=(
        "The resistance measurements (@resistance_observation) were not the "
        "target of the retraction analysis, but with the susceptibility data "
        "invalidated (@susceptibility_data_invalid), the resistance alone "
        "cannot establish bulk superconductivity."
    ),
    prior=0.85,
)

isotope_questioned = claim(
    "The 13C isotope effect was not directly addressed in the retraction, "
    "but the broader data integrity concerns and Dias group's pattern of "
    "issues cast doubt on all data in the paper. The isotope effect alone, "
    "without reliable susceptibility data, provides only weak evidence.",
    title="Isotope Effect Questioned by Context",
)

support(
    premises=[dias_broader_issues],
    conclusion=isotope_questioned,
    reason=(
        "The pattern of data integrity failures across Dias group publications "
        "(@dias_broader_issues) creates reasonable doubt about all measurements "
        "in the paper, including the isotope effect."
    ),
    prior=0.75,
)
