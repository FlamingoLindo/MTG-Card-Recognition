"""
Docstring for read
"""

import cv2 as cv
from Utils.cv.scale_resolution import rescale_frame

img = cv.imread('test_image.jpg')


resized_image = rescale_frame(img)

cv.namedWindow("Card", cv.WINDOW_NORMAL)
cv.imshow('Card', resized_image)

cv.waitKey(0)
cv.destroyAllWindows()
