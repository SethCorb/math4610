Routine Name: Newton

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/7407cb714c2b2213922d7db7f78600434cf2e8ec/software/secant.py)

Purpose: This routine attempts to find a root 

Input: You must input a guess, function, derivative, tolerance and maximum iterations.

Output: This routine returns a root, if possible.

Code:
```
import numpy as np
from matplotlib import pyplot as plt
# import needed modules.
def secant(x0, x1, tol, maxiter):
    expression = "x*np.exp(3*x**2)-7*x"
    #expression = input('Enter expression:\n')
    errlist = []
    iterlist=[]
    x = x0
    f0=eval(expression)
    x = x1
    f1 = eval(expression)
    error = tol * 10
    iter=0
# Initialize needed values.
    while error > tol and iter < maxiter:
        x2 = x1 - f1 * (x1-x0)/(f1-f0)
# Perform the secant step
# Then find the error.
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
# Redefine variables for the next step

# plot stuff
    loglist = []
    for i in errlist:
        loglist.append(np.log(i))
    plt.plot(iterlist,loglist)
    plt.show()
# end plot stuff

    return x2
print(secant(0.7,1,.001,1000))

```
Last modified 10/2021


