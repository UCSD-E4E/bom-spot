"""
Mixin for returning preprocessed frames.
"""
from bom_spot.models.frame import Frame


class PreprocessedFrameMixin:
    """
    Mixin for returning preprocessed frames.
    """

    def __init__(self):
        self.processed_frame: Frame = None
