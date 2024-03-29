"""
Implements a storage of historical frame step for motion detection.
"""

from bom_pipeline import Stage
from bom_pipeline.decorators import config, stage
from bom_pipeline.stage_result import StageResult
from rx.subject import Subject

from bom_spot.mixins.history_frames_mixin import HistoryFramesMixin
from bom_spot.mixins.preprocessed_frame_mixin import PreprocessedFrameMixin


@config(
    parameter_name="history_frame_count",
    key="motion_detector/history_frames",
)
@stage("preprocessed_frame")
class StoreHistoryFrame(Stage, HistoryFramesMixin):
    """
    Implements a storage of historical frame step for motion detection.
    """

    def __init__(
        self, history_frame_count: int, preprocessed_frame: PreprocessedFrameMixin
    ):
        self._history_frame_popped_subject = Subject()
        self.history_frame_popped = self._history_frame_popped_subject

        HistoryFramesMixin.__init__(
            self, history_frame_count, self.history_frame_popped
        )
        Stage.__init__(self)

        self._history_frame_count = history_frame_count
        self._preprocessed_frame = preprocessed_frame
        self._next_history_frame = None

    def execute(self) -> StageResult:
        """
        Implements a storage of historical frame step for motion detection.
        """
        if self.is_full():
            frame = self.history_frames.popleft()
            self._history_frame_popped_subject.on_next(frame)

        if self._next_history_frame is not None:
            self.history_frames.append(self._next_history_frame)

        self._next_history_frame = self._preprocessed_frame.processed_frame

        return StageResult(True, True)
