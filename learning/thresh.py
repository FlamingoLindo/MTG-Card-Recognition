"""
Docstring for learning.thresh
"""
import cv2 as cv

img = cv.imread('test_image.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple
simple_threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.namedWindow("threshold", cv.WINDOW_NORMAL)
cv.imshow('threshold', simple_threshold)

# Inverse
thresh, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.namedWindow("thresh_inverse", cv.WINDOW_NORMAL)
cv.imshow('thresh_inverse', thresh_inverse)

# Adaptive
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.namedWindow("adaptive_thresh", cv.WINDOW_NORMAL)
cv.imshow('adaptive_thresh', adaptive_thresh)

cv.waitKey(0)
cv.destroyAllWindows()
