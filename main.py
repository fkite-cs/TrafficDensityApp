import argparse
import os

from src.tfapp import TFApp 
from types import SimpleNamespace

if __name__ == "__main__":
    model_type = "yolo"
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

    parser = argparse.ArgumentParser()
    parser.add_argument("--img_path", type=str, required=True)
    parser.add_argument("--out_folder", type=str, required=True)
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    config = SimpleNamespace(**config)
    app = TFApp(model_type=model_type, vd_config=config)

    img_path = args.img_path
    if args.device != "cpu":
        print("Coming soon...")
    else:
        if not os.path.exists(args.out_folder):
            os.makedirs(args.out_folder)

        app.main(img_path, args.out_folder)
        print("finish :)")