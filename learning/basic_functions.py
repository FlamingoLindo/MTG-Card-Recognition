"""
Docstring for learning.basic_functions
"""

import cv2 as cv

img = cv.imread('test_image.jpg')

# Grayscale
# cv.namedWindow("Gray", cv.WINDOW_NORMAL)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.namedWindow("Blur", cv.WINDOW_NORMAL)
# cv.imshow('Blur', blur)

# Edge cascade (Canny)
# canny = cv.Canny(img, 125, 175)
# cv.namedWindow("Canny", cv.WINDOW_NORMAL)
# cv.imshow('Canny', canny)

# Dilating the image
# dilated = cv.dilate(canny, (3, 3), iterations=3)
# cv.namedWindow("Dilated", cv.WINDOW_NORMAL)
# cv.imshow('Dilated', dilated)

# Eroding
# eroded = cv.erode(dilated, (3, 3), iterations=3)
# cv.namedWindow("Eroded", cv.WINDOW_NORMAL)
# cv.imshow('Eroded', eroded)

# Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# Cropping
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()
