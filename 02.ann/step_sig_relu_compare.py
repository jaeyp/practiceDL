# Import
import numpy as np
import matplotlib.pylab as plt

# Global Variables

# Classes

# Functions
def step_function(x):
	return np.array(x > 0, dtype=np.int)

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def relu(x):
	return np.maximum(0, x)

def leaky_relu(x):
	return np.maximum(0.01*x, x)

def main():
	x = np.arange(-5.0, 5.0, 0.1)
	y1 = step_function(x)
	y2 = sigmoid(x)
	y3 = relu(x)
	y4 = leaky_relu(x)

	plt.plot(x, y1, 'k--', label='step function')
	plt.plot(x, y2, label='sigmoid')
	plt.plot(x, y3, 'b-', label='ReLU')
	plt.plot(x, y4, 'r:', label='leaky ReLU')
	plt.ylim(-0.1, 1.1)
	plt.legend()
	plt.show()

if __name__ == '__main__':
	main()
