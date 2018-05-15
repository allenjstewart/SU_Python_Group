################################################################################
#
#   Newton's Method Code
#
#       Find solutions to f(x) = 0 using an initial guess of x_1
#
################################################################################
#   Resources:
#
#    Newton's Method:
#       http://tutorial.math.lamar.edu/Classes/CalcI/NewtonsMethod.aspx
#    Invert a matrix:
#       https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.linalg.html
#
################################################################################
#   https://user.xmission.com/~emailbox/ascii_cats.htm
#
#       _
#       \`*-.
#        )  _`-.
#       .  : `. .
#       : _   '  \
#       ; *` _.   `*-._
#       `-.-'          `-.
#         ;       `       `.
#         :.       .        \
#         . \  .   :   .-'   .
#          '  `+.;  ;  '      :
#          :  '  |    ;       ;-.
#          ; '   : :`-:     _.`* ;
# [bug] .*' /  .*' ; .*`- +'  `*'
#       `*-*   `*-*  `*-*'
#
################################################################################
#
# libraries needed:
from math import *      # Try importing all of math this time
import numpy as np      # Needed for arrays and inverting matrices

# Use Newton's Method to solve f(x) = 0, given an initial guess of x1.
# stop when successive iterations agree up to tolerance level tol
# The code will autmatically quit if more than max_iter iterations are needed

def Newton(f, fprime, x1, tol, max_iter):
    x_old = x1
    x_new = x_old - f(x_old)/fprime(x_old)
    # print("x_new = %f, x_old = %f" % (x_new, x_old))
    count = 1
    while (abs(x_new - x_old) > tol):
        # print("Next Guess:", x_new)
        # print("x_old - x_new = ", x_old - x_new)
        count += 1
        if (count > max_iter):
            print("Maximum iterations (%d) reached." % (max_iter))
            break
        x_old = x_new
        x_new = x_old - f(x_old)/fprime(x_old)
    print("Approximate Solution: x = %f, after %d iterations" % (x_new, count))
    return x_new

# Use Newton's method to solve a system of equations F(x) = 0,
# where x is a vector, J is the Jacobian matrix (partial derivatives),
# x1 is the initial guess, tol is the tolerance, and max_iter is the maximum
# number of times that the program will iterate through the while loop before
# terminating if the solution has not converged within the tolerance requested
def NewtonSys(f, J, x1, tol, max_iter):
    x_old = x1
    print("J(x) = ", J(x_old))
    print("f(x) = ", f(x_old))
    x_new = x_old - np.matmul(np.linalg.inv(J(x_old)),f(x_old))
    print("x_new = ", x_new)
    count = 1
    delta = abs(x_new - x_old)
    while (max(delta) > tol):
        # print("Next Guess:", x_new)
        # print("x_old - x_new = ", x_old - x_new)
        count += 1
        if (count == max_iter):
            print("Maximum iterations (%d) reached." % (max_iter))
            break
        x_old = x_new
        x_new = np.matmul(np.linalg.inv(J(x_old)),f(x_old))
    print("Approximate Solution: x = ", x_new)
    print("after %d iterations" % (count))
    return x_new

print("\n\nTest the code with f(x) = cos(x) - x, x1 = 1, tol = 0.00001")

Newton(lambda x: cos(x)-x, lambda x: - 1 - sin(x), 1, 0.0000000001, 100)

print("\n\nTest the system code with f(x) = [[x1^2 + x2^2 - 1], [x2 - x1^2]],")
print("x0 = [[0.5],[0.5]], tol = 0.00001")
NewtonSys(lambda x: [[x[0][0]**2 + x[1][0]**2 - 1], [x[1][0]-x[0][0]**2]], lambda x: [[2*x[0][0], 2*x[1][0]], [-2*x[0][0], 1.0]], [[0.5],[0.5]], 0.0000000001, 100)
