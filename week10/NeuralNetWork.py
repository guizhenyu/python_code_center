import numpy
import scipy.special

class NeuralNetWork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # initailize nerual work, set inputnodes, hiddennodes, outputnodes, learningrate
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.lr = learningrate

        self.wih = (numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes)))
        self.who = (numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes)))

        self.activation_function = lambda x:scipy.special.expit(x)

        pass

    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)

        final_outputs = self.activation_function(final_inputs)

        #caculate error
        output_error = targets_list - final_inputs
        hidden_errors = numpy.dot(self.who.T, output_error)

        self.who += self.lr * numpy.dot((output_error * final_outputs * (1 - final_outputs)),
                                        numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    def query(self,inputs):
        hidden_inputs = numpy.dot(self.wih, inputs)

        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs =  numpy.dot(self.who, hidden_outputs)

        final_outputs = self.activation_function(final_inputs)

        print(final_outputs)
        return final_outputs

# initalize nural network
input_nodes = 784
hidden_nodes = 200
output_nodes = 10
learningg_rate =  0.1
n = NeuralNetWork(input_nodes, hidden_nodes, output_nodes, learningg_rate)

#read training data
training_data_file = open("dataset/mnist_train")
training_data_list = training_data_file.readlines()
training_data_file.close()

epochs = 5
for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:])) / 255 * 0.99 + 0.01
        # set the relationship between image and number
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)

test_data_file = open("dataset/mnist_test.csv")
test_data_list = test_data_file.readlines()
test_data_file.close()
scores = []
for record in test_data_list:
    all_values = record.strip().split(',')
    target = int(all_values[0])

    inputs = (numpy.asfarray(all_values[1:])) / 255 * 0.99 + 0.01
    test_result = n.query(inputs)
    label = numpy.argmax(test_result)

    print("the recognition result of neural network is ", label)
    if target == label:
        scores.append(1)
    else:
        scores.append(0)
    print(scores)

scores_arry = numpy.asfarray(scores)
print("perfermances = ", scores_arry.sum()/ scores_arry.size )


