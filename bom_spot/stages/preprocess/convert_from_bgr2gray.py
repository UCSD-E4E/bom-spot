"""
Converts a color image to a gray-scale image.
"""
import cv2
from bom_pipeline import Stage
from bom_pipeline.decorators import stage
from bom_pipeline.stage_result import StageResult

from bom_spot.mixins.frame_mixin import FrameMixin
from bom_spot.mixins.preprocessed_frame_mixin import PreprocessedFrameMixin
from bom_spot.models.frame import Frame


@stage("frame_mixin")
class ConvertFromBGR2Gray(Stage, PreprocessedFrameMixin):
    """
    Converts a color image to a gray-scale image.
    """

    def __init__(self, frame_mixin: FrameMixin):
        PreprocessedFrameMixin.__init__(self)
        Stage.__init__(self)

        self._frame_mixin = frame_mixin

    def execute(self) -> StageResult:
        """
        Converts a color image to a gray-scale image.
        """

        self.processed_frame = Frame(
            cv2.cvtColor(self._frame_mixin.frame.get_frame(), cv2.COLOR_BGR2GRAY),
            self._frame_mixin.frame.get_frame_number(),
        )
        return StageResult(True, True)
