# Import
import numpy as np
import matplotlib.pylab as plt

# Global Variables

# Classes

# Functions
def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def main():
	X = np.arange(-5.0, 5.0, 0.1)
	Y = sigmoid(X)
	plt.plot(X, Y)			# draw graph
	plt.ylim(-0.1, 1.1)		# set y-axis boundary
	plt.show()				# display graph

if __name__ == '__main__':
	main()

