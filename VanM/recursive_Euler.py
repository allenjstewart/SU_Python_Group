from __future__ import division
import numpy as np

def numSteps(time0,timef,dtime):
    num=(timef-time0)/dtime+1
    num=int(num)
    return num

def Euler(f,x0,t0,tf,dt):
    n=numSteps(t0,tf,dt)
    newX=x0
    for i in range(n):
        newX=[j+dt*k(t0+dt*i,newX) for j,k in zip(newX,f)]
    return newX

print(Euler([lambda t,x:t*x[0]],[1],0,2,.00001))