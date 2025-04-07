import os
from ultralytics import YOLO


class ObjectDetector:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), "..", "models", "yolov5su.pt")
        self.model = YOLO(model_path)

    def detect_objects(self, frame):
        results = self.model(frame)

        objects = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                class_id = box.cls[0].item()
                conf = box.conf[0].item()
                class_name = self.model.names[int(class_id)]

                objects.append({
                    'class': class_name,
                    'confidence': conf,
                    'bbox': (int(x1), int(y1), int(x2), int(y2))
                })

        return objects