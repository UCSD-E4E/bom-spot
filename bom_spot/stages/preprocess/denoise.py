"""
Implements denoising using OpenCV.
"""
import cv2
from bom_pipeline import Stage
from bom_pipeline.decorators import stage
from bom_pipeline.stage_result import StageResult

from bom_spot.decorators.show_result import show_result
from bom_spot.mixins.preprocessed_frame_mixin import PreprocessedFrameMixin
from bom_spot.models.frame import Frame


@stage("preprocessed_frame")
@show_result
class Denoise(Stage, PreprocessedFrameMixin):
    """
    Implements denoising using OpenCV.
    """

    def __init__(self, preprocessed_frame: PreprocessedFrameMixin) -> None:
        PreprocessedFrameMixin.__init__(self)
        Stage.__init__(self)

        self._preprocessed_frame = preprocessed_frame

    def execute(self) -> StageResult:
        self.processed_frame = Frame(
            cv2.fastNlMeansDenoising(
                self._preprocessed_frame.processed_frame.get_frame(),
                h=3,
                templateWindowSize=7,
                searchWindowSize=21,
            ),
            self._preprocessed_frame.processed_frame.get_frame_number(),
        )

        return StageResult(True, True)
