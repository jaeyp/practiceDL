## Imports
import numpy as np

## Gloval Variables

## Classes
# Loss Function data
class LFData:
	def __init__(self, name, c, w):
		self.name = name
		self.correct = c
		self.wrong = w
		self.diff = c / w

# Loss Function data storage
class LFDataStorage:
	current = 0
	stop = 0
	item = []

#	def __init__(self):
#		pass
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.current < self.stop:
			r = self.current
			self.current += 1
			return self.item[r]
		else:
			raise StopIteration

	def __getitem__(self, index):
		if index < self.stop:
			return self.item[index]
		else:
			raise IndexError

	# lname: loss function name
	# lc: loss with correct prediction
	# lw: loss with wrong prediction
	def insert(self, name, c, w):
		self.item.append(LFData(name, c, w))
		self.stop += 1

## Functions
'''
y: predicted values
t: actual values
'''
def mean_squared_error(y, t):
	#return (1/t.size * np.sum((y-t)**2)
	return np.mean((y-t)**2)
mse = mean_squared_error	# alias

def mean_squared_logarithmic_error(y, t):
	return np.mean((np.log(y+1)-np.log(t+1))**2)
msle = mean_squared_logarithmic_error

def mean_absolute_error(y, t):
	return np.mean(np.absolute(y-t))
mae = mean_absolute_error

def mean_absolute_percentage_error(y, t):
	return np.mean(np.absolute((y-t)/y)*100)
mape = mean_absolute_percentage_error

def cross_entropy_error(y, t):
	delta = 1e-7
	return -np.sum(t * np.log(y + delta))
cee = cross_entropy_error

def log_likelihood_error(y, t):
	return 
lle = log_likelihood_error

def main():
	# actual values
	t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
	# predicted values (right prediction)
	y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
	# predicted values (wrong prediction)
	y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

	lfs = LFDataStorage()
	lfs.insert('MSE',  mse(np.array(y1),  np.array(t)), mse(np.array(y2),  np.array(t)))
	lfs.insert('MSLE', msle(np.array(y1), np.array(t)), msle(np.array(y2), np.array(t)))
	lfs.insert('MAE',  mae(np.array(y1),  np.array(t)), mae(np.array(y2),  np.array(t)))
	lfs.insert('CEE',  cee(np.array(y1),  np.array(t)), cee(np.array(y2),  np.array(t)))

	for i in lfs:
		print(i.name + 
			'\tc:{0:.5f}'.format(i.correct) +	# error with correct prediction
			'  w:{0:.5f}'.format(i.wrong) + 	# error with wrong prediction
			'  d:{0:.5f}'.format(i.diff))		# error differential

#	print(lfs[1].name);	# getitem test

if __name__ == '__main__':
	main()
