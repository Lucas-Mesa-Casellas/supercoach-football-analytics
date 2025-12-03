"""
detection.py
-------------
Handles player and ball detection using YOLOv8/YOLOv11 models.
"""

from ultralytics import YOLO

class PlayerDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        """
        Takes a single video frame and returns bounding boxes for players.
        """
        results = self.model(frame)
        return results
