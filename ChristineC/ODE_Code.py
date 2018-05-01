#########################################################
# Code for solving IVPs using:
#       - Euler's Method
#       - RK4
#########################################################
# Resources:
#
# Paul's Online Math Notes:
#       http://tutorial.math.lamar.edu/Classes/DE/EulersMethod.aspx
# RK4:
#       https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods
# Array Storage with NumPy:
#       https://docs.scipy.org/doc/numpy/user/quickstart.html
# Plotting:
#       http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
# SciPy Sove IVP:
#       https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp
#
#############################################################################
# http://wiki.c2.com/?AsciiKitten
#
#   |\      _,,,---,,_
#   /,`.-'`'    -.  ;-;;,_
#  |,4-  ) )-,_..;\ (  `'-'
# '---''(_/--'  `-'\_)
#
#############################################################################
# libraries needed:

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def Euler(f,t0,y0,step,num_steps):
    # Use Euler's Method to solve dy/dt = f(t,y) given y(t0) = y0
    # with stepsize step and number of steps: num_steps
    # Store the output in the array sol.
    # The first column stores t-values, and the second column stores y-values.
    sol = np.zeros((num_steps,2))
    sol[0,0] = t0
    sol[0,1] = y0
    for i in range(1,num_steps,1):
        # print("Array Storage Method: When t = %f, y = %f" % (sol[i-1,0], sol[i-1,1]))
        m = f(sol[i-1,0], sol[i-1,1]) # evaluate f at the previous time
        # step forward in time according to Euler's Method:
        sol[i,0] = sol[i-1,0] + step
        sol[i,1] = sol[i-1,1] + m*step
    # print("Array Storage Method: When t = %f, y = %f" % (sol[num_steps-1,0], sol[num_steps-1,1]))
    print("Euler Complete - yay!\n\n")
    return sol


def RK4(f,t0,y0,step,num_steps):
    # Use RK4 to solve dy/dt = f(t,y) given y(t0) = y0
    # with stepsize step and number of steps: num_steps
    k1 = k2 = k3 = k4 = 0
    # Store the output in the array sol.
    # The first column stores t-values, and the second column stores y-values.
    sol = np.zeros((num_steps,2))
    sol[0,0] = t0
    sol[0,1] = y0
    for i in range(1,num_steps,1):
        #print("Array Storage Method: When t = %f, y = %f" % (sol[i-1,0], sol[i-1,1]))
        k1 = step*f(sol[i-1,0], sol[i-1,1])
        k2 = step*f(sol[i-1,0] + step/2, sol[i-1,1] + k1/2)
        k3 = step*f(sol[i-1,0] + step/2, sol[i-1,1] + k2/2)
        k4 = step*f(sol[i-1,0] + step, sol[i-1,1] + k3)
        m = (k1 + 2*k2 + 2*k3 + k4)/6
        # step forward in time according to RK4:
        sol[i,0] = sol[i-1,0] + step
        sol[i,1] = sol[i-1,1] + m

    #print("Array Storage Method: When t = %f, y = %f" % (sol[num_steps-1,0], sol[num_steps-1,1]))
    print("RK4 Complete - yay!\n\n")
    return sol

######################################################
#
#   Code for 2x2 systems:
#
######################################################

def EulerSys(f,t0,y0,step,num_steps):
    # Use Euler's Method to solve dy/dt = f(t,y) given x(t0) = x0, y(t0) = y0
    # where y is a vector: y = [x, y], and y0 is a vector: y0 = [x0, y0]
    # with stepsize step and number of steps: num_steps
    # Store the output in the array sol.
    # The first column stores t-values, and the second column stores x-values,
    # the third column stores y-values
    sol = np.zeros((num_steps,3))
    sol[0,0] = t0
    sol[0,1] = y0[0]
    sol[0,2] = y0[1]
    for i in range(1,num_steps,1):
        # print("Array Storage Method: When t = %f, y = %f" % (sol[i-1,0], sol[i-1,1]))
        mx = f(sol[i-1,0], [sol[i-1,1], sol[i-1,2]])[0] # evaluate f at the previous time
        my = f(sol[i-1,0], [sol[i-1,1], sol[i-1,2]])[1] # evaluate f at the previous time
        # step forward in time according to Euler's Method:
        sol[i,0] = sol[i-1,0] + step
        sol[i,1] = sol[i-1,1] + mx*step
        sol[i,2] = sol[i-1,2] + my*step
    #print("Array Storage Method: When t = %f, x = %f, y = %f" % (sol[num_steps-1,0], sol[num_steps-1,1], sol[num_steps-1,2]))
    print("Euler (System) Complete - yay!\n\n")
    return sol


