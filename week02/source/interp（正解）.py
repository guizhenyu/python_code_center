#!/usr/bin/env python
# coding: utf-8

#说明：利用python/numpy/opencv实现图像插值法（最邻近，双线性）
#算法思路:
#       1)以彩色图的方式加载图片;
#       2)根据想要生成的图像大小，映射获取某个像素点在原始图像中的浮点数坐标;
#		3)根据浮点数坐标确定插值算法中的系数、参数；
#		4)采用不同的算法实现图像插值。


import cv2
import numpy as np
import matplotlib.pyplot as plt

def Nearest( img, bigger_height, bigger_width, channels  ):
    near_img = np.zeros( shape = ( bigger_height, bigger_width, channels ), dtype = np.uint8 )
    
    for i in range( 0, bigger_height ):
        for j in range( 0, bigger_width ):
            row = ( i / bigger_height ) * img.shape[0]
            col = ( j / bigger_width ) * img.shape[1]
            near_row =  round ( row )
            near_col = round( col )
            if near_row == img.shape[0] or near_col == img.shape[1]:
                near_row -= 1
                near_col -= 1
                
            near_img[i][j] = img[near_row][near_col]
            
    return near_img

def Bilinear( img, bigger_height, bigger_width, channels ):
    bilinear_img = np.zeros( shape = ( bigger_height, bigger_width, channels ), dtype = np.uint8 )
    
    for i in range( 0, bigger_height ):
        for j in range( 0, bigger_width ):
            row = ( i / bigger_height ) * img.shape[0]
            col = ( j / bigger_width ) * img.shape[1]
            row_int = int( row )
            col_int = int( col )
            u = row - row_int
            v = col - col_int
            if row_int == img.shape[0]-1 or col_int == img.shape[1]-1:
                row_int -= 1
                col_int -= 1
                
            bilinear_img[i][j] = (1-u)*(1-v) *img[row_int][col_int] + (1-u)*v*img[row_int][col_int+1] + u*(1-v)*img[row_int+1][col_int] + u*v*img[row_int+1][col_int+1]
            
    return bilinear_img
    
if __name__ == '__main__':
    img = cv2.imread( 'lenna.png',  cv2.IMREAD_COLOR)
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    print( img[3][3] )
    height, width, channels = img.shape
    print( height, width )
    
    bigger_height = height + 200
    bigger_width = width + 200
    print( bigger_height, bigger_width)
    
    near_img = Nearest( img, bigger_height, bigger_width, channels )
    bilinear_img = Bilinear( img, bigger_height, bigger_width, channels )
    
    plt.figure()
    plt.subplot( 2, 2, 1 )
    plt.title( 'Bilinear_Image' )
    plt.imshow( bilinear_img )
    plt.subplot( 2, 2, 2 )
    plt.title( 'Nearest_Image' )
    plt.imshow( near_img )
    plt.subplot( 2, 2, 3 )
    plt.title( 'Source_Image' )
    plt.imshow( img ) 
    plt.show()    
