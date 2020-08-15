import cv2 as cv
import math
import time
import numpy as np
import time
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
cap = cv.VideoCapture(0)
_, one = cap.read()
one = cv.resize(one,(320,240))
past = one
present = past
future = past
'''result = cv.VideoWriter('pingpongcolor.avi',cv.VideoWriter_fourcc(*'MJPG'),10, (320,240))
result2 = cv.VideoWriter('pingpongabsdiff.avi',cv.VideoWriter_fourcc(*'MJPG'),10, (320,240))
result3 = cv.VideoWriter('pingpongbinary.avi',cv.VideoWriter_fourcc(*'MJPG'),10, (320,240))'''
cv.VideoWriter()
while True:
    start = time.time()
    past = present
    present = future
    _, frame = cap.read()
    frame = cv.resize(frame,(320,240))
    future = frame
    #result.write(frame)
    #cv.imshow('past', past)
    #cv.imshow('present', present)
    #cv.imshow('future', future)
    delta_plus = cv.absdiff(present, past)
    #result2.write(delta_plus)
    delta_0 = cv.absdiff(future, past)
    delta_minus = cv.absdiff(present, future)
    #cv.imshow('diff', work(past, present, 10))
    #cv.imshow('comp',delta_plus)
    gray_plus = cv.cvtColor(delta_plus, cv.COLOR_BGR2GRAY)
    gray_0 = cv.cvtColor(delta_0, cv.COLOR_BGR2GRAY)
    gray_minus = cv.cvtColor(delta_minus, cv.COLOR_BGR2GRAY)
    #cv.imshow('gray',gray_plus)
    th = 20
    fplus = cv.threshold(gray_plus, th, 255, cv.THRESH_BINARY)[1]
    f0 = cv.threshold(gray_0, th, 255, cv.THRESH_BINARY)[1]
    fminus = cv.threshold(gray_minus, th, 255, cv.THRESH_BINARY)[1]
    finalp1 = cv.bitwise_or(fplus,f0)
    finalp2 = cv.bitwise_or(finalp1,fminus)
    good = cv.bitwise_not(finalp2)
    cv.imshow('hope', good)
    #result3.write(good)
    k = cv.waitKey(5) & 0xFF
    print(time.time()-start)
    if k == 27:
        break
'''result.release()
result2.release()
result3.release()'''
cv.destroyAllWindows()

