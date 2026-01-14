"""
Docstring for Utils.cv.scale_resolution
"""

import cv2 as cv


def change_resolution(capture: cv.VideoCapture, width: float, height: float, brightness: float):
    """
    Only works for live video

    :param capture: Description
    :type capture: cv.VideoCapture
    :param width: Description
    :type width: float
    :param height: Description
    :type height: float
    :param brightness: Description
    :type brightness: float
    """

    capture.set(3, width)
    capture.set(4, height)
    capture.set(10, brightness)


def rescale_frame(original_frame, scale: float = 0.75):
    """
    Docstring for rescale_frame

    :param original_frame: Description
    :type original_frame: MatLike
    :param scale: Description
    :type scale: float
    """
    width = int(original_frame.shape[1] * scale)
    height = int(original_frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(original_frame, dimensions, interpolation=cv.INTER_AREA)
