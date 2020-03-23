import tensorflow as tf

#定义一个计算图， 实现两个向量的减法操作
#定义两个输入，a为常量，b为变量
a=tf.constant([10.0, 20.0, 40.0],name='a')
b=tf.variable(tf.random_uniform([3]), name='b')
ootput=tf.add_n([a,b], name='add')

writer = tf.summary.FileWriter('logs', tf.get_default_graph())
writer.close()
