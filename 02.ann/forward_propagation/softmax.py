# Import
import numpy as np

# Global Variables

# Classes

# Functions
def softmax(a):
	exp_a = np.exp(a)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y

def main():
	a = np.array([0.3, 2.9, 4.0])
	y = softmax(a)
	print(y)

if __name__ == '__main__':
	main()