def RK4Sys(f,t0,y0,step,num_steps):
    # Use RK4 to solve dy/dt = f(t,y) given x(t0) = x0, y(t0) = y0
    # where y is a vector: y = [x, y], and y0 is a vector: y0 = [x0, y0]
    # with stepsize step and number of steps: num_steps
    k1 = k2 = k3 = k4 = 0
    l1 = l2 = l3 = l4 = 0
    # Store the output in the array sol.
    # The first column stores t-values, and the second column stores x-values,
    # the third column stores y-values
    sol = np.zeros((num_steps,3))
    sol[0,0] = t0
    sol[0,1] = y0[0]
    sol[0,2] = y0[1]
    for i in range(1,num_steps,1):
        #print("Array Storage Method: When t = %f, y = %f" % (sol[i-1,0], sol[i-1,1]))
        k1 = step*f(sol[i-1,0], [sol[i-1,1], sol[i-1,2]])[0]
        l1 = step*f(sol[i-1,0], [sol[i-1,1], sol[i-1,2]])[1]
        k2 = step*f(sol[i-1,0] + step/2, [sol[i-1,1] + k1/2, sol[i-1,2] + l1/2])[0]
        l2 = step*f(sol[i-1,0] + step/2, [sol[i-1,1] + k1/2, sol[i-1,2] + l1/2])[1]
        k3 = step*f(sol[i-1,0] + step/2, [sol[i-1,1] + k2/2, sol[i-1,2] + l2/2])[0]
        l3 = step*f(sol[i-1,0] + step/2, [sol[i-1,1] + k2/2, sol[i-1,2] + l2/2])[1]
        k4 = step*f(sol[i-1,0] + step, [sol[i-1,1] + k3, sol[i-1,2] + l3])[0]
        l4 = step*f(sol[i-1,0] + step, [sol[i-1,1] + k3, sol[i-1,2] + l3])[1]
        mx = (k1 + 2*k2 + 2*k3 + k4)/6
        my = (l1 + 2*l2 + 2*l3 + l4)/6
        # step forward in time according to RK4:
        sol[i,0] = sol[i-1,0] + step
        sol[i,1] = sol[i-1,1] + mx
        sol[i,2] = sol[i-1,2] + my

    print("Array Storage Method: When t = %f, y = %f" % (sol[num_steps-1,0], sol[num_steps-1,1]))
    print("RK4 Complete - yay!\n\n")
    return sol


######################################################
#
#   Initial Test Cases:
#
######################################################


