import cv2

def draw_on_frame(frame, objects, lanes, signs):
    for obj in objects:
        x1, y1, x2, y2 = obj['bbox']
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{obj['class']} {obj['confidence']:.2f}"
        cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    for lane in lanes:
        cv2.line(frame, lane[0], lane[1], (0, 0, 255), 3)

    for sign in signs:
        x, y, w, h = sign['bbox']
        cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
        cv2.putText(frame, sign['class'], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    return frame