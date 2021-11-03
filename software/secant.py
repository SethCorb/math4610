import numpy as np
from matplotlib import pyplot as plt
def secant(x0, x1, tol, maxiter):
    expression = input('Enter expression:\n')
    errlist = []
    iterlist=[]
    x = x0
    f0=eval(expression)
    x = x1
    f1 = eval(expression)
    error = tol * 10
    iter=0
    while error > tol and iter < maxiter:
        x2 = x1 - f1 * (x1-x0)/(f1-f0)
        error = np.abs(x2-x1)
        errlist.append(error)
        iter = iter + 1
        iterlist.append(iter)
        x0 = x1
        x = x0
        f0 = eval(expression)
        x1=x2
        x = x1
        f1 = eval(expression)

# plot stuff
    loglist = []
    for i in errlist:
        loglist.append(np.log(i))
    plt.plot(iterlist,loglist)
    plt.show()
# end plot stuff

    return x2

print(secant(0,.5,.001,1000))