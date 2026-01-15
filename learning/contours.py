"""
Docstring for learning.contours
"""

import cv2 as cv
import numpy as np

img = cv.imread('test_image.jpg')

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)

# Transform the image into binary
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.namedWindow("Contours", cv.WINDOW_NORMAL)
cv.imshow('Contours', blank)

cv.namedWindow("Threshold", cv.WINDOW_NORMAL)
cv.imshow('Threshold', thresh)

cv.waitKey(0)
cv.destroyAllWindows()
