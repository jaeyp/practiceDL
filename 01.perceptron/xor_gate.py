# Imports
from and_gate import AND
from or_gate import OR
from nand_gate import NAND

# Global Variables
samples = [(0,0), (1,0), (0,1), (1,1)]

# Classes

# Functions
def XOR(x1, x2):		# multi-layer perceptron
	s1 = NAND(x1, x2)	# layer 1
	s2 = OR(x1, x2)		# layer 1
	y = AND(s1, s2)		# layer 2
	return y

def main():
	for xs in samples:
		y = XOR(xs[0], xs[1])
		print(str(xs) + " -> " + str(y))

if __name__ == '__main__':
	main()
