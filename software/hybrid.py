import numpy as np
def hybrid(a,b, tol, maxiter):
    #expression = input('Enter expression:\n')
    expression = "x*np.exp(3*x**2)-7*x"
    #expp = input('Enter Derivative of expression:\n')
    expp = "x*np.exp(3*x**2)*6*x+np.exp(3*x**2)-7"
    x0= (a+b)/2
    x = x0
    f0=eval(expression)
    fp0 = eval(expp)
    x1= x0-f0/fp0
    e0=np.abs(b-a)
    e1 = np.abs(x0-x1)
    iter=0
    err=10*tol
    while err > tol and iter < maxiter:
        x1 = x0 - f0/fp0
        errnewt= np.abs(x1-x0)
        if errnewt > err:
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
    return x1

print(hybrid(.5,1,.001,1000))



