import cv2
import numpy as np


class LaneDetector:
    def __init__(self):
        pass

    def detect_lanes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=50)

        lanes = []
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                lanes.append(((x1, y1), (x2, y2)))

        return lanes