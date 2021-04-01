import cv2
import numpy as np
from PIL import Image
import time

CAMERA_ID = 0
cap = cv2.VideoCapture(CAMERA_ID)

print("Frame width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Frame height:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Frame rate:", cap.get(cv2.CAP_PROP_FPS))

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONTSCALE = 0.5
COLOR = (0, 0, 0)
THICKNESS = 1
fps = -1
cum_fps = 0
frame_count = 0

while True:
    start_time = time.time()

    frame_count += 1

    ret, frame = cap.read()

    image = cv2.putText(
        frame, f"FPS: {fps}", (10, 450), FONT, FONTSCALE, COLOR, THICKNESS, cv2.LINE_AA
    )

    image = cv2.putText(
        image,
        f"FC: {frame_count}",
        (10, 470),
        FONT,
        FONTSCALE,
        COLOR,
        THICKNESS,
        cv2.LINE_AA,
    )

    cv2.imshow("camera", image)

    end_time = time.time()
    fps = round(1.0 / (end_time - start_time + 1e-6))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
