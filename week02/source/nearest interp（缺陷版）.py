
import cv2
import numpy as np
def function(img):
    height,width,channels =img.shape
    emptyImage=np.zeros((700,700,channels),np.uint8)
    sh=700/height
    sw=700/width
    for i in range(700):
        for j in range(700):
            x=int(i/sh)
            y=int(j/sw)
            emptyImage[i,j]=img[x,y]
    return emptyImage

img=cv2.imread("lenna.png")
zoom=function(img)
cv2.imshow("nearest interp",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)

