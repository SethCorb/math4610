Code For Question 1:
```

import numpy as np
import matplotlib.pyplot as plt
def partA():
    # Define our function.
    f = "(t+1)*u"
    # Set your initial conditions, add the first point to our list
    un = 1
    t=0
    U = []
    U.append(1)
    for i in range(10):
        # Set up and solve for K1
        u = un
        k1=eval(f)
        t = t+.05
        u = un + .05*k1
        # Set up and solve for k2
        k2 = eval(f)
        u = un + .05*k2
        # Set up and solve for k3
        k3 = eval(f)
        u = un+.1*k3
        t = t + .05
        # Set up and solve for k4
        k4 = eval(f)
        # Find the next step based on k1,k2,k3,k4
        un = un + .1/6*(k1+2*k2+2*k3+k4)
        U.append(un)
    x=0
    #Define our true solution
    sol = "np.exp(.5*x ** 2 + x)"
    solist = []
    err = []
    xlist = []
    #Determine error at each point
    for i in range(11):
        x= .1*i
        xlist.append(x)
        solist.append(eval(sol))
        err.append(solist[i]-U[i])


    plt.plot(xlist,err)
    plt.show()
partA()
```
Error Graph Output:

![image](https://user-images.githubusercontent.com/89805209/155854912-954afcf5-86c6-4515-85d5-2591a8e677e0.png)

Question 2 Code:
```
def Q2():
    # Define our function and initial conditions
    f = "(t+1)*u"
    un = 1
    t = .05
    U = []
    U.append(1)
    # Use forward Euler to get the first step
    u = un
    U.append(un+.05*eval(f))
    # Use Midpoint method to find all other U values
    for i in range(1,20):
        u = U[i]
        t = (i) * .05
        U.append(U[i-1]+.1*eval(f))
    print(U)
    xlist = []
    solist = []
    sol = "np.exp(.5*x ** 2 + x)"
    err = []
    # Find Error
    for i in range(21):
        x= .05*i
        xlist.append(x)
        solist.append(eval(sol))
        err.append(np.abs(solist[i]-U[i]))
    # Plot Error
    plt.plot(xlist, err)
    plt.show()
Q2()
```

Error Graph Output:

![image](https://user-images.githubusercontent.com/89805209/155854855-750b0bf4-3146-4009-a2ff-16fa292d0fe9.png)



