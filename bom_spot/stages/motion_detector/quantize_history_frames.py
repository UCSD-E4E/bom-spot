"""Quantizes the shifted history frame."""

import numpy as np
from bom_pipeline.decorators import config, stage
from bom_pipeline.stage import Stage
from bom_pipeline.stage_result import StageResult

from bom_spot.mixins.quantized_frames_mixin import QuantizedFramesMixin
from bom_spot.mixins.shifted_history_frames_mixin import ShiftedHistoryFramesMixin
from bom_spot.models.frame import Frame


@config(
    parameter_name="scale_factor", key="motion_detector/quantize_frames/scale_factor"
)
@stage("shifted_history_frames")
class QuantizeHistoryFrames(Stage, QuantizedFramesMixin):
    """Quantizes the shifted history frame."""

    def __init__(
        self, scale_factor: float, shifted_history_frames: ShiftedHistoryFramesMixin
    ):
        QuantizedFramesMixin.__init__(self)
        Stage.__init__(self)

        self._scale_factor = scale_factor
        self._shifted_history_frames = shifted_history_frames

    def _quantize_frame(self, frame: Frame):
        """
        Normalize pixel values from 0-255 to values from 0-self._scale_factor
        Returns quantized frame
        """
        return np.floor(
            frame.get_frame().astype(np.float32) * self._scale_factor / 255.0
        ).astype(np.int32)

    def execute(self) -> StageResult:
        """Quantizes the shifted history frame."""
        self.quantized_frames = [
            self._quantize_frame(f)
            for f in self._shifted_history_frames.shifted_history_frames
        ]

        return StageResult(True, True)
