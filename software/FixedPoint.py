import numpy as  np
def g(x):
    return eval("x * np.exp( 3 * x ** 2)- 7 * x", {'x': x, 'np': np})

def FixedPoint(x0,tol,maxiter):
    eps= -.01
    iter=0
    error = 10 * tol
    while error > tol and iter < maxiter:
        x1=x0-eps*g(x0)
        error = np.abs(x1-x0)
        x0=x1
        iter = iter + 1
    return(x1)
print(FixedPoint(.5,.00001,10000))
