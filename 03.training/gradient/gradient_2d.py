import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def _numerical_gradient_no_batch(f, x):
	h = 1e-4  # 0.0001
	grad = np.zeros_like(x)

	for idx in range(x.size):
		tmp_val = x[idx]
		x[idx] = tmp_val + h
		print(f'tmp_x: {x[idx]}')
		fxh1 = f(x)	# f(x+h)
		print(f'tmp_y: {fxh1}')

		x[idx] = tmp_val - h
		fxh2 = f(x) # f(x-h)

		grad[idx] = (fxh1 - fxh2) / (2*h)
		print(f'grad: {grad[idx]}')
		x[idx] = tmp_val

	return grad


def numerical_gradient(f, X):
	# X: 18x18 (total 324 points)
	print(f'X.ndim: {X.ndim} X.shape: {X.shape}')
	if X.ndim == 1:
		return _numerical_gradient_no_batch(f, X)
	else:
		grad = np.zeros_like(X)

		for idx, x in enumerate(X):
			print(f'idx: {idx} x: {x}')
			grad[idx] = _numerical_gradient_no_batch(f, x)

		return grad

# f(x0, x1) = x0**2 + x1**2
def function_2(x):
	if x.ndim == 1:
		print(f'func2_x(dim.1): {x}')
		return np.sum(x**2)	# x[0]**2 + x[1]**2
	else:
		print(f'func2_x(dim.2): {x}')
		return np.sum(x**2, axis=1)


def tangent_line(f, x):
	d = numerical_gradient(f, x)
	print(d)
	y = f(x) - d*x
	return lambda t: d*t + y


if __name__ == '__main__':
	x0 = np.arange(-2, 2.5, 0.25)	# 4.5 / 0.25 = total 18 points
	x1 = np.arange(-2, 2.5, 0.25)	# 4.5 / 0.25 = total 18 points
	X, Y = np.meshgrid(x0, x1)

	X = X.flatten()
	Y = Y.flatten()

	grad = numerical_gradient(function_2, np.array([X, Y]).T).T

	plt.figure()
	plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")
	plt.xlim([-2, 2])
	plt.ylim([-2, 2])
	plt.xlabel('x0')
	plt.ylabel('x1')
	plt.grid()
	plt.draw()
	plt.show()