# print("\n\nCheck our code using the IVP\n y' = 2 - 2y - exp(-4t), y(0)=1")
# print("The exact solution is given by:\n y = 1 + .5 exp(-4t) - .5 exp(-2t)")
# stepsize = .1
# total_steps = 100
# print("\nUse stepsize %f, and run for %d timesteps.\n" % (stepsize, total_steps))
# # The actual solution to this IVP is y = 1 + .5*exp(-4*t)- .5*exp(-2*t)
# exact_sol = np.zeros((total_steps,2))
# exact_sol[0,1]=1
# for i in range(1,total_steps,1):
#     exact_sol[i,0] = exact_sol[i-1,0]+stepsize
#     exact_sol[i,1] = 1 + .5*math.exp(-4*exact_sol[i,0]) - .5*math.exp(-2*exact_sol[i,0])
#
#
#
# print("Run the Euler's Method code:")
# euler_sol = Euler(lambda t,y: 2-2*y-math.exp(-4*t),0,1,stepsize,total_steps)
#
#
#
# print("Run the RK4 code:")
# rk4_sol = RK4(lambda t,y: 2-2*y-math.exp(-4*t),0,1,stepsize,total_steps)
#
# print("Generate another solution using scipy.integrate.solve_ivp:")
# from scipy.integrate import solve_ivp
# sol = solve_ivp(lambda t,y: 2-2*y-math.exp(-4*t),[0,10],[1])
# print("solve_ivp complete - yay!")
#
# plt.plot(exact_sol[:,0],exact_sol[:,1],'k-',label="Exact Solution")
# plt.plot(euler_sol[:,0],euler_sol[:,1],'r--',marker="*",label="Euler's Method")
# plt.plot(rk4_sol[:,0],rk4_sol[:,1],'b-.',marker="o",label="RK4 Method")
# plt.plot(sol.t[:],sol.y[0],'g.',marker="o", markersize=10,label="SciPy solve_ivp")
# plt.title("Numerical Solutions to the IVP y' = 2 - 2y - exp(-4t), y(0)=1")
# plt.xlabel("t")
# plt.ylabel("y")
# plt.legend()
# plt.show()
#
# print("\n\nNext, check our code using the IVP\n y' = y - .5 exp(t/2)sin(5t) + 5 exp(t/2)cos(5t), y(0)=0")
# print("The exact solution is given by:\n y = exp(t/2) sin(5t)")
# stepsize = .05
# total_steps = 200
# print("\nUse stepsize %f, and run for %d timesteps.\n" % (stepsize, total_steps))
# # The actual solution to this IVP is y = exp(t/2)*sin(5t)
# exact_sol2 = np.zeros((total_steps,2))
# exact_sol2[0,1]=1
# for i in range(1,total_steps,1):
#     exact_sol2[i,0] = exact_sol2[i-1,0]+stepsize
#     exact_sol2[i,1] = math.exp(exact_sol2[i,0]/2)*math.sin(5*exact_sol2[i,0])
#
#
#
# print("Run the Euler's Method code:")
# euler_sol2 = Euler(lambda t,y: y-.5*math.exp(t/2)*math.sin(5*t)+5*math.exp(t/2)*math.cos(5*t),0,0,stepsize,total_steps)
#
#
#
# print("Run the RK4 code:")
# rk4_sol2 = RK4(lambda t,y: y-.5*math.exp(t/2)*math.sin(5*t)+5*math.exp(t/2)*math.cos(5*t),0,0,stepsize,total_steps)
#
# print("Generate another solution using scipy.integrate.solve_ivp:")
# from scipy.integrate import solve_ivp
# sol2 = solve_ivp(lambda t,y: y-.5*math.exp(t/2)*math.sin(5*t)+5*math.exp(t/2)*math.cos(5*t),[0,10],[0])
# print("solve_ivp complete - yay!")
#
# plt.plot(exact_sol2[:,0],exact_sol2[:,1],'k-',label="Exact Solution")
# plt.plot(euler_sol2[:,0],euler_sol2[:,1],'r--',marker="*",label="Euler's Method")
# plt.plot(rk4_sol2[:,0],rk4_sol2[:,1],'b-.',marker="o",label="RK4 Method")
# plt.plot(sol2.t[:],sol2.y[0],'g.',marker="o", markersize=10,label="SciPy solve_ivp")
# plt.title("Numerical Solutions to the IVP y' = y - .5 exp(t/2)sin(5t) + 5 exp(t/2)cos(5t), y(0)=0")
# plt.xlabel("t")
# plt.ylabel("y")
# plt.legend()
# plt.show()


############################################
#
#       Assigned Problem Solutions:
#
############################################

# 5a) y' = t - y, y(0) = 4, until t_f = 10:

print("\n\nProblem 5a: Solve the IVP:\n y' = t - y, y(0) = 4, until t_f = 10:")
stepsize = .05
total_steps = int(10/0.05) # t_f/stepsize = 10/0.05
print("\nUse stepsize %f, and run for %d timesteps.\n" % (stepsize, total_steps))

print("Run the Euler's Method code:")
euler_sol5a = Euler(lambda t,y: t-y,0,4,stepsize,total_steps)

print("Run the RK4 code:")
rk4_sol5a = RK4(lambda t,y: t-y,0,4,stepsize,total_steps)
print("Generate another solution using scipy.integrate.solve_ivp:")
sol5a = solve_ivp(lambda t,y: t-y,[0,10],[4])
print("solve_ivp complete - yay!")

plt.plot(euler_sol5a[:,0],euler_sol5a[:,1],'r--',marker="*",label="Euler's Method")
plt.plot(rk4_sol5a[:,0],rk4_sol5a[:,1],'b-.',marker="o",label="RK4 Method")
plt.plot(sol5a.t[:],sol5a.y[0],'g.',marker="o", markersize=10,label="SciPy solve_ivp")
plt.title("Problem 5a: Numerical Solutions to the IVP y' = t - y, y(0) = 4")
plt.xlabel("t")
plt.ylabel("y")
plt.legend(loc="upper left")
plt.show()



# 5b) y' = (y-x)^2 + 1, y(0) = 1:

print("\n\nProblem 5b: Solve the IVP:\n y' = (y-x)^2 + 1, y(0) = 1, until t_f = 10:")
stepsize = .05
total_steps = int(10/0.05)+1 # t_f/stepsize = 10/0.05
print("\nUse stepsize %f, and run for %d timesteps.\n" % (stepsize, total_steps))

print("Run the Euler's Method code:")
euler_sol5b = Euler(lambda x,y: (y-x)**2,0,1,stepsize,total_steps)

print("Run the RK4 code:")
rk4_sol5b = RK4(lambda x,y: (y-x)**2,0,1,stepsize,total_steps)
print("Generate another solution using scipy.integrate.solve_ivp:")
#from scipy.integrate import solve_ivp
sol5b = solve_ivp(lambda x,y: (y-x)**2,[0,10],[1])
print("solve_ivp complete - yay!")

