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
	arr = np.array([])
	classific = np.array([])
	for t in range(0,n):
		x1 = random.uniform(0,1)
		y1 = random.uniform(0,1)
		if ((a*x1 + b) > y1):
			spec = 1
		else:
			spec = -1
		arr.append(np.array([x1, y1, 1]))
		classific.append(spec)
	return (arr,classific)

def create_test_data (n):
	test_data = np.array([])
	for t in range (0,n):
		x1 = random.uniform(0,1)
		x2 = random.uniform(0,1)
		test_data.append([x1,x2,1])
	return test_data

def find_error (w, line, data):
	sum = 0
	for t in range(10000):
		if (sign_custom(dot(data[t],w)) != sign_custom(dot(data[t],line))):
			sum+=1
	return(sum/10000.0)

def error_arr(w, line, data):
	err = []
	for t in range (5):
		err.append(find_error(w[t],line,data))
	return err

def plot_error (w1,w2,w3,w4,w5,line,test_data):
	#First generate 10 000 random data points
	y_data = error_arr([w1,w2,w3,w4,w5], line, test_data)
	x_data = [100,200,300,400,500]
	plt.figure(2)
	plt.plot(x_data,y_data,'r')
	plt.show()

def trim_list(lis):
	sorting = sorted(lis)
	sorting = sorting[5:-5]
	#del sorting[94:99]
	#del sorting[0:5]
	return sorting

def plot_average(line, test_data):
	err = []
	for t in range (100):
		data = generate_dataset(1,0.1,500)
		w1 = perceptron(data,100)
		w2 = perceptron(data,200) 
		w3 = perceptron(data,300)
		w4 = perceptron(data,400)
		w5 = perceptron(data,500)
		err.append(error_arr([w1,w2,w3,w4,w5], line, test_data))
	err1 = trim_list([(x[0]) for x in err])
	err2 = trim_list([(x[1]) for x in err])
	err3 = trim_list([(x[2]) for x in err])
	err4 = trim_list([(x[3]) for x in err])
	err5 = trim_list([(x[4]) for x in err]) #These lists have only 90 elements
	err_summed = [sum(i)/100 for i in zip(*err)]
	x_data = [100,200,300,400,500]
	err_conf = [err1,err2,err3,err4,err5]
	val1=val2=val3=val4=val5=0
	print len(err1)
	for h in range(len(err1)):
		val1 += err1[h]
		val2 += err2[h]
		val3 += err3[h]
		val4 += err4[h]
		val5 += err5[h]
	#plt.plot(x_data,[val1/90,val2/90,val3/90,val4/90,val5/90],c ='gray')
	plt.figure(3)
	plt.plot(x_data,[err1[0],err2[0],err3[0],err4[0],err5[0]], c='gray')
	plt.plot(x_data,[err1[89],err2[89],err3[89],err4[89],err5[89]], c='gray')
	plt.plot(x_data,err_summed,'r')
	plt.show()
	#print err

def plot_points (datapoints, line):
	x_val = [(x[0][0]) for x in datapoints]		#x coordinates
	y_val = [(x[0][1]) for x in datapoints]		#y coordinates
	z_val = [(x[1]) for x in datapoints]		#correct classification
	
	plt.figure(1)
	plt.scatter(x_val, y_val,c = z_val,cmap='jet', s=8)

	something = [0,1]
	vals = map(lambda x: ((-line[0]*x) - line[2])/line[1],something)
	plt.plot(something,vals,'black')
	plt.plot(something,[0.1,1.1],ls='dashed',c='g')
	plt.show()

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
	data = generate_dataset(1,0.1,500)
	w1 = perceptron(data,100)
	w2 = perceptron(data,200) 
	w3 = perceptron(data,300)
	w4 = perceptron(data,400)
	w5 = perceptron(data,500)
	line = np.array([1,-1,0.1])
	test_data = create_test_data(10000)
	plot_average(line,test_data)
	plot_points(data, w5)
	plot_error (w1,w2,w3,w4,w5,line,test_data)
	
    #print data
    #print train
    #plot_points(data, w5)
   	
    #values, result = generate_dataset(1, 0, 10)
    #print values
    #print result

main()

# or plot with: plot_url = py.plot(data, filename='basic-line')