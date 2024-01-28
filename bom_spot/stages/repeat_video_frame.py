from bom_pipeline import Stage
from bom_pipeline.decorators import stage
from bom_pipeline.stage_result import StageResult

from bom_spot.decorators.show_result import show_result
from bom_spot.mixins.frame_mixin import FrameMixin
from bom_spot.models.frame import Frame


@stage("frame")
@show_result
class RepeatVideoFrame(Stage):
    def __init__(self, frame: FrameMixin) -> None:
        Stage.__init__(self)

        self._frame = frame
        self.frame: Frame = None

    def execute(self) -> StageResult:
        self.frame = self._frame.frame

        return StageResult(True, True)
