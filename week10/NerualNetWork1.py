import numpy
import scipy.special

class NerualNetWork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #初始化网络，设置输入层，隐层，输出层的节点数
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # 初始化学习率
        self.lr = learningrate

        '''
        初始化权重矩阵，我们有两个权重矩阵
        wih 表示输入层和中间层节点间的链路权重形成的矩阵
        who 表示中间层和输出层节点间的链路权重形成的矩阵
        numpy.random.normal(centre, scale, size)
        centre 正态分布的均值
        scale 正太分布的标准差（方差均值）
        size: int or touple of ints
        '''

        self.wih = (numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes)))

        self.who = (numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.hnodes, self.hnodes)))


        '''
        activate function
        '''
        self.activation = lambda x:scipy.special.expit(x)

    '''
    :param inputs_list: 
    :param target_list: 
    :return: 
    '''
    def train(self, inputs_list, target_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(target_list, ndmin=2).T

        hidden_inputs = numpy.dot(inputs_list, self.wih)

        hidden_outputs = self.activation(hidden_inputs)

        final_inputs = numpy.dot(hidden_outputs, self.who)

        final_outputs = self.activation(final_inputs)

        outputs_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, outputs_errors)

        self.who += self.lr * numpy.dot(outputs_errors * final_outputs * ( 1 - final_outputs),
                             numpy.transpose(hidden_outputs))

        self.wih += self.lr * numpy.dot(hidden_errors * hidden_outputs * (1 - hidden_errors),
                                        numpy.transpose(inputs))

        pass

