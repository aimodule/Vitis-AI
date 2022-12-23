from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class TableDataset(CocoDataset):

    CLASSES = ('tray_on_table_left', 'background')