# Import
import numpy as np

# Global Variables

# Classes

# Functions
def softmax(a):
	print("------------------------")
	print("input: " + str(a))
	exp_a = np.exp(a)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y

def softmax_modified(a):
	c = np.max(a)			# set maximum value within inputs
	print("------------------------")
	print("input: " + str(a-c))
	exp_a = np.exp(a - c)	# to prevent overflow
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y

def main():
	a = np.array([1010, 1000, 990])
	y = softmax(a)
	print(y)
	y = softmax_modified(a)
	print(y)

if __name__ == '__main__':
	main()
