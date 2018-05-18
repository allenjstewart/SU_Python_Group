
import math as math
import random as random
import time as time
import scipy.integrate as integrate

def f1(x):
    return x**3
def f2(x):
    return math.cos(math.exp(x))
def f3(x):
    return math.log(x)
def f4(x):
    return math.sin(1/x)
def f5(x):
    return math.cos(1/x)

def Trapezoidal(f,a,b,n):
    t0=time.time()
    h=(b-a)/n
    sum=0.0
    for i in range(1, n):
        sum+=h*f(a+i*h)
    sum+=0.5*h*(f(a)+f(b))
    print("    The trapezoid rule gives:  %16.16f and required %1.4f seconds" % (sum,time.time()-t0))
    return sum

def Simpsons(f,a,b,n):
    t0=time.time()
    h=(b-a)/n
    sum=0.0
    for i in range(1, int(n/2)):
        sum+=2.0*f(a+2.0*i*h)
    for i in range(1, int(n/2+1)):
        sum+=4.0*f(a+(2.0*i-1.0)*h)
    sum+=f(a)+f(b)
    sum=h/3.0*sum
    print("    Simpsons rule gives:       %16.16f and required %1.4f seconds" % (sum,time.time()-t0))
    return sum

def MonteCarlo(f,a,b,n):
    t0=time.time()
    sum=0.0
    for _ in range(1,n):
        sum+=(b-a)*f(random.uniform(a,b))
    sum=sum/n
    print("    Monte Carlo gives:         %16.16f and required %1.4f seconds" % (sum,time.time()-t0))
    return sum

def MyIntegrationRoutine(Myf,lower,upper,NNN):
    t0=time.time()
    quad1,_=integrate.quad(Myf,lower,upper)
    print("    Quad gives:                %16.16f and required %1.4f seconds" % (quad1,time.time()-t0))
    t0=time.time()
    romb=integrate.romberg(Myf,lower,upper)
    print("    Romberg gives:             %16.16f and required %1.4f seconds" % (romb,time.time()-t0))
    
    Trapezoidal(Myf,lower,upper,NNN)
    Simpsons(Myf,lower,upper,NNN)
    MonteCarlo(Myf,lower,upper,NNN)

print(' ')
print('FOR THE FIRST INTEGRAL')
MyIntegrationRoutine(f1,-3.0,3.0,10000)
print(' ')
print('FOR THE SECOND INTEGRAL')
MyIntegrationRoutine(f2,0.0,2.0,10000)
print(' ')
print('FOR THE THIRD INTEGRAL')
MyIntegrationRoutine(f3,0.01,1.0,10000)
print(' ')
MyIntegrationRoutine(lambda x:x**2,-1,1,10000)
print('FOR THE FOURTH INTEGRAL')
MyIntegrationRoutine(f4,-1.0,-0.5,10000)
print(' ')
print('FOR THE FIFTH INTEGRAL')
MyIntegrationRoutine(f5,-0.99,-0.9,10000)
print(' ')
