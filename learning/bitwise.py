"""
Docstring for learning.bitwise
"""
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rec = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.namedWindow("rec", cv.WINDOW_NORMAL)
cv.imshow('rec', rec)

cir = cv.circle(blank.copy(), (200, 200), 200, 155, -1)
cv.namedWindow("cir", cv.WINDOW_NORMAL)
cv.imshow('cir', cir)

# AND
bit_and = cv.bitwise_and(rec, cir)
cv.namedWindow("bit_and", cv.WINDOW_NORMAL)
cv.imshow('bit_and', bit_and)

# OR
bit_or = cv.bitwise_or(rec, cir)
cv.namedWindow("bit_or", cv.WINDOW_NORMAL)
cv.imshow('bit_or', bit_or)

# NOT
bit_not = cv.bitwise_not(rec)
cv.namedWindow("bit_not", cv.WINDOW_NORMAL)
cv.imshow('bit_not', bit_not)

# XOR
bit_xor = cv.bitwise_xor(rec, cir)
cv.namedWindow("bit_xor", cv.WINDOW_NORMAL)
cv.imshow('bit_xor', bit_xor)

cv.waitKey(0)
cv.destroyAllWindows()
