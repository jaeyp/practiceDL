# Import
import numpy as np

# Global Variables

# Classes

# Functions
def multiply_ex1():
	print("--------------------------");
	print("Example 1. [2x3] x [3x2] = [2x2]")
	A = np.array([[1,2,3], [4,5,6]])
	print(A)
	print("shape: " + str(A.shape))
	
	B = np.array([[1,2], [3,4], [5,6]])
	print(B)
	print("shape: " + str(B.shape))
	
	Y = np.dot(A, B)
	print(Y)
	print("shape: " + str(Y.shape))

def multiply_ex2():
	print("--------------------------");
	print("Example 2. [3x2] x [2x1] = [3x1]")
	A = np.array([[1,2], [3,4], [5,6]])
	print(A)
	print("shape: " + str(A.shape))
	
	B = np.array([7,8])
	print(B)
	print("shape: " + str(B.shape))
	
	Y = np.dot(A, B)
	print(Y)
	print("shape: " + str(Y.shape))

def multiply_ex3():
	print("--------------------------");
	print("Example 3. [1x2] x [2x3] = [1x3]")
	A = np.array([1,2])
	print(A)
	print("shape: " + str(A.shape))
	
	B = np.array([[1,3,5], [2,4,6]])
	print(B)
	print("shape: " + str(B.shape))
	
	Y = np.dot(A, B)
	print(Y)
	print("shape: " + str(Y.shape))

def main():
	print("--------------------------");
	print("multiplication of matrices")
	multiply_ex1()
	multiply_ex2()
	multiply_ex3()


if __name__ == '__main__':
	main()
