"""
Implements a noise reduction stage.
"""
from typing import Dict

from bom_pipeline import ConfigSerial
from bom_pipeline.decorators import runtime_config

from bom_spot.stages.motion_detector.noise_reduction.dilate_erode_filter import (
    DilateErodeFilter,
)
from bom_spot.stages.motion_detector.noise_reduction.group_filter import GroupFilter
from bom_spot.stages.motion_detector.noise_reduction.hysteresis_filter import (
    HysteresisFilter,
)


@runtime_config("rconfig")
class NoiseReduction(ConfigSerial):
    """
    Implements a noise reduction stage.
    """

    def __init__(self, rconfig: Dict[str, any]) -> None:
        ConfigSerial.__init__(
            self,
            "NoiseReduction",
            "motion_detector_stages",
            rconfig,
            HysteresisFilter,
            GroupFilter,
            DilateErodeFilter,
        )
