# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:06:10 2018

@author: allen
"""

import scipy as sp
import numpy as np
import math as m
import random as rand

def trapezoid(f,a, b, e):
	prevApprox=(b-a)*f((b-a)*rand.random()+a)
	Approx=(b-a)*f((b-a)*rand.random()+a)
	n=1
	count=0
	while (abs(Approx-prevApprox)>e):
		n=2*n
		count=count+1
		prevApprox=Approx
		Approx=0
		for i in range(0,n):
			h = (b-a)/n
			Approx+= 0.5*(f(a+i*h)+f(a+(i+1)*h))*h		
	return Approx,count

trapezoid(lambda x:2*x,6,7,.01)