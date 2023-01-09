from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class FzDataset(CocoDataset):

    CLASSES = ('blauer_Ball', 'gelber_Ball', 'roter_Ball')