import numpy as np
import matvecop as mv
import Matrix as mat
import copy

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
        print(newLam)
    return newLam
print(invPowerMethod([[1,2],[2,1]]))