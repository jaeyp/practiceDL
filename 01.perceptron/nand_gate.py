# Imports
import numpy as np

# Global Variables
samples = [(0,0), (1,0), (0,1), (1,1)]

# Classes

# Functions
def step_function(x):
	if x > 0:
		return 0
	else:
		return 1

def NAND(x1, x2):
	x = np.array([x1, x2])
	weight = np.array([0.5, 0.5])
	bias = -0.7
	tmp = np.sum(x*weight) + bias
	return step_function(tmp)

def main():
	for xs in samples:
		y = NAND(xs[0], xs[1])
		print(str(xs) + " -> " + str(y))

if __name__ == '__main__':
	main()
