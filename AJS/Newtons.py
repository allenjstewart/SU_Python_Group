# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:10:16 2018

@author: allen
"""

import scipy as sp
import sympy as syp
import numpy as np
import math as math
import random as rand

def NewSolve(f,var,point,steps):
	J=[]
	for i in range(0,len(f)):
		J.append([])
	for m in range(0,len(f)):
		for n in range(0,len(var)):
			J[m].append(syp.diff(f[m],var[n]))
	Jpoint=np.zeros([len(f),len(var)])
	varpoint=[]
	numpoint=point
	fnumpoint=point
	for _ in range(0,steps):
		for k in range(0,len(point)):
			varpoint.append((var[k],numpoint[k]))
		if (len(varpoint)>len(point)):
			varpoint=varpoint[len(point):2*len(point)]	
		for k in range(0, len(point)):
			fnumpoint[k]=syp.sympify(f[k]).subs(varpoint)
		for m in range(0,len(f)):
			for n in range(0,len(var)):
				Jpoint[m][n]=J[m][n].subs(varpoint)
		numpoint=numpoint-np.dot(np.linalg.inv(Jpoint),fnumpoint)
	return numpoint			
		
		
	