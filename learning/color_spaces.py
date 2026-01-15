"""
Docstring for learning.contours
"""

import cv2 as cv

img = cv.imread('test_image.jpg')

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow("gray", cv.WINDOW_NORMAL)
cv.imshow('gray', gray)

# BGR tp HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.namedWindow("hsv", cv.WINDOW_NORMAL)
cv.imshow('hsv', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.namedWindow("lab", cv.WINDOW_NORMAL)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.namedWindow("rgb", cv.WINDOW_NORMAL)
cv.imshow('rgb', rgb)


cv.waitKey(0)
cv.destroyAllWindows()
