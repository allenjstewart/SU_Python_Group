# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 21:56:39 2018

@author: Joey
"""

# AUTHOR: J. Nakao
# DATE: 1 May 2018
# PURPOSE: Solve ODEs and systems of ODEs with Euler's method and RK4.
# INSTRUCTIONS: 



import numpy as np
import time as tm
import array as ay
import matplotlib.pyplot as plt

##########################################################
def f(t,y):
    return t - y #y'=f(t,y).
t0 = 0 #initial time.
y0 = 4 #initial condition.
tf = 10 #final time.
N = 10000 #number of steps.
h = (tf-t0)/N #step size.
##########################################################

# Euler's method for first-order ODEs.
def Euler(t0,y0,h):
    tic = tm.time()
    tVals = ay.array('f',[t0]) #time values.
    yVals = ay.array('f',[y0]) #y-values. i.e. the solution.
    for i in range(0,int(N-1)): #for each index.
        tVals.append(t0 + h)
        yVals.append(y0 + h*f(t0,y0))
        t0 = t0 + h
        y0 = y0 + h*f(t0,y0)
    plt.plot(tVals,yVals,'r-')
    #plt.axis([])
    plt.show()
    toc = tm.time()
    print('time elapsed for Euler:',toc-tic)

# RK4 for first-order ODEs.
def RK4(t0,y0,h):
    tic = tm.time()
    tVals = ay.array('f',[t0]) #time values.
    yVals = ay.array('f',[y0]) #y-values. i.e. the solution.
    for i in range(0,int(N)): #for each index.
        tVals.append(t0 + h)
        Kn1 = f(t0,y0)
        Kn2 = f(t0 + 0.5*h,y0 + 0.5*h*Kn1)
        Kn3 = f(t0 + 0.5*h,y0 + 0.5*h*Kn2)
        Kn4 = f(t0 + h,y0 + h*Kn3)
        yVals.append(y0 + (h/6)*(Kn1 + 2*Kn2 + 2*Kn3 + Kn4))
        t0 = t0 + h
        y0 = y0 + (h/6)*(Kn1 + 2*Kn2 + 2*Kn3 + Kn4)
    plt.plot(tVals,yVals,'b-')
    #plt.axis([])
    plt.show()
    toc = tm.time()
    print('time elapsed for RK4:',toc-tic)

Euler(t0,y0,h)
RK4(t0,y0,h)    