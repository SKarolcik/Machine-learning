from pylab import *
from numpy import array, dot, random
import numpy as np
from random import choice
import matplotlib.pyplot as plt

def sign_custom (x):
	if (x < 0):
		return (-1)
	else:
		return 1

def generate_dataset (a, b, n):			#generate random data points separated by the given line y = ax + b
	arr = []
	for t in range(0,n):
		x1 = random.uniform(-5,5)
		y1 = random.uniform(-5,5)
		if ((a*x1 + b) > y1):
			spec = 1
		else:
			spec = -1
		datap = np.array([x1, y1, 1])
		toup = (datap, spec)
		arr.append(toup)
	return arr

def plot_points (datapoints, line):
	x_val = [(x[0][0]) for x in datapoints]		#x coordinates
	y_val = [(x[0][1]) for x in datapoints]		#y coordinates
	z_val = [(x[1]) for x in datapoints]		#correct classification
	
	plt.scatter(x_val, y_val,c = z_val,cmap='jet', s=8)

	something = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
	vals = map(lambda x: ((-line[0]*x) - line[2])/line[1],something)
	plt.plot(something,vals,'black')
	plt.show(block=True)

def perceptron (datapoint,n):
	w = np.array([0,0,1])
	while True:
		err = 0
		for i in range (0,n):
			predict = sign_custom(dot(datapoint[i][0],w))
			if (predict != datapoint[i][1]):
				w = w + (datapoint[i][1] * datapoint[i][0])
				err = 1
		if (err == 0):
			break	 
	return w

def main():
    #plot_points(generate_dataset(1, 0, 10))
    data = generate_dataset(-2,0.5,100)
    train = perceptron(data,100)
    #print data
    #print train
    plot_points(data, train)
   	
    #values, result = generate_dataset(1, 0, 10)
    #print values
    #print result

main()

# or plot with: plot_url = py.plot(data, filename='basic-line')