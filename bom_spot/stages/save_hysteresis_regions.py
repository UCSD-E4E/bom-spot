from typing import Dict, List, Tuple

from bom_pipeline.decorators import stage
from bom_pipeline.stage_result import StageResult

from bom_spot.mixins.baboons_mixin import BaboonsMixin
from bom_spot.mixins.frame_mixin import FrameMixin
from bom_spot.models.bayesian_region import BayesianRegion
from bom_spot.models.region import Region
from bom_spot.stages.save_regions import SaveRegions


@stage("baboons")
@stage("frame")
class SaveHysteresisRegions(SaveRegions):
    def __init__(self, baboons: BaboonsMixin, frame: FrameMixin) -> None:
        SaveRegions.__init__(self, baboons, frame)

        self._seen_baboons = set()
        self._waiting_baboons: Dict[int, Tuple[Region, int]] = {}

    def execute(self) -> StageResult:
        observed_baboons: List[BayesianRegion] = [
            b for b in self._baboons.baboons if b.observed
        ]

        waiting_baboons = [
            self._waiting_baboons[b.identity]
            for b in observed_baboons
            if b.identity in self._waiting_baboons
        ]
        for waiting_baboon in waiting_baboons:
            baboon, _ = waiting_baboon[0]

            for baboon, frame_number in waiting_baboon:
                self._save_baboons_for_frame([baboon], frame_number)

            del self._waiting_baboons[baboon.identity]
            self._seen_baboons.add(baboon.identity)

        frame_number = self._frame.frame.get_frame_number()
        seen_baboons = [b for b in observed_baboons if b.identity in self._seen_baboons]
        self._save_baboons_for_frame(seen_baboons, frame_number)

        unseen_baboons = [
            b for b in observed_baboons if b.identity not in self._seen_baboons
        ]
        for unseen_baboon in unseen_baboons:
            self._waiting_baboons[unseen_baboon.identity] = [
                (unseen_baboon, frame_number)
            ]

        return StageResult(True, True)
