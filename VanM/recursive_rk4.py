from __future__ import division
from scipy.integrate import solve_ivp

def rk4system(f,x0,t0,tf,dt):
    n=int((tf-t0)/dt)+1
    newX=x0
    for i in range(n):
        k1=[dt*j(t0+dt*i,newX) for j in f]
        k2=[dt*j(t0+dt*i+dt/2,[a+b/2 for a,b in zip(newX,k1)]) for j in f]
        k3=[dt*j(t0+dt*i+dt/2,[a+b/2 for a,b in zip(newX,k2)]) for j in f]
        k4=[dt*j(t0+dt*i+dt,[a+b for a,b in zip(newX,k1)])for j in f]
        newX=[a+(1/6)*(b+2*c+2*d+e) for a,b,c,d,e in zip(newX,k1,k2,k3,k4)]
    return newX

print(rk4system([lambda t,x:t*x[0]],[1.0],0.0,2.0,.000001))
print(solve_ivp(lambda t,x:t*x[0],[0.0,2.0],[1.0]))

