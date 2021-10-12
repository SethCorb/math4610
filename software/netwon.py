import numpy as np
def newton(x0, tol, maxiter):
    expression = input('Enter expression:\n')
    expp = input('Enter Derivative of expression:\n')
    x = x0
    f0=eval(expression)
    fp0 = eval(expp)
    error = tol * 10
    iter=0
    while error > tol and iter < maxiter:
        x1 = x0 - f0/fp0
        error = np.abs(x1-x0)
        iter = iter + 1
        x0 = x1
        x=x0
        f0 = eval(expression)
        fp0 = eval(expp)
    return x1

print(newton(1.5,.1,1000))



