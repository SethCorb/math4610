import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
def parta():
    f = "(t+1)*u"
    un = 1
    t=0
    U = []
    U.append(1)
    for i in range(10):
        u = un
        k1=eval(f)
        t = t+.05
        u = un + .05*k1
        k2 = eval(f)
        u = un + .05*k2
        k3 = eval(f)
        u = un+.1*k3
        t = t + .05
        k4 = eval(f)
        un = un + .1/6*(k1+2*k2+2*k3+k4)
        U.append(un)
    print(U)
    x=0
    sol = "np.exp(.5*x ** 2 + x)"
    solist = []
    err = []
    xlist = []
    for i in range(11):
        x= .1*i
        xlist.append(x)
        solist.append(eval(sol))
        err.append(solist[i]-U[i])


    plt.plot(xlist,err)
    plt.show()
def Q2():
    f = "(t+1)*u"
    un = 1
    t = 0
    U = []
    U.append(1)
    u = un
    U.append(un+.05*eval(f))
    for i in range(1,20):
        u = U[i]
        t = (i+2) * .05
        U.append(U[i-1]+.1*eval(f))
    print(U)
    xlist = []
    solist = []
    sol = "np.exp(.5*x ** 2 + x)"
    err = []
    for i in range(21):
        x= .05*i
        xlist.append(x)
        solist.append(eval(sol))
        err.append(np.abs(solist[i]-U[i]))
    plt.plot(xlist, err)
    plt.show()
Q2()