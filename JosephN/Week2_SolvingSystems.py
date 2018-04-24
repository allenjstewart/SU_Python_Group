# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:18:40 2018

@author: Joey
"""

# AUTHOR: J. Nakao
# DATE: 24 April 2018
# PURPOSE: Newton's method for solving 2D-nonlinear systems of ODEs.
# INSTRUCTIONS:
# 1. Declare functions f(x,y) and g(x,y).
# 2. Declare step sizes, dx and dy, for derivative.
# COMMENTS: N/A.
# 
# 
import numpy as np
import time as tm

###################################
# Declare functions (the system) to solve.
def f(x,y):
    return y-x**2-np.cos(np.pi*x)
def g(x,y):
    return (1/x)-y*x-np.exp(-y)
x0 = 1 #initial x-point.
y0 = 1 #initial y-point.
dx = 0.00000001
dy = 0.00000001
###################################

# Derivative of f w.r.t. x.
def f_x(x,y,dx):
    return (f(x+dx,y)-f(x,y))/dx

# Derivative of f w.r.t. y.
def f_y(x,y,dy):
    return (f(x,y+dy)-f(x,y))/dy

# Derivative of g w.r.t. x.
def g_x(x,y,dx):
    return (g(x+dx,y)-g(x,y))/dx

# Derivative of g w.r.t. y.
def g_y(x,y,dy):
    return (g(x,y+dy)-g(x,y))/dy

# Determinent of Jacobian matrix (2x2 matrix).
def det(x,y):
    return (f_x(x,y,dx)*g_y(x,y,dy))-(f_y(x,y,dy)*g_x(x,y,dx))

# Newton's method for 2D-system of nonlinear equations.
def Newton(x,y):
    tic = tm.time()
    tol = 0.00000001 #tolerance.
    ftol = 1 #f(x,y) tolerance.
    gtol = 1 #g(x,y) tolerance.
    count = 0 #number of iterations.
    while ftol>tol and gtol>tol:
        count += 1
        x = x - (((f(x,y)*g_y(x,y,dy))/det(x,y)) - ((g(x,y)*f_y(x,y,dy))/det(x,y)))
        y = y - (-((f(x,y)*g_x(x,y,dx))/det(x,y)) + ((g(x,y)*f_x(x,y,dx))/det(x,y)))
        ftol = np.abs(f(x,y))
        gtol = np.abs(g(x,y))
    toc = tm.time() - tic
    print("Solution:",x,y)
    print("Number of iterations:",count)
    print("Time run:",toc)

Newton(x0,y0)




















