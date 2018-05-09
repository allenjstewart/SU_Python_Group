# Author: AJ Stewart
# This code uses random processes to create partitions and then
# Simpson's method to approximate a definite integral
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
# Oh my god, comments
# You should know what I'm thinking
# This code's wild ride
#####################################
import numpy as np #Arrays, blah blah blah
import math as math #math functions, blah blah
import random as rand #I need this to create the initial partition of (a,b)
import time #For computational testing

def simpson(f,a, b, e):
###################
#Initialize Variables
###################
    time_start=time.clock() #Start the clock
#Create two initial approximations
    prevApprox=(b-a)*f((b-a)*rand.random()+a)
    Approx=(b-a)*f((b-a)*rand.random()+a)
#Create an initial number of subintervals
    n=math.floor(-1*math.log10(e))
    error=0.5*e
    count=0
#Is the function defined at the end points?
#If not, redefine the endpoints.
    try:
        f(a)
    except ValueError:
        a=a+error/float(n)
    try:
        f(b)
    except ValueError:
        b=b-error/float(n)
    in_part=[a] #Initialize the partition.

#######################
#Create the initial partition
#######################
#The next loop creates an initial distribution with at approximately n subintervals
#n depends on the error value given by the use
#Random values are choosen by a Weibull distribution
#The Weibull distribution guarantees that there is a 99% chance
#That the next value in the partition is between .6(b-a)/n and 1.2(b-a)/n
#Of the previous value
#The loop will run until the last value appended is greater than b
###############################################################################

    while (in_part[len(in_part)-1]<b):
        in_part.append((b-a)*rand.weibullvariate(1,10)/n+in_part[len(in_part)-1])
        if in_part[len(in_part)-1]>=b:
            in_part[len(in_part)-1]=b

######################
#The bulk of the approximation
######################
#Now that the intial parition of a and b has been created
#We run Simpson's method on each of the subintervals in in_part
#The code will run until
#(a) two succesive approximations are within error given or
#(b) it has been 10 seconds and the approximations are not within .1
###############################################################################

    while (abs(Approx-prevApprox)>error):
        if (time.clock()-time_start>10) and (abs(Approx-prevApprox)>.1): #I chose .1 based on tests of the code
          return print("Integral does not exist") #Not within .1 in 10 seconds, bounce
        prevApprox=Approx
        n=2*n
        Approx=0
#We'll now run Simpson's method on each subinterval	with 2n subintervals each
#This means that there will be a total of 2n^2 subintervals of (a,b)
#In our first value of Approx
        for i in range(0,len(in_part)-1):
            sub_sum=0 #sub_sum will be the Simpson's approximation on a subinterval
            h = (in_part[i+1]-in_part[i])/float(n)
            sub_sum=f(in_part[i])+f(in_part[i+1])
#Simpson's method on the interval defined by in_part[i] to in_part[i+1]
            for j in range(1,n,2):
               sub_sum+= 4*f(in_part[i]+j*h)
            for j in range(2,n,2):
               sub_sum+= 2*f(in_part[i]+j*h)
            Approx+=sub_sum*h/3
    return Approx
