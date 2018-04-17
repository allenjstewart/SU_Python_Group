
import random as random

def montecarlo(f,a,b,n):
    h=(b-a)/n
    s=0.0
    
    for i in range(1,n):
        s+=f(random.uniform(a,b))
    
    return h*s

print(montecarlo(lambda x:x**2, 5.0, 10.0, 10000))