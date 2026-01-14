"""
Docstring for learning.transformations
"""

import cv2 as cv
import numpy as np

img = cv.imread('test_image.jpg')

# Translation
# def translate(original_img, x, y):
#     """
#     -x (left), x (right), -y (up), y (down)

#     :param original_img: Description
#     :param x: Description
#     :param y: Description
#     """

#     trans_mat = np.float32([[1, 0, x], [0, 1, y]])

#     dimensions = (original_img.shape[1], original_img.shape[0])

#     return cv.warpAffine(img, trans_mat, dimensions)


# translated_img = translate(img, 100, 100)
# cv.namedWindow("Translated", cv.WINDOW_NORMAL)
# cv.imshow('Translated', translated_img)


# Rotation
# def rotate(original_img, angle, rot_point=None):
#     """
#     Docstring for rotate

#     :param original_img: Description
#     :param angle: Description
#     :param rot_point: Description
#     """

#     (height, width) = original_img.shape[:2]

#     if rot_point is None:
#         rot_point = (width//2, height//2)

#     rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
#     dimensions = (height, width)

#     return cv.warpAffine(original_img, rot_mat, dimensions)


# rotated = rotate(img, 45)
# cv.namedWindow("Rotated", cv.WINDOW_NORMAL)
# cv.imshow('Rotated', rotated)

# Resize
# Shrinking = cv.INTER_AREA
# Enlarging = cv.INTER_LINEAR/CUBIC
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# cv.namedWindow("Resized", cv.WINDOW_NORMAL)
# cv.imshow('Resized', resized)

# Flipping
# flip = cv.flip(img, -1)
# cv.namedWindow("Flip", cv.WINDOW_NORMAL)
# cv.imshow('Flip', flip)

# Cropped
cropped = img[200:400, 300:400]
cv.namedWindow("Cropped", cv.WINDOW_NORMAL)
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()

# https://youtu.be/oXlwWbU8l2o?t=3427
