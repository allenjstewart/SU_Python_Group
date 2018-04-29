# Author: AJ Stewart
# This code uses the trapezoid method to approximate a definite integral
# Also this code does not require a specified number of sub intervals
# Instead the user enters an error and subintervals are added until
# Two adjacent approximations are within the error of eachother
#
#####################################
# Variables
# f= a lambda type function
# a,b= real numbers a<b
# e=the desired maximum error for the integral
#
#####################################
#
# I wrote this code first
# But writing comments second
# Are you entertained?
#####################################

import scipy as sp #Do I need this?
import numpy as np #Seems like I don't need this either...
import math as m #Probably need this in case someone inputs a strange function
import random as rand #At some point I will make this code more effective with singular points

def trapezoid(f,a, b, e):
#Initialize two random rectangular approximations of the integral
	prevApprox=(b-a)*f((b-a)*rand.random()+a)
	Approx=(b-a)*f((b-a)*rand.random()+a)
#Initialize the number of subintervals
	n=1
	count=0
#The loop will run while the two approximations differ by
#A value greater that the user given error
	while (abs(Approx-prevApprox)>e):
		n=2*n
		count=count+1
		prevApprox=Approx
		Approx=0
		for i in range(0,n):
			h = (b-a)/n
			Approx+= 0.5*(f(a+i*h)+f(a+(i+1)*h))*h
		if count>1000000000:
			raise ValueError("Woah, dude. What happened?")
			
#Return the approximation along with the number of loops run.
	return Approx,count
