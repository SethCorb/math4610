# Task 1

![image](https://user-images.githubusercontent.com/89805209/138328423-8ff10ed7-4add-41bd-8ed3-722549142751.png)

![image](https://user-images.githubusercontent.com/89805209/138328455-c74cd3b4-4590-4469-a00a-99782a6d9cca.png)

Output:

![image](https://user-images.githubusercontent.com/89805209/138328488-1c9d53f2-8ec9-4ccd-b1fb-e1fd8403dbe2.png)


# Task 2

![image](https://user-images.githubusercontent.com/89805209/138329897-237169b5-51cb-45b8-b82b-db64223a5bfc.png)

![image](https://user-images.githubusercontent.com/89805209/138329927-2035d11c-041b-4290-add6-7996e70fafcf.png)

Output:

![image](https://user-images.githubusercontent.com/89805209/138329958-e2202476-d18e-4dbc-8a34-7b66785f06e4.png)


# Task 3

![image](https://user-images.githubusercontent.com/89805209/138330332-2fd214ac-8ccd-4b9d-839f-2c2c67aeb15a.png)

# Task 4

![image](https://user-images.githubusercontent.com/89805209/138330421-29ad2c8d-9db1-42df-a94a-ed3a4a2eac0c.png)

# Task 5
Code:
```
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
```
Output:

![image](https://user-images.githubusercontent.com/89805209/138352803-71048b92-6848-4d54-bf01-f11d45c49e20.png)

# Task 6

An advantage of the Bisection method is that it is fairly robust. It is harder to break than the others, but it does gain accuracy slower, which can be a downside. Newton's method and Secant method both converge more quickly than the bisection method. Newton's method is the fastest, but requires computation of a derivative, which can be difficult. Secant method does not require a derivative, which is nice.

[https://en.wikipedia.org/wiki/Root-finding_algorithms#Newton's_method_(and_similar_derivative-based_methods)](https://en.wikipedia.org/wiki/Root-finding_algorithms#Newton's_method_(and_similar_derivative-based_methods))
