from typing import Any, Dict

from bom_pipeline import Stage
from bom_pipeline.decorators import runtime_config, stage
from bom_pipeline.stage_result import StageResult
from library.region_file import RegionFile, region_factory

from bom_spot.decorators.debug import debug
from bom_spot.mixins.baboons_mixin import BaboonsMixin
from bom_spot.mixins.frame_mixin import FrameMixin


# @debug(FrameMixin, (0, 255, 0))
# @runtime_config("config")
# @stage("frame")
class GetRegionFileRegionBase(Stage, BaboonsMixin):
    def __init__(self, frame: FrameMixin, config: Dict[str, Any]) -> None:
        Stage.__init__(self)
        BaboonsMixin.__init__(self)

        self._frame = frame
        self._region_file: RegionFile = None

        if "region_file" in config:
            self._region_file = region_factory(config["region_file"])

    def execute(self) -> StageResult:
        self.baboons = (
            list(self._region_file.frame_regions(self._frame.frame.get_frame_number()))
            if self._region_file
            else []
        )

        return StageResult(True, True)


@debug(FrameMixin, (0, 255, 0))
@runtime_config("config")
@stage("frame")
class GetRegionFileRegion(GetRegionFileRegionBase):
    def __init__(self, frame: FrameMixin, config: Dict[str, Any]) -> None:
        GetRegionFileRegionBase.__init__(self, frame, config)


@debug(FrameMixin, (0, 0, 255))
@runtime_config("config")
@stage("frame")
class GetGroundTruthRegion(GetRegionFileRegionBase):
    def __init__(self, frame: FrameMixin, config: Dict[str, Any]) -> None:
        if "ground_truth" in config and config["ground_truth"]:
            config["region_file"] = config["ground_truth"]
        elif "region_file" in config:
            config.pop("region_file")

        GetRegionFileRegionBase.__init__(self, frame, config)
