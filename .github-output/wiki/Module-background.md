# Module: background

### bcs_theory

**QID:** `github:csh_superconductivity::bcs_theory`
**Type:** setting
**Role:** setting
**Content:** Bardeen-Cooper-Schrieffer (BCS) theory: phonon-mediated electron-electron attraction leads to Cooper pairing. The Eliashberg formulation places no apparent upper bound on Tc. High Tc requires: (1) high-frequency phonons, (2) strong electron-phonon coupling, (3) high electronic density of states.

### h3s_precedent

**QID:** `github:csh_superconductivity::h3s_precedent`
**Type:** setting
**Role:** setting
**Content:** Drozdov et al. (2015) demonstrated superconductivity at Tc = 203 K in H3S under ~155 GPa, confirmed by multiple groups. This established hydrogen-rich compounds under extreme pressure as a viable route to high-Tc superconductivity.

### lah10_precedent

**QID:** `github:csh_superconductivity::lah10_precedent`
**Type:** setting
**Role:** setting
**Content:** Drozdov et al. (2019) and Somayazulu et al. (2019) independently confirmed superconductivity at ~250 K in LaH10 (lanthanum decahydride) in the clathrate structure under ~170 GPa. This demonstrated that the hydride route could reach even higher Tc than H3S.

### diamond_anvil_cell

**QID:** `github:csh_superconductivity::diamond_anvil_cell`
**Type:** setting
**Role:** setting
**Content:** Diamond anvil cell (DAC) enables static high-pressure experiments up to hundreds of GPa. Four-probe resistance measurements and ac magnetic susceptibility measurements can be performed in situ. Samples are typically ~10 um in diameter.

### hydride_route_validated

**QID:** `github:csh_superconductivity::hydride_route_validated`
**Type:** claim
**Role:** independent
**Content:** The discoveries of H3S at 203 K and LaH10 at 250 K established that hydrogen-rich compounds under extreme pressure can achieve very high superconducting Tc via the conventional BCS mechanism. This validated the hydride route and motivated searches for even higher Tc by chemical tuning.
**Prior:** 0.95
**Belief:** 0.93
**prior:** 0.95
**prior_justification:** H3S and LaH10 independently confirmed by multiple groups; hydride route firmly established.
**Referenced by:** deduction -> `github:csh_superconductivity::csh_design_rationale`

### csh_design_rationale

**QID:** `github:csh_superconductivity::csh_design_rationale`
**Type:** claim
**Role:** derived
**Content:** The C-S-H system was targeted by mixing methane (CH4) into the H2S + H2 precursor mixture for H3S at low pressures. The rationale was that molecular exchange within the van der Waals solid assemblage could produce hydrogen-rich compounds with potentially higher Tc than H3S. Carbon introduction was motivated by the desire to chemically tune the H-S system toward higher critical temperatures.
**Belief:** 0.96
**Derived from:** deduction
**Premises:** `github:csh_superconductivity::hydride_route_validated`
**gaia:** {'provenance': {'referenced_claims': ['hydride_route_validated']}}
**Referenced by:** support -> `github:csh_superconductivity::photochemical_synthesis`

### photochemical_synthesis

**QID:** `github:csh_superconductivity::photochemical_synthesis`
**Type:** claim
**Role:** derived
**Content:** Samples were prepared by photochemical synthesis from elemental precursors (C + S + H2) in the DAC, using green laser irradiation to drive the reaction. This is a non-standard synthesis approach — most high-pressure hydride studies use direct compression of molecular precursors or laser heating.
**Belief:** 0.83
**Derived from:** support
**Premises:** `github:csh_superconductivity::csh_design_rationale`

### main_question

**QID:** `github:csh_superconductivity::main_question`
**Type:** question
**Role:** question
**Content:** Does the photochemically synthesized carbonaceous sulfur hydride (C-S-H) system exhibit room-temperature superconductivity under high pressure, and if so, is the evidence robust?
