from __future__ import division
import numpy as np


#big important note: f is designed to accept two inputs and the 
#first one BETTER be time or else this will work VERY poorly
def eulersys(f,f0,t0,tf,stepsize):
    #assume stepsize evenly divides (tf-t0)
    numSteps=(tf-t0)/stepsize+1
    numSteps=int(numSteps)
    #define time array:
    timeArray=[]
    for i in range(numSteps):
        timeArray.append(t0+i*stepsize)
    #build solution array
    solArray=[]
    for i in range(len(f)):
        solArray.append(np.zeros(numSteps))
    #input initial conditions
    for i in range(len(f)):
        solArray[i][0]=f0[1]
    #We now implement the method. 
    #I have chosen to iterate by time
    #step and then element in function
    #array, but one could equivalently
    #iterate in the alternative order
    for i in range(1,numSteps):
        for j in range(len(f)):
            addition= stepsize*f[j](timeArray[i-1],solArray[j][i-1])
            solArray[j][i]=solArray[j][i-1]+addition
    
    for i in range(len(f)):
        print(solArray[i][numSteps-1])
    
eulersys([lambda t,x:t*x],[1,1],1.0,2.0,0.25)