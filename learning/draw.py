"""
Docstring for read
"""

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# Manual rectangle
# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow('Green square', blank)

# Rectangle
# cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# Circle
# cv.circle(blank, (250, 250), 40, (0, 255, 0), thickness=3)
# cv.imshow('Circle', blank)

# Line
# cv.line(blank, (250, 250), (150, 150), (0, 255, 0), thickness=1)
# cv.imshow('Line', blank)

# Text
cv.putText(blank, 'Test', (250, 250),
           fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0), thickness=2)
cv.imshow('Text', blank)


cv.waitKey(0)
cv.destroyAllWindows()
