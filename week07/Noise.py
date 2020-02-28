import cv2 as cv
import numpy  as np
from PIL import Image
from skimage import util

img_path = "/root/PycharmProjects/python_code_center/learn.jpg"
img = cv.imread(img_path)
# noise_img = util.random_noise(img, mode='gaussian')
# noise_img = util.random_noise(img, mode='gaussian')
noise_img = util.random_noise(img, mode='s&p')

cv.imshow("source", img)
cv.imshow("lenna_noise", noise_img)
cv.waitKey(0)
cv.destroyAllWindows()