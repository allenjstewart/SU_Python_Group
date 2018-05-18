
import math as math
import random as random
import time as time
import scipy.integrate as integrate
import numpy as numpy
import inspect as inspect

def f1(x):
    return x**3-2.0

def df1(x):
    return 3*x**2

def F1(x):
    return numpy.array([x[0]**2.0+x[1]**2.0-4.0,x[0]**2-x[1]**2+2.0])

def DF1(x):
    return numpy.array([[2.0*x[0],2.0*x[1]],[2.0*x[0],-2.0*x[1]]])

def F2(x):
    return numpy.array([x[0]**3.0+x[1]**3.0-4.0,x[0]**2-x[1]**2+2.0])

def DF2(x):
    return numpy.array([[3.0*x[0]**2,3.0*x[1]**2],[2.0*x[0],-2.0*x[1]]])

def NewtonsMethod(fxn,dfxn,x0,n):
    for _ in range(1,n+1):
        x0=x0-fxn(x0)/dfxn(x0)
    return x0

def VecNewtonsMethod(Fxn,DFxn,x0,n):
    for _ in range(1,n+1):
        x0=x0-numpy.linalg.inv(DFxn(x0)).dot(Fxn(x0))
#        print(x0)
#        print(((1.0-x0[0])**2.0+(1.73205080757-x0[1])**2.0)**0.5)
#        print(((0.639396468498-x0[0])**2.0+(1.55203989766-x0[1])**2.0)**0.5)
    return x0

result1=NewtonsMethod(f1,df1,1.0,5)
print('')
print('My Newton solver works for predefined scalar problems!   2**(1/3)=',result1,'according to five steps of Newton with x0=1')
print('In comparison, the exact decimal value is                2**(1/3)=',2.0**(1.0/3.0))
result2=NewtonsMethod(lambda x: x**5.0-5.0,lambda x: 5.0*x**4.0,1.0,5)
print('')
print('It also works if I input scalar problems using lambda x notation!   5**(1/5)=',result2,'according to five steps of Newton with x0=1')
print('In comparison, the exact decimal value is                           5**(1/5)=',5.0**(1.0/5.0))
print('')
result3=VecNewtonsMethod(F1,DF1,numpy.array([2,3]),5)
print('My vector Newton solver works for predefined vector functions!  Exact solution is     x0= 1.0000000000000000')
print('                                                                Exact solution is     x1= 1.7320508075688773')
print('Using five steps and an inital guess of [2,3] gives                                   x0=',result3[0])
print('                                                                                      x1=',result3[1])
print('')
print('For a second vector problem:')
result4=VecNewtonsMethod(F2,DF2,numpy.array([1,2]),5)
print('My solution:         x0=%16.16f and x1=%16.16f' % (result4[0],result4[1]))
print('Exact solution:      x0=0.6393964684978625 and x1=1.552039897659702')
print('')
result5=VecNewtonsMethod(lambda x: numpy.array([x[0]**3.0+x[1]**3.0-4.0,x[0]**2-x[1]**2+2.0]),lambda x: numpy.array([[3.0*x[0]**2,3.0*x[1]**2],[2.0*x[0],-2.0*x[1]]]),numpy.array([2,3]),5)
print('It also works using lambda x notation!!!')
print('My solution:         x0=%16.16f and x1=%16.16f' % (result5[0],result5[1]))
print('Exact solution:      x0=0.6393964684978625 and x1=1.552039897659702')
print('')
print('I can also get it to solve systems of linear equations')
a=numpy.array([[470,344,12],[221,12,17],[0.2,0.3,0.7]])
b=numpy.array([5,9,13])
x=numpy.linalg.solve(a,b)
numpy.set_printoptions(precision=16)
print(x)
