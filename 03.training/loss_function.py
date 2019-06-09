# Imports
import numpy as np

# Gloval Variables

# Classes

# Functions
def mean_squared_error(y, t):
	return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
	delta = 1e-7
	return -np.sum(t * np.log(y + delta))

def main():
	# actual value
	t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
	# predicted value (right prediction)
	y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
	# predicted value (wrong prediction)
	y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

	print('[loss function with right prediction]')
	print(f'mean squared error: {mean_squared_error(np.array(y1), np.array(t))}')
	print(f'cross entropy error: {cross_entropy_error(np.array(y1), np.array(t))}')

	print('\n[loss function with wrong prediction]')
	print(f'mean squared error: {mean_squared_error(np.array(y2), np.array(t))}')
	print(f'cross entropy error: {cross_entropy_error(np.array(y2), np.array(t))}')

if __name__ == '__main__':
	main()
