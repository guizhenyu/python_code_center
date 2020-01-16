#!/usr/bin/env python
# encoding=gbk

import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
'''
equalizeHist—直方图均衡化
函数原型： equalizeHist(src, dst=None)
src：图像矩阵(单通道图像)
dst：默认即可
'''


def equalizeHist(gray):
    hist_freq_dict = {}
    (width, high) = gray.shape
    for w in range(width):
        for h in range(high):
            hist = int(gray[w][h])
            if hist not in hist_freq_dict:
                hist_freq_dict[hist] = 1
            else:
                hist_freq_dict[hist] += 1

    hist_arr = []
    for key in hist_freq_dict.keys():
        hist_arr.append(key)

    hist_arr.sort()
    last_pi = 0.0
    for k in hist_arr:
        pi = float(hist_freq_dict[k] / (width * high)) + last_pi
        sum_pi = math.floor(pi * 256)
        hist_freq_dict[k] = sum_pi
        last_pi = pi

    for w in range(width):
        for h in range(high):
            hist = gray[w][h]
            if hist not in hist_freq_dict:
                print(w, h, "error")
            else:
                gray[w][h] = hist_freq_dict[hist]

    return gray

# 获取灰度图像
img = cv2.imread("timg-wf", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("image_gray", gray)
# # 灰度图像直方图均衡化
dst = cv2.equalizeHist(gray)
ss = equalizeHist(gray)

sum_n = 0
(w, h) = dst.shape
for i in range(w):
    for j in range(h):
        if int(dst[i][j]) != int(ss[i][j]):
            sum_n += 1
            print(i, j, dst[i][j], ss[i][j])

print("sum_n", sum_n)


#
# # 直方图
hist = cv2.calcHist([ss],[0],None,[256],[0,256])

plt.figure()
plt.hist(ss.ravel(), 256)
plt.show()

cv2.imshow("Histogram Equalization", np.hstack([gray, ss]))
cv2.waitKey(0)



# 彩色图像直方图均衡化
# img = cv2.imread("lenna.png", 1)
# cv2.imshow("src", img)
#
# # 彩色图像均衡化,需要分解通道 对每一个通道均衡化
# (b, g, r) = cv2.split(img)
# bH = cv2.equalizeHist(b)
# gH = cv2.equalizeHist(g)
# rH = cv2.equalizeHist(r)
# # 合并每一个通道
# result = cv2.merge((bH, gH, rH))
# cv2.imshow("dst_rgb", result)
#
# cv2.waitKey(0)








