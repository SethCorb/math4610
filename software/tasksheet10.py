import numpy as np
import matvecop as mv
import Matrix as mat
import copy
import random

def diagDomSym(n):
    A = [[] for i in range(n)]
    #for i in A:
     #   for j in range(n):
      #      i.append([])
    for i in range(n):
        for j in range(i):
            A[i].append(random.randint(1,5))
            A[j].append(random.randint(1,5))
    for i in range(n-1):
        sum = 0
        for j in range(n-1):
            sum += A[i][j]
        A[i][i] = sum+1
    for i in range(n):
        A[i].append(1)
    return A

def powerMethod(A,tolerance=.01,maxiter=1000):
    oldLam=1
    iter = 1
    err = 10*tolerance
    x = [1 for i in range(len(A))]
    while tolerance < err and iter < maxiter:
        x= mv.matrix_vector_multiplication(A,x)
        newLam = np.abs(x).max()
        x = x/newLam
        iter +=1
        err = np.abs(newLam-oldLam)
        oldLam=newLam
    return newLam

def invPowerMethod(A,tolerance=.01,maxiter=1000):
    y = [1 for i in range(len(A))]
    err = tolerance * 10
    iter = 0
    oldLam = 1
    while iter < maxiter and err > tolerance:
        B=copy.deepcopy(A)
        y=mat.gauss(B,y)[1]
        v = [ i / np.linalg.norm(y) for i in y]
        B=copy.deepcopy(A)
        q = mat.gauss(B,v)[1]
        newLam = mv.dot_product(v,q)
        err = np.abs(newLam-oldLam)
        iter+=1
        oldLam = newLam
        y = copy.deepcopy(v)
    return newLam

