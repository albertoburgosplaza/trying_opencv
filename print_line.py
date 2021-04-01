import cv2
import numpy as np
from PIL import Image
import time

CAMERA_ID = 0
cap = cv2.VideoCapture(CAMERA_ID)

FRAME_WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FRAME_HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FRAME_FPS = int(cap.get(cv2.CAP_PROP_FPS))

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONTSCALE = 0.5
COLOR = (0, 0, 0)
THICKNESS = 1

START_POINT_LINE = (0, FRAME_HEIGHT // 2)
END_POINT_LINE = (FRAME_WIDTH, FRAME_HEIGHT // 2)

lines = []


def get_mouse_coords(event, x, y, flags, param):
    global lines, image
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(lines) == 2:
            lines = []
        lines.append((x, y))
        print(lines)
    elif event == cv2.EVENT_MOUSEMOVE:
        if (len(lines) > 0) & (len(lines) % 2 == 1):
            image = frame.copy()
            cv2.line(image, lines[-1], (x, y), (0, 0, 255), THICKNESS)
            cv2.imshow("camera", image)


while True:
    ret, frame = cap.read()

    image = frame.copy()

    cv2.putText(
        image,
        "Press 't' to take a frame",
        (10, 470),
        FONT,
        FONTSCALE,
        COLOR,
        THICKNESS,
        cv2.LINE_AA,
    )

    cv2.imshow("camera", image)

    if cv2.waitKey(1) & 0xFF == ord("t"):
        break

image = frame.copy()
cap.release()
cv2.setMouseCallback("camera", get_mouse_coords)

while True:
    cv2.imshow("camera", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
