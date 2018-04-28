# Author: AJ Stewart
# This code uses multivariable Newton's method to solve a system of equations
#
#####################################
# Variables
# f= list of equations inputed as strings
# var= list of variables inputed as strings
# point= list of initial values
# steps= the number of steps to iterate
#
#####################################
#
# I'm wasting my time
# Writing haikus in my code
# Are you reading this?
#####################################

import scipy as sp #Probably don't need this, but...
import sympy as syp #Definitely need this. It's used to define the Jacobian
import numpy as np #At some point I use vectors or lists or whatever
import math as math #Just in case someone loves trig functions
import random as rand # At some point I'll worry about pathological things

def NewSolve(f,var,point,steps):
#Initialize the Jacobian as an empty list
	J=[]
	for i in range(0,len(f)):
		J.append([])
#Use sympy to differentiate expressions in f
#And append the derivatives into the empty Jacobian
	for m in range(0,len(f)):
		for n in range(0,len(var)):
			J[m].append(syp.diff(f[m],var[n]))
#Create a numerical 0-matrix that will eventually be used to evaluate the Jacobian.
#This is because J is an array of sympy objects that aren't numerical
	Jpoint=np.zeros([len(f),len(var)])
#Create an empty list to input tuples of variables
#This will be use to evalute the expressions in f
	varpoint=[]
#initialize the x and f values
	numpoint=point
	fnumpoint=point
	for _ in range(0,steps):
		for k in range(0,len(point)):
#create the list of tuples for evaluation
			varpoint.append((var[k],numpoint[k]))
		if (len(varpoint)>len(point)):
#I'm appended the tuples to varpoint
#I can't redefine varpoint as empty once values have been appended
#So I need to keep chopping of the first portion of varpoint
#In order to keep varpoint at the correct length
			varpoint=varpoint[len(point):2*len(point)]
		for k in range(0, len(point
#Create the vector of f values
#Evaluate the kth function in f at the variable values defined by varpoint
#Should be noted that sympify uses eval which runs strings as python Code
			fnumpoint[k]=syp.sympify(f[k]).subs(varpoint)
		for m in range(0,len(f)):
			for n in range(0,len(var)):
#Evaluate the Jacobian at the variables value defined by varpoint
				Jpoint[m][n]=J[m][n].subs(varpoint)
#Newton's Method
		numpoint=numpoint-np.dot(np.linalg.inv(Jpoint),fnumpoint)
	return numpoint
