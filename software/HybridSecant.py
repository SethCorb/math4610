import numpy as np


def hybrid(a, b, tol, maxiter):
    # expression = input('Enter expression:\n')
    expression = "np.exp(-x**2)*np.sin(4*x**2-1)+.051"
    x0= (a+b)/2
    x=a
    x0=a
    f0 = eval(expression)
    x1=b
    x=b
    f1 = eval(expression)
    error = tol * 10
    iter = 0
    err = 5 * tol
    error = 1000
    zerolist = []
    increment = .01
    lowbound=a
    x=lowbound
    solist= []
    fl=eval(expression)
    zerolist = []
    while True:
        upbound=lowbound+increment
        x=upbound
        fu=eval(expression)

        if fl*fu<0:
            zerolist.append(lowbound)
        lowbound+=increment
        fl=eval(expression)
        if lowbound > b:
            break
    fl = fu
    for i in zerolist:
        a = i
        b = i+increment
        x=a
        x0=a
        f0 = eval(expression)
        x=b
        x1=b
        f1 = eval(expression)
        while err > tol and iter < maxiter:
            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
            errsec = np.abs(x2 - x1)
            err = errsec
            if errsec > error:
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
            x = x1
            f1 = eval(expression)
            iter=0
            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
            error = np.abs(x2 - x1)
            iter = iter + 1
            x0 = x1
            x = x0
            f0 = eval(expression)
            x1 = x2
            x = x1
            f1 = eval(expression)
        solist.append(x1)
    abslist = []
    for i in solist:
        abslist.append(np.abs(i))
    return min(abslist)


print(hybrid(-5, 6, .001, 1000))
