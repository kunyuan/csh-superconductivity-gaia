"""Leaf claim priors — package input interface.

Each entry maps a leaf claim (not derived by any strategy) to its
prior probability and a one-line justification. These are injected
into claim metadata by ``gaia compile`` and read by the lowering
layer during inference.

Priors are assigned as if reading the paper fresh — reflecting
intuitive plausibility of each experimental observation.
"""

from .background import hydride_route_validated
from .experiment import (
    field_suppression,
    isotope_effect_observed,
    resistance_observation,
    susceptibility_observation,
)

PRIORS: dict = {
    # Background — well-established prior results
    hydride_route_validated: (
        0.95,
        "H3S and LaH10 independently confirmed by multiple groups; "
        "hydride route firmly established.",
    ),
    # Experimental claims — reasonable priors for DAC measurements
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
}
