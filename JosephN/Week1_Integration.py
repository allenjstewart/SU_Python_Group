# AUTHOR: J. Nakao
# DATE: 17 April 2018
# PURPOSE: Integration techniques for trapezoid rule,
# Simpson's rule, and Monte Carlo. Will investigate
# various functions.
# INSTRUCTIONS:
# 1. Declare function to integrate as f(x).
# 2. Declare bounds of integration, A and B.
# COMMENTS: N/A.
# 
# 
import numpy as np
import random as rn
import time as tm

###################################
# Declare function to integrate and lower/upper bounds.
def f(x):
    #return x**3
    #return np.cos(np.exp(x))
    #return np.log(x)
    #return np.sin(1/x)
    return np.cos(1/x)
A = -1
B = 1
###################################

# Trapezoid rule approximation, integrating from a to b.
def trapz(a,b):
    trapz_t0 = tm.time()
    x = np.linspace(a,b,int(np.ceil((b-a)/0.001)))
    trap_approx = 0
    for i in range(0,int(np.ceil((b-a)/0.001)-1)):
        dx = x[i+1] - x[i]
        trap_approx += dx*((f(x[i])+f(x[i+1]))/2)
    trapz_t0 = tm.time() - trapz_t0
    print("Trapezoid rule approximation: ",trap_approx)
    print("time to run trapz: ",trapz_t0)

# Simpson's rule approximation, integrating from a to b.
def simpson(a,b):
    simps_t0 = tm.time()
    x = np.linspace(a,b,int(np.ceil((b-a)/0.001)+1))
    #+1 to ensure even number of subdivisions (necessary for Simpson's rule.
    #i.e. (b-a)/n, where n is even)
    
    if int(np.ceil((b-a)/0.001)+1) % 2 == 0: #if even number (i.e. n is odd).
        print("CAUTION!!! n is even. make odd for Simpson's rule.")
    
    simpson_approx = 0
    for i in range(0,int(np.ceil((b-a)/0.001)+1)):
        if i<int(np.ceil((b-1)/0.001)):
            dx = x[i+1]-x[i]
            if i==0:
                simpson_approx += (dx/3)*f(x[i])
            elif i % 2 == 1: #if i is odd.
                simpson_approx += 4*(dx/3)*f(x[i])
            elif i % 2 == 0 and i!=0: #if i is even.
                simpson_approx += 2*(dx/3)*f(x[i])
        elif i==int(np.ceil((b-1)/0.001)):
            dx = (b-a)/int(np.ceil((b-1)/0.001)+1)
            simpson_approx += (dx/3)*f(x[i])
    simps_t0 = tm.time() - simps_t0
    print("Simpson's rule approximation: ",simpson_approx)
    print("time to run simps: ",simps_t0)

# Monte Carlo approximation, integrating from a to b.
def mc(a,b):
    mc_t0 = tm.time()
    n = 100000 #number of selected node points.
    mc_approx = 0 #temporary monte carlo approximation.
    for i in range(0,n):
        x_i = rn.uniform(a,b) #random number between a and b.
        mc_approx += ((b-a)/n)*f(x_i)
    mc_t0 = tm.time() - mc_t0
    print("Monte Carlo approximation: ",mc_approx)
    print("time to run mc: ",mc_t0)
    
# All approximations (results).
trapz(A,B)
simpson(A,B)
mc(A,B)
