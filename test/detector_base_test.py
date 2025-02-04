import unittest
import sys
import os
import cv2
import numpy as np
from types import SimpleNamespace

try:
    sys.path.insert(0, "..")
    import src.yolo_utils as yu
except Exception as e:
    # sys.path.insert(0, os.path.abspath(".."))
    sys.path.insert(0, "/home/runner/work/AIVA_2022_TrafficDensityApp/AIVA_2022_TrafficDensityApp/")

import src.detector_base as detector_base


opt = {
    "conf_thres": 0.25,
    "iou_thres": 0.45,
    "classes": None,
    "agnostic_nms": False,
    "max_det": 1000
}

config = {
    "weights_path": "best.pt",
    "device": "cpu",
    "yolo": opt
}

config = SimpleNamespace(**config)

class TestDetectorBase(unittest.TestCase):

    def test_class_name(self):
        model_type = "yolo"
        model = detector_base.DetectorBase(model_type, config)
        m_name = model.model.__class__.__name__
        self.assertEquals(m_name.lower(), model_type)
        model_type = "ssd"
        model = detector_base.DetectorBase(model_type, config)
        m_name = model.model.__class__.__name__
        self.assertEquals(m_name.lower(), model_type)
    
    def test_forward(self):
        model_type = "yolo"
        img = cv2.imread("imgs/austin1_cropped_2.jpg").astype(np.float32)
        model = detector_base.DetectorBase(model_type, config)
        bbox = model.forward([img])
        self.assertEquals(type(bbox), list)
        self.assertEquals(len([img]), len(bbox))
        self.assertEquals(bbox[0].shape[1], 4)

if __name__ == "__main__":
    unittest.main()
