"""
Provides an algorithm for extracting motion regions from drone footage.
"""
from bom_common.pipeline.library_config import LibraryConfig
from bom_common.pipeline.tqdm_progress import TqdmProgress
from bom_pipeline.factory import factory
from bom_pipeline.initializer import Initializer
from bom_pipeline.pipeline import Pipeline

from bom_spot.decorators.debug import DisplayDebugRegions
from bom_spot.stages.get_video_frame import GetVideoFrame
from bom_spot.stages.motion_detector.motion_detector import MotionDetector
from bom_spot.stages.overlay import Overlay
from bom_spot.stages.preprocess.preprocess_frame import PreprocessFrame
from bom_spot.stages.save_motion_regions import SaveMotionRegions
from bom_spot.stages.test_exit import TestExit


class MotionTrackerPipeline(Pipeline):
    """
    An algorithm that attempts to extract motion regions from drone footage.
    """

    def __init__(self, video_path: str, runtime_config=None):
        Initializer(LibraryConfig())

        Pipeline.__init__(
            self,
            "MotionTrackerPipeline",
            factory(GetVideoFrame, video_path),
            PreprocessFrame,
            MotionDetector,
            SaveMotionRegions,
            Overlay,
            DisplayDebugRegions,
            TestExit,
            runtime_config=runtime_config,
            progress=TqdmProgress(),
        )
