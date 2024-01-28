"""
Union frames that were previously intersected.
"""
import numpy as np
from bom_pipeline import Stage
from bom_pipeline.decorators import stage
from bom_pipeline.stage_result import StageResult

from bom_spot.mixins.intersected_frames_mixin import IntersectedFramesMixin
from bom_spot.mixins.unioned_frames_mixin import UnionedFramesMixin


@stage("intersected_frames")
class UnionIntersections(Stage, UnionedFramesMixin):
    """
    Union frames that were previously intersected.
    """

    def __init__(self, intersected_frames: IntersectedFramesMixin) -> None:
        Stage.__init__(self)
        UnionedFramesMixin.__init__(self)

        self._intersected_frames = intersected_frames

    def execute(self) -> StageResult:
        intersected_frames = self._intersected_frames.intersected_frames
        self.unioned_frames = self._union_frames(intersected_frames)

        return StageResult(True, True)

    def _union_frames(self, frames):
        """
        Union all frame intersections to produce acting background for all frames
        Returns the single union frame produced by unioning all frames in input
        """
        union = np.zeros(frames[0].shape, dtype=np.uint8)

        f_copy = frames.copy()
        f_copy.reverse()

        for f in f_copy:
            union[union == 0] = f[union == 0]

        return union
