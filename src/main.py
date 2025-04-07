import cv2
import os
from object_detection import ObjectDetector
from lane_detection import LaneDetector
from traffic_sign_recognition import SignRecognizer
from utils import draw_on_frame


def process_video(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: Input video file not found at {input_path}")
        return

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {input_path}")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    object_detector = ObjectDetector()
    lane_detector = LaneDetector()
    sign_recognizer = SignRecognizer()

    frame_count = 0
    print("Starting video processing...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        objects = object_detector.detect_objects(frame)
        lanes = lane_detector.detect_lanes(frame)
        signs = sign_recognizer.recognize_signs(frame)

        annotated_frame = draw_on_frame(frame, objects, lanes, signs)
        out.write(annotated_frame)

        frame_count += 1
        if frame_count % 100 == 0:
            print(f"Processed {frame_count} frames...")

    cap.release()
    out.release()
    print(f"Video processing complete. Output saved to {output_path}")


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "..", "data", "driving_through_city.mp4")
    output_path = os.path.join(os.path.dirname(__file__), "..", "output", "processed_video.mp4")
    process_video(input_path, output_path)