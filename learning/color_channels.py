"""
Docstring for learning.color_channels
"""

import cv2 as cv
import numpy as np

img = cv.imread('test_image.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.namedWindow("b", cv.WINDOW_NORMAL)
cv.imshow('b', blue)

cv.namedWindow("g", cv.WINDOW_NORMAL)
cv.imshow('g', green)

cv.namedWindow("r", cv.WINDOW_NORMAL)
cv.imshow('r', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.namedWindow("merged", cv.WINDOW_NORMAL)
cv.imshow('merged', merged)

cv.waitKey(0)
cv.destroyAllWindows()
