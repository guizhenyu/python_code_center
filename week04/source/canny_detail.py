import numpy  as np
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    pic_path = '/root/PycharmProjects/python_code_center/learn.jpg'
    img = plt.imread(pic_path)
    if pic_path[-4:] == '.png':
        img = img * 255
    img = img.mean(axis=-1)

    sigma = 1.52
    dim = int(np.round(6 * sigma + 1))
    if dim % 2 == 0:
        dim += 1
    Gaussian_filter = np.zeros([dim, dim])
    tmp = [i -dim / 2 for i in range(dim)]
    n1 = 1 / (2 * math.pi * sigma**2)
    n2 = -1 /(2 * sigma**2)
    for i in range(dim):
        for j in range(dim):
            Gaussian_filter[i,j] = n1*math.exp(n2*(tmp[i]**2 + tmp[j]**2))
    Gaussian_filter = Gaussian_filter / Gaussian_filter.sum()
    dx, dy = img.shape
    img_new = np.zeros(img.shape)
    tmp = dim//2
    img_pad = np.pad(img, ((tmp, tmp),(tmp, tmp)), 'constant')
    for i in range(dx):
        for j in range(dy):
            img_new[i, j] = np.sum(img_pad[i:i+dim, j:j+dim] * Gaussian_filter)
    plt.figure(1)
    plt.imshow(img_new.astype(np.uint8), cmap='gray')
    plt.axis('off')

    sobel_kernel_x = np.array([[-1, 0, 1], [-2,0,2],[-1,0,1]])
    sobel_kernel_y = np.array([[1,2,2], [0,0,0],[-1,-2,-1]])
    img_tidu_x = np.zeros(img_new.shape)
    img_tidu_y = np.zeros([dx, dy])
    img_tidu = np.zeros(img_new.shape)
    img_pad = np.pad(img_new, ((1,1),(1,1)), 'constant')
    for i in range(dx):
        for j in range(dy):
            img_tidu_x[i,j] = np.sum(img_pad[i:i+3,j:j+3] * sobel_kernel_x)
            img_tidu_y[i,j] = np.sum(img_pad[i:i+3,j:j+3] * sobel_kernel_y)
            img_tidu[i,j] = np.sqrt(img_tidu_x[i,j]**2 + img_tidu_y[i,j] ** 2)
    img_tidu_x[img_tidu_x == 0] = 0.00000001
    angle = img_tidu_y / img_tidu_x
    plt.figure(2)
    plt.imshow(img_tidu.astype(np.unit8), cmap= 'gray')
    plt.axis('off')

    # non-maximum suppression
    img_nms = np.zeros(img_tidu.shape)
    for i in range(1, dx-1):
        for j in range(1, dy-1):
            flag = True
            temp = img_tidu[i-1:i+2,j-1:j+2]
            if angle[i,j] <= -1:
                num1 = (temp[0,1] - temp[0,0]) / angle[i,j] + temp[0,1]
                num2 = (temp[2,2] - temp[2,1]) / angle[i,j] + temp[2,1]
                if num1 >= img_tidu[i,j] or num2 >= img_tidu[i, j]:
                    flag =False
            elif angle[i,j] >= 1:
                num1 = (temp[0,2] - temp[0,1]) / angle[i,j] + temp[0,1]
                num2 = (temp[2,0] - temp[2,1]) / angle[i,j] + temp[2,1]
                if num1 >= img_tidu[i, j] or num2 >= img_tidu[i, j]:
                    flag = False
            elif angle[i,j] < 0:
                num1 = (temp[1,0] - temp[0,0]) * angle[i,j] + temp[1,0]
                num2 = (temp[2,2] - temp[1,2]) * angle[i,j] + temp[1,2]
                if num1 >= img_tidu[i,j] or num2 >= img_tidu[i, j]:
                    flag =False
            elif angle[i,j] > 0:
                num1 = (temp[0,2] - temp[1,2]) * angle[i,j] + temp[1,2]
                num2 = (temp[1,0] - temp[2,0]) * angle[i,j] + temp[1,0]
                if num1 >= img_tidu[i,j] or num2 >= img_tidu[i, j]:
                    flag =False
            if flag:
                img_nms[i,j] = img_tidu[i,j]
    plt.figure(3)
    plt.imshow(img_nms.astype(np.uint8), cmap='gray')
    plt.axis('off')

    lower_boundary = img_tidu.mean() * 0.5
    high_boundary = lower_boundary * 3
    zhan= []
    for i in range(1, img_nms.shape[0]-1):
        for j in range(1, img_nms.shape[1]-1):
            if img_nms[i,j] >= high_boundary:
                img_nms[i,j] = 255
                zhan.append([i,j])
            if img_nms[i,j] <= lower_boundary:
                img_nms[i,j] = 0

    while not len(zhan) == 0:
        temp1, temp2 = zhan.pop()
        a = img_nms[temp1 -1: temp1 +2, temp2 - 1 : temp2 + 2]
        if a[0,0] > lower_boundary and a[0,0] < high_boundary:
            img_nms[temp1 - 1, temp2 - 1] = 255
            zhan.append([temp1 - 1, temp2 - 1])
        if a[0, 1] > lower_boundary and a[0, 1] < high_boundary:
            img_nms[temp1 - 1, temp2] = 255
            zhan.append([temp1 - 1, temp2])
        if a[0, 2] > lower_boundary and a[0, 2] < high_boundary:
            img_nms[temp1 - 1, temp2 + 1] = 255
            zhan.append([temp1 - 1, temp2 + 1])
        if a[1, 0] > lower_boundary and a[1, 0] < high_boundary:
            img_nms[temp1, temp2 -1] = 255
            zhan.append([temp1, temp2-1])
        if a[1, 2] > lower_boundary and a[1,2] < high_boundary:
            img_nms[temp1, temp2 + 1] = 255
            zhan.append([temp1, temp2 + 1])
        if a[2, 0] > lower_boundary and a[2, 0] < high_boundary:
            img_nms[temp1 + 1, temp2 - 1] = 255
            zhan.append([temp1 + 1, temp2 - 1])
        if a[2, 1] > lower_boundary and a[2, 1] < high_boundary:
            img_nms[temp1 + 1, temp2] = 255
            zhan.append([temp1 + 1, temp2])
        if a[2, 2] > lower_boundary and a[2, 2] < high_boundary:
            img_nms[temp1 + 1, temp2 + 1] = 255
            zhan.append([temp1 + 1, temp2 + 1])
    for i in range(img_nms.shape[0]):
        for j in range(img_nms.shape[1]):
            if img_nms[i,j] != 0 and img_nms[i,j] != 255:
                img_nms[i,j] = 0

    plt.figure(4)
    plt.imshow(img_nms.astype(np.uint8), cmap='gray')
    plt.axis('off')
    plt.show()