Routine Name: bisection

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/681c0ae37bf779e3682a5e1a084587d9c3a1a98c/software/Bisection.py)

Purpose: This routine attempts to find a root 

Input: You must input a lower and upper bound, tolerance and maximum iterations.

Output: This routine returns a root, if possible.

Code:
```
import numpy as  np
def f(x):
    return eval("x * np.exp( 3 * x ** 2)- 7 * x", {'x': x, 'np': np})
c define your function
def bisection(a,b,tol,maxiter):
    fa = f(a)
c find f(a)
    error = 10 * tol
c define error to run through the loop at least once.
    iter = 0
c start iteration count at 0.
    while error > tol and iter < maxiter:
c define your loop so it will continue until conditions are satisfied
        c = (a+b)/2
c define c as your midpoint of a, b
        fc = f(c)
c find f(c)
        if fa * fc < 0:
            b = c
        else:
            a = c
c change a or b to be c to tighten your interval
        iter = iter + 1
        error = np.abs(b-a)
c find your error and iteration
    return c
```
Last modified 9/2021
