# This file will contain code to numerically evaluate integrals using the following methods:
#   Trapezoid Rule
#   Simpson's Rule
#   MonteCarlo Method
#
# Example code for Trapezoid found at:
# http://hplgit.github.io/edu/py_vs_m/._numerical_programming_guide001.html
#
######################################################
#   https://user.xmission.com/~emailbox/ascii_cats.htm
#
#                )\._.,--....,'``.       
#  .b--.        /;   _.. \   _\  (`._ ,.
# `=,-,-'~~~   `----(,_..'--(,_..'`-.;.'
#
######################################################
# libraries needed for MonteCarlo:

import math
import random
#import numpy as np

# Code for the Trapezoid Rule for function f(x) on the interval a<x<b with n subdivisions
def Trapezoidal(f, a, b, n):
    #function = f('x')
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))
    for i in range(1,n,1):
        s = s + f(a + i*h)
    s = h*s
    print("Trapezoidal Rule Approximation for the interval %d < x < %d with %d subdivisions: \n %f" % (a, b, n, s))
    return s

# Code for Simpson's Rule for function f(x) on the interval a<x<b with n subdivisions
def Simpson(f, a, b, n):
    s = 0
    if n % 2 == 1:
        raise ValueError("n must be even (received n=%d) \n " % n)

    h = (b-a)/float(n)
    s += f(a) # evaluate at x=a
    #print("First Approx: ",s)
    for i in range(1,n,2): # it was tricky to get the indexing right here...the range seems to stop at n-1 when you input n??
        s += 4*f(a + i*h) + 2*f(a + (i+1)*h)
    s = s - f(b)    #the last step in the loop added 2*f(b), but we only need one.
    s = s*h/3
    print("Simpson's Rule Approximation for the interval %d < x < %d with %d subdivisions: \n %f" % (a, b, n, s))
    return s

# Code for the MonteCarlo Method for function f(x) on the interval a<x<b with n subdivisions
def MonteCarlo(f, a, b, num_steps):
    #h = (b-a)/float(n)
    mc_approx = 0
    random.seed() # seeds the random number generator with the clock time
    for i in range(1,num_steps,1):
        mc_approx+= f(random.uniform(a,b)) # evaluate at a random point within the domain
    mc_approx = (b-a)*mc_approx/num_steps
    print("MonteCarlo Approximation for the interval %d < x < %d with %d iteratons: \n %f" % (a, b, num_steps, mc_approx))
    return mc_approx


# Define the functions that we are going to use:
# def func(x):
#     return np.power(x,3)

print("\n\n Several approximations of the integral of f(x) = x^3" + "\n\n")
Trapezoidal(lambda x: x**3,-5,5,100)
Simpson(lambda x: x**3,-5,5,100)
MonteCarlo(lambda x: x**3,-5,5,10000)
print("\n\n Complete - yay! \n\n\n")

print("\n\n Several approximations of the integral of f(x) = cos(e^x)" + "\n\n")
Trapezoidal(lambda x: math.cos(math.exp(x)),0,10,100)
Simpson(lambda x: math.cos(math.exp(x)),0,10,100)
MonteCarlo(lambda x: math.cos(math.exp(x)),0,10,1000)
print("\n\n Complete - yay! \n\n\n")

print("\n\n Several approximations of the integral of f(x) = ln(x).\n Note that since f(x) is not defined when x=0, we have to be careful about how we proceed.\n\n")
Trapezoidal(lambda x: math.log(x),0.0000001,1,100)
Simpson(lambda x: math.log(x),0.0000001,1,100)
MonteCarlo(lambda x: math.log(x),0,1,1000)
print("\n\n Complete - yay! \n\n\n")

print("\n\n Several approximations of the integral of f(x) = sin(1/x).\n Note that since f(x) is not defined when x=0,we have to be careful about how we proceed.  I haven't figured out how to make Simpson's Rule work yet. :-()\n\n")
Trapezoidal(lambda x: math.sin(1/x),-1,1,101)
#Simpson(lambda x: math.sin(1/x),-1.000003,1.000003,100)
MonteCarlo(lambda x: math.sin(1/x),-1,1,1000)
print("\n\n Complete - yay! \n\n\n")

print("\n\n Several approximations of the integral of f(x) = cos(1/x).\n Note that since f(x) is not defined when x=0,we have to be careful about how we proceed.  I haven't figured out how to make Simpson's Rule work yet. :-(\n\n")
Trapezoidal(lambda x: math.cos(1/x),-1,1,101)
#Simpson(lambda x: math.cos(1/x),-1.000003,1.000003,100)
MonteCarlo(lambda x: math.cos(1/x),-1,1,1000)
print("\n\n Complete - yay! \n\n\n")
