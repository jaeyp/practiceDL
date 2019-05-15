# Import
import numpy as np
import matplotlib.pylab as plt

# Global Variables

# Classes

# Functions
def relu(x):
	return np.maximum(0, x)

def main():
	X = np.arange(-5.0, 5.0, 0.1)
	Y = relu(X)
	plt.plot(X, Y)
	plt.ylim(-1.0, 5.5)
	plt.show()

if __name__ == '__main__':
	main()
