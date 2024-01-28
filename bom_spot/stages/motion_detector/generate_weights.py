"""
Generates a set of weights to represent how often a pixel changes.
"""
import numpy as np
from bom_pipeline import Stage
from bom_pipeline.decorators import stage
from bom_pipeline.stage_result import StageResult
from library.utils import scale_ndarray

from bom_spot.decorators.save_img_result import save_img_result
from bom_spot.mixins.frame_mixin import FrameMixin
from bom_spot.mixins.quantized_frames_mixin import QuantizedFramesMixin
from bom_spot.mixins.weights_mixin import WeightsMixin


@stage("quantized_frames")
@stage("frame")
@save_img_result
class GenerateWeights(Stage, WeightsMixin):
    """
    Generates a set of weights to represent how often a pixel changes.
    """

    def __init__(
        self, quantized_frames: QuantizedFramesMixin, frame: FrameMixin
    ) -> None:
        Stage.__init__(self)
        WeightsMixin.__init__(self)

        self._quantized_frames = quantized_frames
        self._frame = frame

    def execute(self) -> StageResult:
        quantized_frames = self._quantized_frames.quantized_frames

        self.weights = self._get_weights(quantized_frames)
        self.weights_frame = scale_ndarray(
            self.weights, self._frame.frame.get_frame_number()
        )

        return StageResult(True, True)

    def _get_weights(self, q_frames):
        """
        Calculate weights based on frequency of commonality between frames according
        to figure 12 of paper
        Returns frame representing frequency of commonality
        """
        weights = np.zeros(q_frames[0].shape).astype(np.uint8)

        for i, _ in enumerate(q_frames):
            if i == 0:
                continue

            mask = (np.abs(q_frames[i] - q_frames[i - 1]) <= 1).astype(np.uint8)
            weights = weights + mask

        return weights
