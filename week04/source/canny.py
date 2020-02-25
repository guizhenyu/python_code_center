#!/usr/bin/env python
#encoding=gbk
import cv2

img= cv2.imread('learn.jpg', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
cv2.imshow("canny", cv2.Canny(gray, 200, 300))
cv2.waitKey()
cv2.destroyAllWindows()