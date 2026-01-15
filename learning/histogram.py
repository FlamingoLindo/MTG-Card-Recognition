"""
Docstring for learning.histogram
"""
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('test_image.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()

plt.title('Gray histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

plt.plot(hist)
plt.xlim([0, 256])
plt.show()
