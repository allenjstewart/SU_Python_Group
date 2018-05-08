################################################################################
#
#   ODE Challenge:
#
#     Solve the stiff van der Pol equation, with mu=1000:
#           y1' = y2
#           y2' = mu*(1-y1^2)*y2 - y1
#           y1(0) = 2
#           y2(0) = 0
#           from t=0 to t=3000
#   Source:
#     https://www.mathworks.com/help/matlab/math/solve-stiff-odes.html
#
################################################################################


def vanderpol(t, y):
    mu = 1000
    dydt = [y[1], mu*(1-y[0]**2)*y[1] - y[0]]
    return dydt
