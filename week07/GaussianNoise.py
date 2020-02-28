
#随机生成符合正态（高斯）分布的随机数，means,sigma为两个参数
import numpy
import cv2
from numpy import shape
import random

def GaussianNoise(src, means, sigma, percentage):
    NosieImg = src
    NoiseNum = int(percentage * src.shape[0] * src.shape[1])
    for i in range(NoiseNum):
        # 每次取一个随机点
        # 把一张图片的像素用行和列表示的话，randX 代表随机生成的行，randY代表随机生成的列
        # random.randint生成随机整数
        # 高斯噪声图片边缘不处理，故-1
        randX = random.randint(0, src.shape[0] - 1)
        randY = random.randint(0, src.shape[1] - 1)
        #此处在原有像素灰度值上加上随机数
        NosieImg[randX, randY] = NosieImg[randX, randY] + random.gauss(means, sigma)
        #若灰度值小于0则强制为0，若灰度值大于255则强制为255
        if NosieImg[randX, randY] < 0 :
            NosieImg[randX, randY] = 0
        elif NosieImg[randX, randY] > 255:
            NosieImg[randX, randY] = 255

    return NosieImg
img_path = "/root/PycharmProjects/python_code_center/learn.jpg"
img = cv2.imread(img_path, 0)
img1 = GaussianNoise(img, 4, 8, 0.5)
img = cv2.imread(img_path)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('source', img2)
cv2.imshow("lenna_GaussioanNoise", img1)
cv2.waitKey(0)