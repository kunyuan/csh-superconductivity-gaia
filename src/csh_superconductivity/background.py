"""Section 1: Background — Hydride Superconductivity Context

Establishes the high-pressure hydride superconductivity precedents (H3S, LaH10),
the chemical design rationale for C-S-H, and the synthesis approach used in the
Snider et al. study.
"""

from gaia.lang import claim, deduction, question, setting, support

from h3s_superconductivity import hydrogen_materials_prospect
from lah10_superconductivity import rtsc_prospect

# ---------------------------------------------------------------------------
# Settings — established prior discoveries
# ---------------------------------------------------------------------------

bcs_theory = setting(
    "Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron "
    "attraction leads to Cooper pairing. The Eliashberg formulation places no "
    "apparent upper bound on Tc. High Tc requires: (1) high-frequency phonons, "
    "(2) strong electron-phonon coupling, (3) high electronic density of states.",
    title="BCS Theory",
)

diamond_anvil_cell = setting(
    "Diamond anvil cell (DAC) enables static high-pressure experiments up to "
    "hundreds of GPa. Four-probe resistance measurements and ac magnetic "
    "susceptibility measurements can be performed in situ. Samples are "
    "typically ~10 um in diameter.",
    title="Diamond Anvil Cell Technique",
)

# ---------------------------------------------------------------------------
# Claims — Prior hydride results motivate further search
# ---------------------------------------------------------------------------

hydride_route_validated = claim(
    "The discoveries of H3S at 203 K and LaH10 at 250 K established that "
    "hydrogen-rich compounds under extreme pressure can achieve very high "
    "superconducting Tc via the conventional BCS mechanism. This validated "
    "the hydride route and motivated searches for even higher Tc by "
    "chemical tuning.",
    title="Hydride SC Route Validated by H3S and LaH10",
)

deduction(
    premises=[hydrogen_materials_prospect, rtsc_prospect],
    conclusion=hydride_route_validated,
    background=[bcs_theory],
    reason=(
        "The H3S discovery established that hydrogen-rich materials are "
        "high-Tc superconductors (@hydrogen_materials_prospect), and the "
        "LaH10 result showed room-temperature SC appears achievable "
        "(@rtsc_prospect). Together, these validated the hydride route "
        "and motivated further chemical exploration."
    ),
    prior=0.95,
)

# ---------------------------------------------------------------------------
# Claims — Chemical design rationale for C-S-H
# ---------------------------------------------------------------------------

csh_design_rationale = claim(
    "The C-S-H system was targeted by mixing methane (CH4) into the H2S + H2 "
    "precursor mixture for H3S at low pressures. The rationale was that "
    "molecular exchange within the van der Waals solid assemblage could produce "
    "hydrogen-rich compounds with potentially higher Tc than H3S. Carbon "
    "introduction was motivated by the desire to chemically tune the H-S "
    "system toward higher critical temperatures.",
    title="C-S-H Design Rationale",
)

deduction(
    premises=[hydride_route_validated],
    conclusion=csh_design_rationale,
    background=[bcs_theory],
    reason=(
        "Given the validated hydride route (@hydride_route_validated) with "
        "H3S at 203 K and LaH10 at 250 K, a natural research direction is to "
        "chemically tune the H-S system by introducing additional elements "
        "(carbon) to potentially increase Tc further, guided by BCS theory's "
        "prediction that hydrogen-rich systems favor high Tc."
    ),
    prior=0.90,
)

photochemical_synthesis = claim(
    "Samples were prepared by photochemical synthesis from elemental "
    "precursors (C + S + H2) in the DAC, using green laser irradiation "
    "to drive the reaction. This is a non-standard synthesis approach — "
    "most high-pressure hydride studies use direct compression of molecular "
    "precursors or laser heating.",
    title="Photochemical Synthesis Method",
)

support(
    premises=[csh_design_rationale],
    conclusion=photochemical_synthesis,
    background=[diamond_anvil_cell],
    reason=(
        "The photochemical approach was chosen to synthesize the C-S-H "
        "compound from elemental precursors, allowing formation of "
        "hydrogen-rich phases not accessible through simple compression "
        "of pre-existing molecular precursors."
    ),
    prior=0.85,
)

# ---------------------------------------------------------------------------
# Question
# ---------------------------------------------------------------------------

main_question = question(
    "Does the photochemically synthesized carbonaceous sulfur hydride (C-S-H) "
    "system exhibit room-temperature superconductivity under high pressure, "
    "and if so, is the evidence robust?",
    title="Main Question: Room-Temperature SC in C-S-H",
)
