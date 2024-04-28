from argparse import ArgumentParser, Namespace

from bom_common.pluggable_cli import Plugin

from bom_spot.motion_tracker_pipeline import MotionTrackerPipeline


class MotionTrackerPlugin(Plugin):
    def __init__(self, parser: ArgumentParser):
        super().__init__(parser)

    def execute(self, args: Namespace):
        motion_tracker = MotionTrackerPipeline(args.input)
        motion_tracker.run()
