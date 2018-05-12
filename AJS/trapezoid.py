# Author: AJ Stewart
# This code uses random processes and the trapezoid method
# To approximate a definite integral
# This code does not require a specified number of sub intervals
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
# Working on a plane
# No time to write a haiku
# Well, I guess I lied
#####################################

import numpy as np #Arrays!
import math as math #Functions!
import random as rand #And Distributions! Oh, My!
import time #

def trapezoid(f,a, b, e):

###################
#Initialize Variables
###################

    time_start=time.clock() #Start the computation clock
#Two initial approximations
    prevApprox=[(b-a)*f((b-a)*rand.random()+a)]
    Approx=(b-a)*f((b-a)*rand.random()+a)
    n=math.floor(-1*math.log10(e)) #The intial amount of subintervals
    error=0.5*e
#Check the endpoints.
#If the function isn't defined shift the endpoints
    try:
        f(a)
    except ValueError:
        a=a+e/100 #I chose 100 arbitrarily
    try:
        f(b)
    except ValueError:
        b=b-e/100

#######################
#Create the initial partition
#######################
#Start at the left endpoint
#The loop creates an initial distribution with at approximately n subintervals
#n depends on the error value given by the use
#Random values are choosen by a Weibull distribution
#The Weibull distribution guarantees that there is a 99% chance
#That the next value in the partition is between .6(b-a)/n and 1.2(b-a)/n
#Of the previous value
#The loop will run until the last value appended is greater than b
###############################################################################

    in_part=[a]
    while (in_part[len(in_part)-1]<b):
        in_part.append((b-a)*rand.weibullvariate(1,10)/n+in_part[len(in_part)-1])
        if in_part[len(in_part)-1]>=b:
            in_part[len(in_part)-1]=b
######################
#The bulk of the approximation
######################
#Now that the intial parition of a and b has been created
#We run the trapezoid method on each of the subintervals in in_part
#The code will run until
#(a) it has been 10 seconds and the approximations are not within .1
#(b) the approximation and the average of the previous two approximations
#    is within the error tolerance
#I take the average of two previous approximations in order to reduce noise
###############################################################################

    while (abs(Approx-np.average(prevApprox))>error):
#Stop if the intergral is not converging
        if (time.clock()-time_start>10) and (abs(Approx-prevApprox[len(prevApprox)-1])>.1):
          return print("The integral does not exist")
#Create a new partition
        part=[a] #Start at the left endpoint
        for i in range(0,len(in_part)-1):
#If the length of the pervious subinterval is
#Greater than the error
#Divide the subinterval by picking a random point
#In the subinterval
#Otherwise leave the subinterval alone
            if abs(in_part[i+1]-in_part[i])>error:
             part.append((in_part[i+1]-in_part[i])*rand.random()+in_part[i])
            part.append(in_part[i+1])
#Append the previous approximation to
#An array of approximations
        prevApprox.append(Approx)
#Reduce the array of previous approximations 
#To length two
        if(len(prevApprox)>2):
               prevApprox=prevApprox[len(prevApprox)-2:]
        Approx=0
#The Trapezoid method
        for i in range(0,len(part)-1):
            h = part[i+1]-part[i]
            Approx += 0.5*(f(part[i+1])+f(part[i]))*h
        in_part = part
    return Approx, time.clock()-time_start
