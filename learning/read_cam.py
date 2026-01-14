"""
Docstring for read_cam
"""

import cv2 as cv
from Utils.cv.scale_resolution import rescale_frame

capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()

    resized_frame = rescale_frame(frame)

    cv.imshow('Video', resized_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
