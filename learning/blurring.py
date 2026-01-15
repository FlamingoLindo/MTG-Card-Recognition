"""
Docstring for learning.blurring
"""
import cv2 as cv

img = cv.imread('test_image.jpg')

# Averaging
average = cv.blur(img, (7, 7))
cv.namedWindow("average", cv.WINDOW_NORMAL)
cv.imshow('average', average)

# Gaussian
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.namedWindow("gaussian", cv.WINDOW_NORMAL)
cv.imshow('gaussian', gaussian)

# Medium
medium = cv.medianBlur(img, 7)
cv.namedWindow("medium", cv.WINDOW_NORMAL)
cv.imshow('medium', medium)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.namedWindow("bilateral", cv.WINDOW_NORMAL)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()
