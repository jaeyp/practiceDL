# Import
import numpy as np

# Global Variables

# Classes

# Functions
def main():
	A = np.array([1, 2, 3, 4])				# 1d matrix
	print(A)
	print("dimention: " + str(np.ndim(A)))	# number of dimention
	print("shape: " + str(A.shape))			# output is tuple
	print(A.shape[0])

	B = np.array([[1,2], [3,4], [5,6]])		# 2d matrix (3x2)
	print(B)
	print("dimention: " + str(np.ndim(B)))	# number of dimention
	print("shape: " + str(B.shape))			# output is tuple

if __name__ == '__main__':
	main()
