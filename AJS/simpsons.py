# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:06:10 2018

@author: allen
"""

import numpy as np
import math as math
import random as rand
import time

def simpson(f,a, b, e):
    time_start=time.clock()
    prevApprox=(b-a)*f((b-a)*rand.random()+a)
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
    while (abs(Approx-prevApprox)>error):
        if (time.clock()-time_start>10) and (abs(Approx-prevApprox)>.1):
          return print("Integral does not exist")
        prevApprox=Approx
        n=2*n 
        Approx=0		           
        for i in range(0,len(in_part)-1):
            sub_sum=0
            h = (in_part[i+1]-in_part[i])/float(n)
            sub_sum=f(in_part[i])+f(in_part[i+1])
            for j in range(1,n,2):
               sub_sum+= 4*f(in_part[i]+j*h)
            for j in range(2,n,2):
               sub_sum+= 2*f(in_part[i]+j*h)
            Approx+=sub_sum*h/3  
        count=count+1        
        print(Approx, count, time.clock()-time_start)        
    return Approx, time.clock()-time_start

simpson(lambda x:x**(-2),-1,1,.0001)