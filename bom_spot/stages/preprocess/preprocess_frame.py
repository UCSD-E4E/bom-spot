"""
Provides a pipeline step for preprocessing a frame.
"""
from typing import Dict

# from bom_spot.stages.preprocess.denoise import Denoise
# from bom_spot.stages.preprocess.denoise_color import DenoiseColor
from bom_pipeline import Serial
from bom_pipeline.decorators import runtime_config

from bom_spot.stages.preprocess.blur_gray import BlurGray
from bom_spot.stages.preprocess.convert_from_bgr2gray import ConvertFromBGR2Gray

# from bom_spot.stages.preprocess.feature_reduction_pca import FeatureReductionPca


@runtime_config("rconfig")
class PreprocessFrame(Serial):
    """
    Pipeline step for preprocessing a frame.
    """

    def __init__(self, rconfig: Dict[str, any]):
        Serial.__init__(
            self,
            "PreprocessFrame",
            rconfig,
            # DenoiseColor,
            # FeatureReductionPca,
            ConvertFromBGR2Gray,
            # Denoise,
            BlurGray,
        )
