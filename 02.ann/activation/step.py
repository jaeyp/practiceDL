# Import
import numpy as np
import matplotlib.pylab as plt

# Global Variables

# Classes

# Functions
def step_function(x):
	# 'x > 0' changes input obj's value to true/false
	# 'dtype=np.int' changes true/false to 1/0	 
	return np.array(x > 0, dtype=np.int)	

def main():
	X = np.arange(-5.0, 5.0, 0.1)
	Y = step_function(X)
	plt.plot(X, Y)
	plt.ylim(-0.1, 1.1)
	plt.show()

if __name__ == '__main__':
	main()
