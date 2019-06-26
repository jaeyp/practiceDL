## Imports
import sys, os
project_root = os.path.abspath(os.path.dirname(__file__) + "../..")
sys.path.append(project_root)
import numpy as np
import pickle
import timeit
from dataset.mnist import load_mnist

## Gloval Variables

## Classes

## MNIST Function
def init_network():
	with open("sample_weight.pkl", 'rb') as f:
		network = pickle.load(f)	# get weight and bias
	return network

def get_data():
	(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
	return x_test, t_test

## Activation Function
def sigmoid(x):
	return 1 / (1 + np.exp(-x))

## Identity Function
def softmax(a):
	c = np.max(a)
	exp_a = np.exp(a - c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y

## Loss Functions
'''
y: predicted values
t: actual values
'''
def mean_squared_error(y, t):
	#return (1/t.size * np.sum((y-t)**2)
	return np.mean((y-t)**2)
mse = mean_squared_error	# alias

def mean_squared_logarithmic_error(y, t):
	return np.mean((np.log(y+1)-np.log(t+1))**2)
msle = mean_squared_logarithmic_error

def mean_absolute_error(y, t):
	return np.mean(np.absolute(y-t))
mae = mean_absolute_error

def mean_absolute_percentage_error(y, t):
	return np.mean(np.absolute((y-t)/y)*100)
mape = mean_absolute_percentage_error

def cross_entropy_error(y, t):
	delta = 1e-7 # we add a very small value (0.0000007) to y in order to prevent -inf where y is 0
	return -np.sum(t * np.log(y + delta))
#	return -np.sum(t * np.log(y + delta) + (1-t)*np.log(1-y + delta))
cee = cross_entropy_error

def log_likelihood_error(y, t):
	return 
lle = log_likelihood_error

## Forward Propagation
def predict(network, x):
	W1, W2, W3 = network['W1'], network['W2'], network['W3']    # weight
	b1, b2, b3 = network['b1'], network['b2'], network['b3']    # bias

	a1 = np.dot(x, W1) + b1
#	print(f'x: {x.shape}')
#	print(f'W1: {W1.shape}')
	z1 = sigmoid(a1)    # activation
	a2 = np.dot(z1, W2) + b2
#	print(f'z1: {z1.shape}')
#	print(f'W2: {W2.shape}')
	z2 = sigmoid(a2)    # activation
	a3 = np.dot(z2, W3) + b3
#	print(f'z2: {z2.shape}')
#	print(f'W3: {W3.shape}')
	y = softmax(a3)     # identity function
#	print(f'y: {y.shape}')
	return y


def main():
	x, t = get_data()
	network = init_network()
	batch_size = 100	# increase cache hits (spatial locality)
	total_correct_answers = 0

#	start = timeit.default_timer()	# check performance
	for i in range(0, len(x), batch_size):
		x_batch = x[i:i+batch_size]
		t_batch = t[i:i+batch_size]
		y_batch = predict(network, x_batch)
		p = np.argmax(y_batch, axis=1)
		correct_answers = np.sum(p == t_batch)
		total_correct_answers += correct_answers

		print(f'SAMPLE[{i}]------------')
		print(f'MSE:  {mse(p, t_batch)}')
		print('MSLE: ' + '{0:.5f}'.format(msle(p, t_batch)))
		print(f'MAE:  {mae(p, t_batch)}')
		print('CEE:  ' + '{0:.5f}'.format(cee(p, t_batch)))
		print(f'accuracy: {correct_answers}/{batch_size}')
#		print(f'{p==t_batch}')
#		print(f'y: {p}')		# predicted value
#		print(f't: {t_batch}')	# actual value

#	stop = timeit.default_timer()
	print("=============================")
#	print("Total elapsed time: " + str('{0:.5f}'.format(stop - start)) + " seconds")
	print("Total accuracy: " + str('{0:.5f}'.format((float(total_correct_answers) / len(x)) * 100)) + " %")

if __name__ == '__main__':
	main()
