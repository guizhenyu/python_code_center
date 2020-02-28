import numpy as np
import cv2
from numpy import shape
import random

def fun1(src, percentage):
    NoiseImg = src
    NosieNum = int(percentage * NoiseImg.shape[0] * NoiseImg.shape[1])
    for i in range(NosieNum):
        randX = random.randint(0, NoiseImg.shape[0] - 1)
        randY = random.randint(0, NoiseImg.shape[1] - 1)
        if random.random() <= 0.5:
            NoiseImg[randX, randY] = 0
        else:
            NoiseImg[randX, randY] = 255
    return NoiseImg

img_path = "/root/PycharmProjects/python_code_center/learn.jpg"
img = cv2.imread(img_path, 0)
img1 = fun1(img, 0.2)
img = cv2.imread(img_path)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("source", img)
cv2.imshow("PepperSaltNoise", img1)
cv2.waitKey(0)