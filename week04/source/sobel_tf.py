#!/usr/bin/env python
# coding=utf-8
import sys
sys.path.append("/bin/conda/envs/tensorflow/lib/python3.7/site-packages")


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import pylab

myimg = mpimg.imread("learn.jpg") # 512 * 512 * 3
print(myimg.shape)
full = np.concatenate((myimg, myimg), axis=2)
full = np.reshape(full, [1, 512, 512, 6])
inputfull = tf.Variable(tf.constant(1.0, shape=[1, 512, 512, 6]))
filter1 = tf.Variable(tf.constant([[-1.0, -1.0, -1.0], [0, 0, 0], [1.0, 1.0, 1.0],
                                   [-1.0, -1.0, -1.0], [-2.0, -2.0, -2.0], [-1.0, -1.0, -1.0],
                                   [-2.0, -2.0, -2.0], [0, 0, 0], [2.0, 2.0, 2.0],
                                   [0, 0, 0], [0, 0, 0], [0, 0, 0],
                                   [-1.0, -1.0, -1.0], [0, 0, 0], [1.0, 1.0, 1.0],
                                   [1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [1.0, 1.0, 1.0]],

                                  shape=[3, 3, 6, 1]
                                  ))

op = tf.nn.conv2d(inputfull, filter1, strides = [1, 1, 1, 1], padding='SAME')
o = tf.cast(((op - tf.reduce_min(op)) / (tf.reduce_max(op) - tf.reduce_min(op))) * 255, tf.uint8)
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    t, f = sess.run([o, filter1], feed_dict={inputfull: full})
    t = np.reshape(t, [512, 512])
    plt.imshow(t, cmap='Grey_r')
    plt.savefig('00_1.jpg')
    plt.show()