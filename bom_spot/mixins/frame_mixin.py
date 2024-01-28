"""
Mixin for returning frames.
"""
from bom_spot.models.frame import Frame


class FrameMixin:
    """
    Mixin for returning frames.
    """

    def __init__(self):
        self.frame: Frame = None
