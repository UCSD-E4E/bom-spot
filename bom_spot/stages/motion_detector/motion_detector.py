"""
Implements a motion tracker pipeline.
"""
from typing import Dict

# from bom_spot.stages.save_video import SaveVideo
from bom_pipeline import Serial
from bom_pipeline.decorators import runtime_config

from bom_spot.stages.motion_detector.apply_masks import ApplyMasks
from bom_spot.stages.motion_detector.compute_moving_foreground import (
    ComputeMovingForeground,
)
from bom_spot.stages.motion_detector.compute_transformation_matrices import (
    ComputeTransformationMatrices,
)
from bom_spot.stages.motion_detector.detect_blobs import DetectBlobs
from bom_spot.stages.motion_detector.generate_mask_subcomponents.generate_mask_subcomponents import (
    GenerateMaskSubcomponents,
)
from bom_spot.stages.motion_detector.generate_weights import GenerateWeights

# from bom_spot.stages.motion_detector.min_size_filter import MinSizeFilter
from bom_spot.stages.motion_detector.noise_reduction.db_scan_filter import DbScanFilter

# from bom_spot.stages.motion_detector.hysteresis_filter import HysteresisFilter
from bom_spot.stages.motion_detector.quantize_history_frames import (
    QuantizeHistoryFrames,
)
from bom_spot.stages.motion_detector.store_history_frame import StoreHistoryFrame
from bom_spot.stages.motion_detector.transformed_frames.transformed_frames import (
    TransformedFrames,
)

# from bom_spot.stages.motion_detector.noise_reduction.noise_reduction import (
#     NoiseReduction,
# )


@runtime_config("rconfig")
class MotionDetector(Serial):
    """
    Implements a motion tracker pipeline.
    """

    def __init__(self, rconfig: Dict[str, any]):
        Serial.__init__(
            self,
            "MotionDetector",
            rconfig,
            StoreHistoryFrame,
            ComputeTransformationMatrices,
            TransformedFrames,
            QuantizeHistoryFrames,
            GenerateWeights,
            GenerateMaskSubcomponents,
            ComputeMovingForeground,
            ApplyMasks,
            DbScanFilter,
            # NoiseReduction,
            DetectBlobs,
            # MinSizeFilter,
        )
