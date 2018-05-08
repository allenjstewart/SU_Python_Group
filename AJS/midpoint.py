# -*- coding: utf-8 -*-
"""
Created on Sat May  5 13:25:09 2018

@author: allen
"""

import numpy as np
import math as math
import random as rand
import time

def midpoint(f,a, b, e):
    time_start=time.clock()
    prevApprox=[(b-a)*f((b-a)*rand.random()+a)]
    Approx=(b-a)*f((b-a)*rand.random()+a)
    n=math.floor(-1*math.log10(e))
    error=0.5*e
    count=0
    try:
        f(a)
    except ValueError:
        a=a+e/100
    try:
        f(b)
    except ValueError:
        b=b-e/100
    in_part=[a] 
    while (in_part[len(in_part)-1]<b):
        in_part.append((b-a)*rand.weibullvariate(1,10)/n+in_part[len(in_part)-1])
        if in_part[len(in_part)-1]>=b:
            in_part[len(in_part)-1]=b          
    while (abs(Approx-np.average(prevApprox))>error):
        #if((time.clock()-time_start)>20):
         #  return Approx, count, time.clock()-time_start
        part=[a] 
        #print(part, in_part)               
        for i in range(0,len(in_part)-1): 
            if abs(in_part[i+1]-in_part[i])>error:
             part.append((in_part[i+1]-in_part[i])*rand.random()+in_part[i])
            part.append(in_part[i+1])    
        count=count+1 
        prevApprox.append(Approx)
        if(len(prevApprox)>2):
               prevApprox=prevApprox[len(prevApprox)-2:]
        Approx=0
        for i in range(0,len(part)-1):
            h = part[i+1]-part[i]
            Approx += f(0.5*(part[i+1]+part[i]))*h      
        in_part = part     
    return Approx, time.clock()-time_start

