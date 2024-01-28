"""
Mixin for returning baboon objects.
"""

from typing import List

from bom_spot.models.region import Region


class BaboonsMixin:
    """
    Mixin for returning baboon objects.
    """

    def __init__(self):
        self.baboons: List[Region] = None