plt.plot(euler_sol5b[:,0],euler_sol5b[:,1],'r--',marker="*",label="Euler's Method")
plt.plot(rk4_sol5b[:,0],rk4_sol5b[:,1],'b-.',marker="o",label="RK4 Method")
plt.plot(sol5b.t[:],sol5b.y[0],'g.',marker="o", markersize=10,label="SciPy solve_ivp")
plt.title("Problem 5b: Numerical Solutions to the IVP y' = (y-x)^2 + 1, y(0) = 1")
plt.xlabel("t")
plt.ylabel("y")
plt.legend(loc="upper left")
plt.show()



# 5c) Solve the system -x' + y' = 6, -x' - y' = 13t, x(0) = 5, y(0) = 6
# First add the equations together and divide by -2 to get: x' = -3 -13/2*t
# Then y' = 6 + x' = 3 - 13/2*t
def fun5c(t,y):
    dydt = [-3 - 13*t/2, 3 - 13*t/2]
    return dydt

print("Generate a solution using scipy.integrate.solve_ivp:")
#from scipy.integrate import solve_ivp
sol5c = solve_ivp(fun5c,[0,10],[5,6])

print("Run the Euler's Method System code:")
euler_sol5c = EulerSys(fun5c,0,[5,6],stepsize,total_steps)
print("Run the RK4 System code:")
rk4_sol5c = RK4Sys(fun5c,0,[5,6],stepsize,total_steps)

plt.plot(euler_sol5c[:,0],euler_sol5c[:,1],'r--',marker="*",label="Euler's Method, x(t)")
plt.plot(euler_sol5c[:,0],euler_sol5c[:,2],'b--',marker="*",label="Euler's Method, y(t)")
plt.plot(rk4_sol5c[:,0],rk4_sol5c[:,1],'y-.',marker="x",label="RK4 Method, x(t)")
plt.plot(rk4_sol5c[:,0],rk4_sol5c[:,2],'g-.',marker="x",label="RK4 Method, y(t)")
plt.plot(sol5c.t[:],sol5c.y[0,:],'g-',marker="o", markersize=10,label="SciPy solve_ivp, x(t)")
plt.plot(sol5c.t[:],sol5c.y[1,:],'k--',marker="o", markersize=10,label="SciPy solve_ivp, y(t)")
plt.title("Problem 5c: Numerical Solutions to the IVP\n -x' + y' = 6, -x' - y' = 13t, x(0) = 5, y(0) = 6")
plt.xlabel("t")
plt.ylabel("y")
plt.legend(loc="lower left")
plt.show()

# 5d) Solve the system x' + y' = 6, -x' + y' = 13t, x(0) = 5, y(0) = 6
# First add the equations together and divide by 2 to get: y' = 3 + 13/2*t
# Then x' = 6 - y' = 3 - 13/2*t
def fun5d(t,y):
    dydt = [3 - 13*t/2, 3 + 13*t/2]
    return dydt

print("Generate a solution using scipy.integrate.solve_ivp:")
#from scipy.integrate import solve_ivp
sol5d = solve_ivp(fun5d,[0,10],[5,6])
print("Run the Euler's Method System code:")
euler_sol5d = EulerSys(fun5d,0,[5,6],stepsize,total_steps)
print("Run the RK4 System code:")
rk4_sol5d = RK4Sys(fun5d,0,[5,6],stepsize,total_steps)

plt.plot(euler_sol5d[:,0],euler_sol5d[:,1],'r--',marker="*",label="Euler's Method, x(t)")
plt.plot(euler_sol5d[:,0],euler_sol5d[:,2],'b--',marker="*",label="Euler's Method, y(t)")
plt.plot(rk4_sol5d[:,0],rk4_sol5d[:,1],'y-.',marker="x",label="RK4 Method, x(t)")
plt.plot(rk4_sol5d[:,0],rk4_sol5d[:,2],'g-.',marker="x",label="RK4 Method, y(t)")
plt.plot(sol5d.t[:],sol5d.y[0,:],'g-',marker="o", markersize=10,label="SciPy solve_ivp, x(t)")
plt.plot(sol5d.t[:],sol5d.y[1,:],'k--',marker="o", markersize=10,label="SciPy solve_ivp, y(t)")
plt.title("Problem 5d: Numerical Solutions to the IVP\n x' + y' = 6, -x' + y' = 13t, x(0) = 5, y(0) = 6")
plt.xlabel("t")
plt.ylabel("y")
plt.legend(loc="upper left")
plt.show()
