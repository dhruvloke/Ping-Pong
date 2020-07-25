import cv2 as cv
import numpy as np
import time
from matplotlib import pyplot as plt
cap = cv.VideoCapture(0)
while True:
    _, frame = cap.read()
    edges = cv.Canny(frame, 100, 200)

    contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    '''img = cv.drawContours(frame, contours, -1, (0, 255, 0), 3)
    cv.imshow("image",frame)'''
    #print(contours)
    contour_list = []
    for cnt in contours:
        approx = cv.approxPolyDP(cnt, .03 * cv.arcLength(cnt, True), True)
        if len(approx) == 8:
            area = cv.contourArea(cnt)
            (cx, cy), radius = cv.minEnclosingCircle(cnt)
            circleArea = radius * radius * np.pi
            error = abs(circleArea-area)
            if area > 300:
                contour_list.append(cnt)

    cv.drawContours(frame, contour_list, -1, (255, 0, 0), 2)
    cv.imshow('Objects Detected', frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()