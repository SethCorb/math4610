import numpy as np


def hybrid(a, b, tol, maxiter):
    # expression = input('Enter expression:\n')
    expression = "np.exp(-x**2)*np.sin(4*x**2-1)+.051"
    # expp = input('Enter Derivative of expression:\n')
    expp = "8*x*np.exp(-x**2)*np.cos(4*x**2-1)-2*x*np.exp(-x**2)*np.sin(4*x**2-1)"
    x0 = (a + b) / 2
    x = x0
    f0 = eval(expression)
    fp0 = eval(expp)
    x1 = x0 - f0 / fp0
    e0 = np.abs(b - a)
    e1 = np.abs(x0 - x1)
    iter = 0
    err = 5 * tol
    error = 1000
    while err > tol and iter < maxiter:
        x1 = x0 - f0 / fp0
        errnewt = np.abs(x1 - x0)
        if errnewt > error:
            for k in range(4):
                x = a
                fa = eval(expression)
                x = b
                fb = eval(expression)
                if fa * fb < 0:
                    continue
                c = (a + b) / 2
                x = c
                fc = eval(expression)
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc
                x0 = (a + b) / 2
                # finish bisection method.

        x = x0
        f0 = eval(expression)
        fp0 = eval(expp)
        x1 = x0 - f0 / fp0
        error = np.abs(x1 - x0)
        iter = iter + 1
        x0 = x1
        x = x0
        f0 = eval(expression)
        fp0 = eval(expp)
    return x1


print(hybrid(-5, 6, .001, 1000))
