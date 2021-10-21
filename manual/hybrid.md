Routine Name: hybrid

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/1ea6abc7ef4a6d4584deb7c7da988a5eb3673085/software/hybrid.py)

Purpose: This routine attempts to find a root using a hybrid method of Newton's and bisection.

Input: You must input a lower and upper bound, tolerance and maximum iterations.

Output: This routine returns a root, if possible.

Code:

```
import numpy as np
def hybrid(a,b, tol, maxiter):
    #expression = input('Enter expression:\n')
    expression = "x*np.exp(3*x**2)-7*x"
    #expp = input('Enter Derivative of expression:\n')
    expp = "x*np.exp(3*x**2)*6*x+np.exp(3*x**2)-7"
c this code is set up to run the problem from Tasksheet 5. To set it up differently, switch the comments.
    x0= (a+b)/2
    x = x0
    f0=eval(expression)
    fp0 = eval(expp)
    x1= x0-f0/fp0
    e0=np.abs(b-a)
    e1 = np.abs(x0-x1)
    iter=0
    err=10*tol
c Do initial calculations. Find error, set iterations to 0, and so on.
    while err > tol and iter < maxiter:
        x1 = x0 - f0/fp0
        errnewt= np.abs(x1-x0)
        if errnewt > err:
c if newton wouldn't work, use bisection for 4 steps.
            for k in range(4):
                c=(a+b)/2
                x=a
                fa=eval(expression)
                x=c
                fc=eval(expression)
                if fa*fc <0:
                    b=c
                    fb=fc
                else:
                    a=c
                    fa=fc
                    # finish bisection method.
c go back and do Newton's method after the steps.                    
        x0=(a+b)/2
        x=x0
        f0=eval(expression)
        fp0=eval(expp)
        x1 = x0 - f0 / fp0
        error = np.abs(x1 - x0)
        iter = iter + 1
        x0 = x1
        x = x0
        f0 = eval(expression)
        fp0 = eval(expp)
c when we've reached our tolerance, we return x1.
    return x1

print(hybrid(.5,1,.001,1000))
```


