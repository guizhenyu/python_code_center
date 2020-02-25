import math

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pic_path = 'learn.jpg'
    img = plt.imread(pic_path)
    if pic_path[-4:] == '.png':
        img = img * 255
    img = img.mean(axis = 1)

    sigma = 1.52
    dim = int(np.round(6 * sigma + 1))

    if dim % 2 == 0:
        dim += 1
    Gaussian_filter = np.zeros([dim, dim])
    tmp = [i-dim//2 for i in range(dim)]
    n1 = 1/(2*math.pi*sigma**2)
    n2 = -1 / (2*sigma**2)
    for i in range(dim):
        for j in range(dim):
            Gaussian_filter[i, j] = n1*math.exp(n2*(tmp1[i]**2 + tmp[j]**2))
    Gaussian_filter = Gaussian_filter / Gaussian_filter.sum()
    dx, dy = img.shape
    img_new = np.zeros(img.shape)
    tmp = dim//2
    img_pad = np.pad(img, ((tmp,tmp), (tmp,tmp)), 'constant')
    for i in range(dx):
        for j in range(dy):
            img_new[i,j] = np.sum(img_pad[i:i+dim, j:j+dim]*Gaussian_filter)
    plt.figure(1)
    plt.imshow(img_new.astype(np.uint8), cmap='gray')
    plt.axis('off')
