import numpy as  np
import math
def f(x):
    return eval("x * np.exp( 3 * x ** 2)- 7 * x", {'x': x, 'np': np})

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

print(bisection(.3,.9,.001))
