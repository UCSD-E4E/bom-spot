"""
Compute shifted masks for use in throwing pixels not common between frames.
"""
import cv2
import numpy as np
from bom_pipeline.decorators import stage
from bom_pipeline.stage import Stage
from bom_pipeline.stage_result import StageResult

from bom_spot.mixins.history_frames_mixin import HistoryFramesMixin
from bom_spot.mixins.preprocessed_frame_mixin import PreprocessedFrameMixin
from bom_spot.mixins.shifted_masks_mixin import ShiftedMasksMixin
from bom_spot.mixins.transformation_matrices_mixin import TransformationMatricesMixin
from bom_spot.models.frame import Frame


@stage("transformation_matrices")
@stage("history_frames")
@stage("frame")
class ComputeShiftedMasks(Stage, ShiftedMasksMixin):
    """
    Compute shifted masks for use in throwing pixels not common between frames.
    """

    def __init__(
        self,
        transformation_matrices: TransformationMatricesMixin,
        history_frames: HistoryFramesMixin,
        frame: PreprocessedFrameMixin,
    ):
        ShiftedMasksMixin.__init__(self)
        Stage.__init__(self)

        self._transformation_matrices = transformation_matrices
        self._history_frames = history_frames
        self._frame = frame

    def execute(self) -> StageResult:
        transformation_matrices = self._transformation_matrices.transformation_matrices
        history_frames = self._history_frames.history_frames
        frame = self._frame.processed_frame

        img = np.ones(frame.get_frame().shape).astype(np.uint8)
        self.shifted_masks = [
            Frame(
                cv2.warpPerspective(
                    img,
                    M,
                    (frame.get_frame().shape[1], frame.get_frame().shape[0]),
                ),
                h.get_frame_number(),
            )
            for M, h in zip(transformation_matrices, history_frames)
        ]

        return StageResult(True, True)
