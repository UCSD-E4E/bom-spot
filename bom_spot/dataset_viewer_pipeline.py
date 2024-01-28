# from bom_pipeline.factory import factory
# from bom_pipeline.pipeline import Pipeline

# from bom_spot.decorators.debug import DisplayDebugRegions
# from bom_spot.stages.get_region_file_region import (  # GetGroundTruthRegion,
#     GetRegionFileRegion,
# )
# from bom_spot.stages.get_video_frame import GetVideoFrame
# from bom_spot.stages.test_exit import TestExit


# class DatasetViewerPipeline(Pipeline):
#     def __init__(self, video_path: str, runtime_config=None):
#         Pipeline.__init__(
#             self,
#             "DatasetViewer",
#             factory(GetVideoFrame, video_path),
#             GetRegionFileRegion,
#             # GetGroundTruthRegion,
#             DisplayDebugRegions,
#             TestExit,
#             runtime_config=runtime_config,
#             progress=TqdmProgress(),
#         )
