'''
Script for Calculating the Pearson Correlation Coefficient, aka, a normalized 
covariance rating between -1 and 1.
'''
import math as m

#literally takes the average
def mean(X):
	bar = 0
	for num in X:
		bar += num
	return bar/len(X)

def distance(value, mean):
    return value - mean

def squareDistance(value, mean):
    return (distance(value,mean))**2

def covariance(X, Y):
	total = 0
	n = len(X)
	for num in range(n):
		total += (distance(X[num], mean(X)) * distance(Y[num],mean(Y)))
	return total

def standardDeviation(array):
#Note: this version of SD only works in the context of the PCC. It ignores 
#dividing by n-1 for samples and n for entire populations
    total = 0
    n = len(array)
    for num in range(n):
        total += squareDistance(array[num], mean(array))
    return m.sqrt(total)

def pearsonCC(X,Y):
    global Xbar
    Xbar = mean(X)
    global Ybar
    Ybar = mean(Y)
    return covariance(X,Y) / (standardDeviation(X) * standardDeviation(Y))
