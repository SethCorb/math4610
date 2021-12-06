import numpy as np

def l2norm(x):
    n=len(x)
    doubleSum = 0
    for i in range(n):
        doubleSum +=x[i] *x[i]
    return np.sqrt(doubleSum)

def l1norm(x):
    n=len(x)
    sum=0
    for i in range(n):
        sum+= np.abs(x[i])
    return(sum)

def lInfNorm(x):
    return max(x)

def l2Err(x,y):
    n=len(x)
    sum=0
    for i in range(n):
        diff = x[i]-y[i]
        sum+= diff * diff
    return np.sqrt(sum)

def l1Err(x,y):
    n=len(x)
    sum = 0
    for i in range(n):
        diff = x[i] - y[i]
        sum+= np.abs(diff)
    return sum

def lInfErr(x,y):
    z=[]
    for i in range(len(x)):
        z.append(np.abs(x[i]-y[i]))
    return max(z)
