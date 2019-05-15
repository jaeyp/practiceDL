# Import
import numpy as np

# Global Variables
samples = [(0,0), (1,0), (0,1), (1,1)]

# Classes

# Functions
def step_function(x):
	if x > 0:
		return 1
	else:
		return 0

def OR(x1, x2):
	x = np.array([x1, x2])		# input
	w = np.array([0.5, 0.5])	# weight
	b = -0.3					# bias
	tmp = np.sum(x*w) + b		# linear function
	return step_function(tmp)	# activation function (non-linear function)

def main():
	for xs in samples:
		y = OR(xs[0], xs[1])
		print(str(xs) + " -> " + str(y))

if __name__ == '__main__':
	main()




