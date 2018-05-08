# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:42:20 2018

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
#import scipy.integrate as solve_ivp

##########################################################
def f(t,x,y):
    return (1/2)*(6-13*t) #x'=f(t,x,y).
def g(t,x,y):
    return (1/2)*(6+13*t) #y'=g(t,x,y).
t0 = 0 #initial time.
x0 = 2 #initial condition for x-equation.
y0 = 5 #initial condition for y-equation.
tf = 5 #final time.
N = 10000 #number of steps.
h = (tf-t0)/N #step size.
##########################################################

# Euler's method for first-order ODEs.
def Euler(t0,x0,y0,h):
    tic = tm.time()
    tVals = ay.array('f',[t0]) #time values.
    xVals = ay.array('f',[x0]) #x-values. i.e. the solution.
    yVals = ay.array('f',[y0]) #y-values. i.e. the solution.
    for i in range(0,int(N)): #for each index.
        tVals.append(t0 + h)
        xVals.append(x0 + h*f(t0,x0,y0))
        yVals.append(y0 + h*g(t0,x0,y0))
        t0 = t0 + h
        x0 = x0 + h*f(t0,x0,y0)
        y0 = y0 + h*g(t0,x0,y0)
    plt.plot(tVals,xVals,'r-',label='x-solution')
    plt.plot(tVals,yVals,'b-',label='y-solution')
    plt.legend()
    plt.title('Plotting Euler approximation for system')
    plt.xlabel('t')
    plt.ylabel('x and y')
    #plt.axis([])
    plt.show()
    toc = tm.time()
    print('time elapsed for Euler:',toc-tic)

# RK4 for first-order ODEs.
def RK4(t0,x0,y0,h):
    tic = tm.time()
    tVals = ay.array('f',[t0]) #time values.
    xVals = ay.array('f',[x0]) #x-values. i.e. the solution.
    yVals = ay.array('f',[y0]) #y-values. i.e. the solution.
    for i in range(0,int(N)): #for each index.
        tVals.append(t0 + h)
        Kn1x = f(t0,x0,y0)
        Kn2x = f(t0 + 0.5*h,x0 + 0.5*h*Kn1x,y0)
        Kn3x = f(t0 + 0.5*h,x0 + 0.5*h*Kn2x,y0)
        Kn4x = f(t0 + h,x0 + h*Kn3x,y0)
        xVals.append(x0 + (h/6)*(Kn1x + 2*Kn2x + 2*Kn3x + Kn4x))
        Kn1y = g(t0,x0,y0)
        Kn2y = g(t0 + 0.5*h,x0,y0 + 0.5*h*Kn1y)
        Kn3y = g(t0 + 0.5*h,x0,y0 + 0.5*h*Kn2y)
        Kn4y = g(t0 + h,x0,y0 + h*Kn3y)
        yVals.append(y0 + (h/6)*(Kn1y + 2*Kn2y + 2*Kn3y + Kn4y))
        t0 = t0 + h
        x0 = x0 + (h/6)*(Kn1x + 2*Kn2x + 2*Kn3x + Kn4x)
        y0 = y0 + (h/6)*(Kn1y + 2*Kn2y + 2*Kn3y + Kn4y)
    plt.plot(tVals,xVals,'r-',label='x-solution')
    plt.plot(tVals,yVals,'b-',label='y-solution')
    plt.legend()
    plt.title('Plotting RK4 approximation for system')
    plt.xlabel('t')
    plt.ylabel('x and y')
    #plt.axis([])
    plt.show()
    toc = tm.time()
    print('time elapsed for RK4:',toc-tic)

Euler(t0,x0,y0,h)
RK4(t0,x0,y0,h)    
#solve_ivp([lambda t,y: t-y],[0,10],[4])