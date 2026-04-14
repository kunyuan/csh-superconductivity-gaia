"""Leaf claim priors — package input interface.

Each entry maps a leaf claim (not derived by any strategy) to its
prior probability and a one-line justification. These are injected
into claim metadata by ``gaia compile`` and read by the lowering
layer during inference.

NOTE: Priors for the ORIGINAL claims are assigned as if reading the paper
fresh, before knowing about the retraction. Priors for RETRACTION evidence
are assigned based on the quality of the analyses and replication attempts.
"""

from .background import hydride_route_validated
from .experiment import (
    field_suppression,
    isotope_effect_observed,
    resistance_observation,
    susceptibility_observation,
)
from .retraction import (
    background_subtraction_fraud,
    dias_broader_issues,
    eremets_failed_replication,
    goncharov_failed_replication,
    nature_retraction,
)

PRIORS: dict = {
    # Background — well-established prior results
    hydride_route_validated: (
        0.95,
        "H3S and LaH10 independently confirmed by multiple groups; "
        "hydride route firmly established.",
    ),
    # Original experimental claims — reasonable priors AS IF reading the paper fresh
    resistance_observation: (
        0.85,
        "Four-probe measurement in DAC, standard technique; "
        "but extraordinary claim warrants some skepticism.",
    ),
    susceptibility_observation: (
        0.80,
        "AC susceptibility in DAC is complex; background subtraction "
        "introduces significant processing uncertainty.",
    ),
    field_suppression: (
        0.80,
        "Standard magnetic field test, but depends on same DAC setup "
        "and sample quality as other measurements.",
    ),
    isotope_effect_observed: (
        0.75,
        "13C substitution is less conventional than H/D isotope effect; "
        "C phonon contribution to SC pairing is less established.",
    ),
    # Retraction evidence — HIGH priors because well-documented analyses
    background_subtraction_fraud: (
        0.95,
        "Detailed statistical analysis by van der Marel & Hirsch; "
        "peer-reviewed methodology, reproducible findings.",
    ),
    eremets_failed_replication: (
        0.90,
        "6-month effort by leading high-pressure SC group; "
        "partial SC observed but far below claimed Tc.",
    ),
    goncharov_failed_replication: (
        0.90,
        "Expert group could not synthesize claimed compound; "
        "independent negative evidence.",
    ),
    nature_retraction: (
        0.99,
        "Official editorial retraction by Nature; highest level of "
        "formal invalidation.",
    ),
    dias_broader_issues: (
        0.92,
        "Second retraction (lutetium hydride) plus institutional "
        "investigations; documented pattern.",
    ),
}
