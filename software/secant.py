import numpy as np
def secant(x0, x1, tol, maxiter):
    expression = input('Enter expression:\n')
    x = x0
    f0=eval(expression)
    x = x1
    f1 = eval(expression)
    error = tol * 10
    iter=0
    while error > tol and iter < maxiter:
        x2 = x1 - f1 * (x1-x0)/(f1-f0)
        error = np.abs(x2-x1)
        iter = iter + 1
        x0 = x1
        x=x0
        f0 = eval(expression)
        x1=x2
        x = x1
        f1 = eval(expression)
    return x2

print(secant(1,2,.01,1000))