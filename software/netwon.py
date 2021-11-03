import numpy as np
from matplotlib import pyplot as plt
def newton(x0, tol, maxiter):
    errlist = []
    iterlist = []
    #expression = input('Enter expression:\n')
    expression = "np.exp(-x**2)*np.sin(4*x**2-1)+.051"
    #expp = input('Enter Derivative of expression:\n')
    expp = "8*x*np.exp(-x**2)*np.cos(4*x**2-1)-2*x*np.exp(-x**2)*np.sin(4*x**2-1)"
    x = x0
    f0=eval(expression)
    fp0 = eval(expp)
    error = tol * 10
    iter=0
    while error > tol and iter < maxiter:
        x1 = x0 - f0/fp0
        error = np.abs(x1-x0)
        errlist.append(error)
        iterlist.append(iter)
        iter = iter + 1
        x0 = x1
        x=x0
        f0 = eval(expression)
        fp0 = eval(expp)
    #plt.loglog(iterlist, errlist)
    #plt.show()
# End plot stuff
    return x1

print(newton(2,.0001,1000))



