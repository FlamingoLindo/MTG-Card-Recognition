"""
Docstring for learning.edge_detect
"""

import cv2 as cv
import numpy as np

img = cv.imread('test_image.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.namedWindow("lap", cv.WINDOW_NORMAL)
cv.imshow('lap', lap)

# Sobel
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelX, sobelY)
cv.namedWindow("combined", cv.WINDOW_NORMAL)
cv.imshow('combined', combined)


cv.waitKey(0)
cv.destroyAllWindows()
