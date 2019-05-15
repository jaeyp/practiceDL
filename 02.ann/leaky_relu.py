# Import
import numpy as np
import matplotlib.pylab as plt

# Global Variables

# Classes

# Functions
def leaky_relu(x):
	return np.maximum(0.01*x, x)

def main():
	X = np.arange(-10.0, 10.0, 0.1)
	Y = leaky_relu(X)
	plt.plot(X, Y)
	plt.ylim(-1.0, 11)
	plt.show()

if __name__ == '__main__':
	main()
