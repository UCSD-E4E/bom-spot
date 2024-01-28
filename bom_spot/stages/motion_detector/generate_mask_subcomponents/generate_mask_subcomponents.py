"""
Calculate the subcomponents that will later be combined into the moving foreground.
"""
from typing import Dict

from bom_pipeline import Parallel
from bom_pipeline.decorators import runtime_config

from bom_spot.stages.motion_detector.generate_mask_subcomponents.foreground.foreground import (
    Foreground,
)
from bom_spot.stages.motion_detector.generate_mask_subcomponents.generate_history_of_dissimilarity import (
    GenerateHistoryOfDissimilarity,
)


@runtime_config("rconfig")
class GenerateMaskSubcomponents(Parallel):
    """
    Calculate the subcomponents that will later be combined into the moving foreground.
    """

    def __init__(self, rconfig: Dict[str, any]) -> None:
        Parallel.__init__(
            self,
            "GenerateMaskSubcomponents",
            rconfig,
            GenerateHistoryOfDissimilarity,
            Foreground,
        )
