Routine Name: Newton

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/356463679483beaecf373ca7f37e1cff1aade7ef/software/netwon.py)

Purpose: This routine attempts to find a root 

Input: You must input a guess, function, derivative, tolerance and maximum iterations.

Output: This routine returns a root, if possible.

Code:
```
import numpy as np
from matplotlib import pyplot as plt

def newton(x0, tol, maxiter):
    errlist = []
    iterlist = []
c set up empty lists to be used for x, y values.
    expression = input('Enter expression:\n')
c input an expression then its derivative.
    expp = input('Enter Derivative of expression:\n')
    x = x0
    f0=eval(expression)
c evaluate your expression and its derivative at your guess.
    fp0 = eval(expp)
    error = tol * 10
    iter=0
c set iterations to 0 and define error so it will run through at least once.
    while error > tol and iter < maxiter:
        x1 = x0 - f0/fp0
        error = np.abs(x1-x0)
        errlist.append(error)
        iterlist.append(iter)
c do the calculation and add the error to the error list, iter to the iter list.
        iter = iter + 1
c step up the iteration count
        x0 = x1
c set new x0
        x=x0
        f0 = eval(expression)
        fp0 = eval(expp)
    plt.loglog(iterlist, errlist)
    plt.show()
c plot the logs of x and y to see convergence.

# End plot stuff

    return x1

print(newton(.05,.01,1000))
```
Last modified 9/2021

Output from example:
![image](https://user-images.githubusercontent.com/89805209/138352644-442f50e1-48d6-4c0e-bb6b-8ee55ce26d11.png)
