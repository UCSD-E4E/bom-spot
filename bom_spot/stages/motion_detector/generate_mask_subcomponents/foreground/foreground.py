"""
Calculate the foreground of the current frame.
"""
from typing import Dict

from bom_pipeline import Serial
from bom_pipeline.decorators import runtime_config

from bom_spot.stages.motion_detector.generate_mask_subcomponents.foreground.group_frames import (
    GroupFrames,
)
from bom_spot.stages.motion_detector.generate_mask_subcomponents.foreground.intersect_frames import (
    IntersectFrames,
)
from bom_spot.stages.motion_detector.generate_mask_subcomponents.foreground.subtract_background import (
    SubtractBackground,
)
from bom_spot.stages.motion_detector.generate_mask_subcomponents.foreground.union_intersections import (
    UnionIntersections,
)


@runtime_config("rconfig")
class Foreground(Serial):
    """
    Calculate the foreground of the current frame.
    """

    def __init__(self, rconfig: Dict[str, any]) -> None:
        Serial.__init__(
            self,
            "Foreground",
            rconfig,
            GroupFrames,
            IntersectFrames,
            UnionIntersections,
            SubtractBackground,
        )
