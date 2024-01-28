"""
Mixin for returning the moving foreground.
"""
from bom_spot.models.frame import Frame


class MovingForegroundMixin:
    """
    Mixin for returning the moving foreground.
    """

    def __init__(self):
        self.moving_foreground: Frame = None
