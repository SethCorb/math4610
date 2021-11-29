import numpy as np
import random

def defMat(n):
    A = []
    b = []
    for i in range(n):
        A.append([])
        b.append(1)
    for i in range(n):
        for j in range(n):
            if i >= j:
                A[j].append(i+j+1)
            else:
                A[j].append(0)
    return A

def MatTranspose(A):
    n = len(A)
    B = []
    for i in A:
        B.append([])
    for i in range(n):
        for j in range(n):
            B[i].append(A[j][i])
    return B

def backsub(A):
    n=len(A)
    b=[]
    for i in range(n):
        b.append(1)
    x=[]
    for i in range(n):
        x.append(0)
    m=n-1
    x[m]=b[m]/A[m][m]
    for i in range(m-1,-1,-1):
        sum=b[i]
        for j in range(i+1,n):
            sum=sum-A[i][j]*x[j]
        x[i]=sum/A[i][i]
    return x

def RandSqMat(n,seed=10):
    A=[]
    random.seed(seed)
    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append(random.randint(1,10))
    return(A)

def RandLowMat(n,seed=10):
    A=[]
    random.seed(seed)
    for i in range(n):
        A.append([])
        for j in range(n):
            if i >= j:
                A[i].append(random.randint(1,10))
            else:
                A[i].append(0)
    return(A)

def RandUpMat(n,seed=10):
    A=[]
    random.seed(seed)
    for i in range(n):
        A.append([])
        for j in range(n):
            if i <= j:
                A[i].append(random.randint(1,10))
            else:
                A[i].append(0)
    return(A)

def RandDiagMat(n,seed=10):
    A=[]
    random.seed(seed)
    for i in range(n):
        A.append([])
        for j in range(n):
            if i == j:
                A[i].append(random.randint(-10,10))
            else:
                A[i].append(0)
    return(A)

def Gauss(A,b):
    n=len(b)
    for k in range(n):
        for i in range(k+1,n):
            factor=A[i][k]/A[k][k]
            for j in range(n):
                A[i][j]=A[i][j]-factor*A[k][j]
    return(A)


print(Gauss(RandSqMat(3,4),[1,1,1]))