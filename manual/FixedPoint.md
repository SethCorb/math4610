Routine Name: Fixed Point

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/ac59c9f9599e79ff28343c7f2dcb67a630dd79a1/software/FixedPoint.py)

Purpose: This routine will give you a root based on fixed point iteration.

Input: The inputs are a guess, input, and maximum iteration.

Output: This routine returns a root.

Code:
```
import numpy as  np
def g(x):
    return eval("x * np.exp( 3 * x ** 2)- 7 * x", {'x': x, 'np': np})
c define your function
def FixedPoint(x0,tol,maxiter):
    eps= -.01
c define epsilon to meet convergence criteria
    iter=0
c set iteration count to 0
    error = 10 * tol
c set error so we run through the program at least once
    while error > tol and iter < maxiter:
        x1=x0-eps*g(x0)
c do the computation
        error = np.abs(x1-x0)
c find error
        x0=x1
c redefine x0
        iter = iter + 1
    return(x1)
print(FixedPoint(.5,.00001,10000))
```
Last modified 9/2021
