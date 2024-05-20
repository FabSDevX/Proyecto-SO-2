import random
import cv2
import torch
import numpy as np
from pathlib import Path
from utils.general import check_img_size, non_max_suppression, scale_coords, xyxy2xywh
from utils.datasets import letterbox
from models.experimental import attempt_load
from utils.torch_utils import select_device

# Define the labels you're using
labels = ['knife', 'glasses']

class YOLOV5_Detector:
    def __init__(self, weights, img_size, confidence_thres, iou_thresh, agnostic_nms, augment):
        self.weights = str(weights) 
        self.imgsz = img_size
        self.conf_thres = confidence_thres
        self.iou_thres = iou_thresh
        self.agnostic_nms = agnostic_nms
        self.augment = augment

        self.device = select_device("")
        
        self.model = attempt_load(self.weights) 
        self.stride = int(self.model.stride.max()) 
        self.imgsz = check_img_size(img_size, s=self.stride)  

    def plot_one_box(self, x, img, color=None, label=None, line_thickness=3):
        tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # Line thickness
        color = color or [random.randint(0, 255) for _ in range(3)]
        c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
        cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        if label:
            tf = max(tl - 1, 1)  # Font thickness
            t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
            cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # Filled
            cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    def Detect(self, img0):
        img = letterbox(img0, self.imgsz, stride=self.stride)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img)

        img = torch.from_numpy(img).to(self.device)
        img = img.float()
        img /= 255.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        pred = self.model(img, augment=self.augment)[0]

        # Apply NMS
        pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, agnostic=self.agnostic_nms)

        # Process detections
        for i, det in enumerate(pred):
            s = '%gx%g ' % img.shape[2:]  # Print string
            gn = torch.tensor(img0.shape)[[1, 0, 1, 0]]  # Normalization gain whwh
            if len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()

                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # Detections per class
                    s += f"{n} {labels[int(c)]}{'s' * (n > 1)}, "  # Add to string

                for *xyxy, conf, cls in reversed(det):
                    label = f'{labels[int(cls)]} {conf:.2f}'
                    self.plot_one_box(xyxy, img0, label=label, color=[0, 0, 255], line_thickness=3)

                print("Total Detections:", len(det))

        return img0

    def get_counts(self):
        # Return counts of detected objects
        pass
