"""
Provides a pipeline that takes regions in a Sqlite database and uses the particle filter.
"""
from bom_pipeline.factory import factory
from bom_pipeline.pipeline import Pipeline

from bom_spot.decorators.debug import DisplayDebugRegions
from bom_spot.stages.get_sqlite_baboon import GetSqliteBaboon
from bom_spot.stages.get_video_frame import GetVideoFrame
from bom_spot.stages.particle_filter import ParticleFilterStage as ParticleFilter
from bom_spot.stages.save_computed_regions import SaveComputedRegions
from bom_spot.stages.save_hysteresis_regions import SaveHysteresisRegions
from bom_spot.stages.test_exit import TestExit


class SqliteParticleFilterPipeline(Pipeline):
    """
    Provides a pipeline that takes regions in a Sqlite database and uses the particle filter.
    """

    def __init__(self, video_path: str, runtime_config=None):
        Pipeline.__init__(
            self,
            "SqliteParticleFilterPipeline",
            factory(GetVideoFrame, video_path),
            GetSqliteBaboon,
            ParticleFilter,
            SaveComputedRegions,
            SaveHysteresisRegions,
            DisplayDebugRegions,
            TestExit,
            runtime_config=runtime_config,
            progress=TqdmProgress(),
        )
