import numpy as  np

#i = input("fn")
def f(x):
    return eval("x * np.exp( 3 * x ** 2)- 7 * x", {'x': x, 'np': np})

def bisection(a,b,tol,maxiter):
    fa = f(a)
    error = 10 * tol
    iter = 0
    while error > tol and iter < maxiter:
        c = (a+b)/2
        fc = f(c)
        if fa * fc < 0:
            b = c
        else:
            a = c
        iter = iter + 1
        error = np.abs(b-a)


    return c

print(bisection(-.5,.5,.01,100))