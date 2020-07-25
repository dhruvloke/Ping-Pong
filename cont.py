import cv2
import numpy as np

img = cv2.imread("photo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new = cv2.medianBlur(gray, 5)
color = cv2.cvtColor(new, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(new, cv2.HOUGH_GRADIENT, 1,minDist=1, param1=100, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img, i[0], i[1], i[2], (0, 255, 0), 2)

    cv2.circle(img, i[0], i[1], 2, (0, 255, 0), 3)

cv2.imshow("Circles", img)
cv2.waitKey(5)
cv2.destroyWindow()
