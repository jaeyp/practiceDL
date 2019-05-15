# Imporat
import sys, os
project_root = os.path.abspath(os.path.dirname(__file__) + "../../")
sys.path.append(project_root)
import numpy as np
import pickle
import timeit	# check performance
from dataset.mnist import load_mnist

# Global Variables

# Classes

# Functions
def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def softmax(a):
	c = np.max(a)
	exp_a = np.exp(a - c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y

def get_data():
	(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
	return x_test, t_test


def init_network():
	with open("sample_weight.pkl", 'rb') as f:
		network = pickle.load(f)
	return network


def predict(network, x): 
	W1, W2, W3 = network['W1'], network['W2'], network['W3']
	b1, b2, b3 = network['b1'], network['b2'], network['b3']

	a1 = np.dot(x, W1) + b1
	z1 = sigmoid(a1)
	a2 = np.dot(z1, W2) + b2
	z2 = sigmoid(a2)
	a3 = np.dot(z2, W3) + b3
	y = softmax(a3)
	return y

def main():
	x, t = get_data()
	network = init_network()
	batch_size = 100
	accuracy_cnt = 0

	start = timeit.default_timer()	# check performance
	for i in range(0, len(x), batch_size):
		x_batch = x[i:i+batch_size]
		y_batch = predict(network, x_batch)
		p = np.argmax(y_batch, axis=1)
		accuracy_cnt += np.sum(p == t[i:i+batch_size])
	stop = timeit.default_timer()	# check performance
	print("=============================")
	print("Total elapsed time: " + str(stop - start) + " seconds")
	print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

if __name__ == '__main__':
	main()
