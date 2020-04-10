import tensorflow as tf

# a = tf.constant([[1, 1], [2, 2], [3, 3]], dtype=tf.float32)
# b = tf.constant([1, -1], dtype=tf.float32)
# c = tf.constant([1], dtype=tf.float32)
#
# with tf.Session() as sess:
#     print('bias_add: a+b')
#     print(sess.run(tf.nn.bias_add(a, b)))
#     # 执行下面语句错误
#     # print(sess.run(tf.nn.bias_add(a, c)))
#
#     print('add: a+c')
#     print(sess.run(tf.add(a, c)))
#
#     print('add: a+b')
#     print(sess.run(tf.add(a, b)))

tf.add_to_collection("loss", "123")
tf.add_to_collection("loss", "1234")

# create two matrixes

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],
                       [2]])

product = tf.matmul(matrix1,matrix2)
session = tf.Session()
print(session.run(product))