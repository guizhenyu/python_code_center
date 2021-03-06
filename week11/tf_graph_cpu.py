import tensorflow as tf

with tf.device('/cpu:0'):
    a = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0], shape=[2,3], name='a')
    b = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0], shape=[3,2], name='b')

print(a)

print(b)
c = tf.matmul(a,b, name='mul')

sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement = True))

print(sess.run(c))

sess.close()