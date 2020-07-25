import cv2 as cv
import time
import numpy as np
import time
from matplotlib import pyplot as plt
cap = cv.VideoCapture(0)
_, one = cap.read()
past = one
present = past
future = past
while True:
    past = present
    present = future
    _, frame = cap.read()
    future = frame
    #cv.imshow('past', past)
    #cv.imshow('present', present)
    #cv.imshow('future', future)
    delta_plus = cv.absdiff(present, past)
    delta_0 = cv.absdiff(future, past)
    delta_minus = cv.absdiff(present, future)
    cv.imshow('diff', delta_minus)
    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([255, 255, 0])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(delta_minus, lower_blue, upper_blue)
    cv.imshow('work',mask)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

