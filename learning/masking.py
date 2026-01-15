"""
Docstring for learning.masking
"""
import cv2 as cv
import numpy as np

img = cv.imread('test_image.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2-300), 300, 255, -1)
cv.namedWindow("mask", cv.WINDOW_NORMAL)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.namedWindow("masked", cv.WINDOW_NORMAL)
cv.imshow('masked', masked)

cv.waitKey(0)
cv.destroyAllWindows()
