# Author: AJ Stewart
# This code uses random processes and the midpoint method
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
# Why'd I write this code
# Cuz it was pretty simple
# But I won't use it
#####################################

#Important imports of import portion
import numpy as np
import math as math
import random as rand
import time

def midpoint(f,a, b, e):
###################
#Initialize Variables
###################
    time_start=time.clock() #Is this code fast and efficient? Survey says, no.

#Got to start somewhere
#Initial approximations
    prevApprox=[(b-a)*f((b-a)*rand.random()+a)]
    Approx=(b-a)*f((b-a)*rand.random()+a)
    n=math.floor(-1*math.log10(e)) #Intial number of subintervals
    error=0.5*e
    count=0
#Woah buddy. Are you trying to evaluate at undefined points?
    try:
        f(a)
    except ValueError:
        a=a+e/100
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

#I should probably just create a function called in_part
###############################################################################
    in_part=[a]
    while (in_part[len(in_part)-1]<b):
        in_part.append((b-a)*rand.weibullvariate(1,10)/n+in_part[len(in_part)-1])
        if in_part[len(in_part)-1]>=b:
            in_part[len(in_part)-1]=b
    while (abs(Approx-np.average(prevApprox))>error):
#Stop if the intergral is not converging
        if (time.clock()-time_start>10) and (abs(Approx-prevApprox[len(prevApprox)-1])>.1):
          return print("The integral does not exist")
#Create a new partition
        part=[a] #Start at the left endpont
        for i in range(0,len(in_part)-1):
#If the length of the previous subinterval is
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
#The midpoint method
        for i in range(0,len(part)-1):
            h = part[i+1]-part[i]
            Approx += f(0.5*(part[i+1]+part[i]))*h
        in_part = part
    return Approx, time.clock()-time_start
