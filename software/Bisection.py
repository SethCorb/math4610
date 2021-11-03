import numpy as  np
import math
def f(x):
    return eval("np.exp(-x**2)*np.sin(4*x**2-1)+.051", {'x': x, 'np': np})

def bisection(a,b,tol):
    fa = f(a)
    iter = 0
    error = np.abs(b - a)
    k = math.ceil((math.log(error / tol) / math.log(2)) +1)
    for i in range(k):
        c = (a+b)/2
        fc = f(c)
        if fa * fc < 0:
            b = c
        else:
            a = c
        iter = iter + 1



    return c

print(bisection(0,1,.001))
