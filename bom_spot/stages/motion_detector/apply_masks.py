"""
Applies the masks to the moving foreground.
"""

import numpy as np
from bom_pipeline import Stage
from bom_pipeline.decorators import stage
from bom_pipeline.stage_result import StageResult

from bom_spot.decorators.save_video_result import save_video_result
from bom_spot.decorators.show_result import show_result
from bom_spot.mixins.frame_mixin import FrameMixin
from bom_spot.mixins.moving_foreground_mixin import MovingForegroundMixin
from bom_spot.mixins.shifted_masks_mixin import ShiftedMasksMixin
from bom_spot.models.frame import Frame


@stage("moving_foreground")
@stage("shifted_masks")
@stage("frame")
@save_video_result
@show_result
class ApplyMasks(Stage, MovingForegroundMixin):
    """
    Applies the masks to the moving foreground.
    """

    def __init__(
        self,
        moving_foreground: MovingForegroundMixin,
        shifted_masks: ShiftedMasksMixin,
        frame: FrameMixin,
    ) -> None:
        Stage.__init__(self)
        MovingForegroundMixin.__init__(self)

        self._moving_foreground = moving_foreground
        self._shifted_masks = shifted_masks
        self._frame = frame

    def execute(self) -> StageResult:
        # This cleans up the edges after performing image registration.
        for mask in self._shifted_masks.shifted_masks:
            self.moving_foreground = Frame(
                np.multiply(
                    self._moving_foreground.moving_foreground.get_frame(),
                    mask.get_frame(),
                ),
                self._frame.frame.get_frame_number(),
            )

        return StageResult(True, True)
