import numpy as np
from matplotlib import pyplot as plt

def newton(x0, tol, maxiter):
    errlist = []
    iterlist = []
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
        errlist.append(error)
        iterlist.append(iter)
        iter = iter + 1
        x0 = x1
        x=x0
        f0 = eval(expression)
        fp0 = eval(expp)
# plot stuff
#    loglist = []
#    logiter= []
#    for i in errlist:
#        loglist.append(np.log(i))
#    for i in iterlist:
#        logiter.append(np.log(i))
#    print(loglist,logiter)
#    plt.plot(logiter,loglist)
#    plt.show()
    newerr = [1]
    for i in errlist:
        newerr.append(i)
    plt.loglog(iterlist, errlist)
    plt.show()

# End plot stuff

    return x1

print(newton(.05,.01,1000))



