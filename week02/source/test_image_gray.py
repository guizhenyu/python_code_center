# -*- coding: utf-8 -*-
"""
@author: Michael

彩色图像的灰度化、二值化
"""
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

plt.subplot(221)
img = plt.imread("lenna.png") 
plt.imshow(img)
print("---image lenna----")
print(img)
 
# 灰度化
img_gray = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gray, cmap='gray')
print("---image gray----")
print(img_gray)

# 二值化
# rows, cols = img_gray.shape
# for i in range(rows):
#     for j in range(cols):
#         if (img_gray[i, j] <= 0.5):
#             img_gray[i, j] = 0
#         else:
#             img_gray[i, j] = 1
 
img_binary = np.where(img_gray >= 0.5, 1, 0) 
print("-----imge_binary------")
print(img_binary)

plt.subplot(223) 
plt.imshow(img_binary)
plt.show()
