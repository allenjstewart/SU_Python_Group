
import math as math
import numpy as np
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
from scipy import special
np.set_printoptions(precision=16)


def KdVRK4(kvec,t0,x0,tf,n):
    tvec=np.zeros(n+1)
    xvec=np.zeros((n+1,len(x0)))
    tvec[0]=t0
    xvec[0]=x0
    h=(tf-t0)/n
    for j in range(0,n):
        k1=h*KdVRHS(xvec[j],kvec)
        k2=h*KdVRHS(xvec[j]+0.5*k1,kvec)
        k3=h*KdVRHS(xvec[j]+0.5*k2,kvec)
        k4=h*KdVRHS(xvec[j]+k3,kvec)
        xvec[j+1]=xvec[j]+(k1+2.0*k2+2.0*k3+k4)/6.0
        tvec[j+1]=tvec[j]+h
    return tvec,xvec

def KdVRHS(u,kvec):
    uhat=np.fft.fft(u)
    ux=np.fft.ifft(kvec*uhat)
    uxxx=np.fft.ifft(kvec**3*uhat)
    return np.real(-2.0*u*ux-uxxx)

def KdVcnSoln(x,t,kappa,k):
    _,cn,_,_=special.ellipj(kappa*(x-4.0*kappa**2*(2.0*k**2-1.0)*t),k**2)
    return 6.0*kappa**2*k**2*cn**2

N=32
kappa=1.0/3.0
k=0.8
tf=20.0
L=2.0*special.ellipk(k**2)/kappa
x=np.linspace(0,L-L/N,N)
kvec=1j*np.zeros(N)
kvec[0:int(N/2)]=2.0*math.pi/L*1j*np.arange(0,int(N/2),1)
kvec[int(N/2)+1:N]=2.0*math.pi/L*1j*np.arange(-int(N/2)+1,0,1)
u0=KdVcnSoln(x,0,kappa,k)
uf=KdVcnSoln(x,tf,kappa,k)

NNN=20000
asd,dsa=KdVRK4(kvec,0.0,u0,tf,NNN)

print("The L1 error is:",sum(abs(dsa[NNN]-uf)))

f=plt.figure(1)
plt.subplot(211)
plt.plot(u0,label="Initial Condition")
plt.plot(uf,label="Solution at t_f")
plt.xlabel("x")
plt.ylabel("u")

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.subplot(212)
plt.plot(dsa[NNN]-uf)
plt.xlabel("x")
plt.ylabel("uf-exact")
plt.show()


