import Task92
import LUDecomp
import Matrix
import random

def diagDomSym(n):
    A = [[] for i in range(n)]
    #for i in A:
     #   for j in range(n):
      #      i.append([])
    for i in range(n):
        for j in range(i+1):
            A[i].append(random.randint(1,5))
            A[j].append(random.randint(1,5))
    for i in range(n-1):
        sum = 0
        for j in range(n-1):
            sum += A[i][j]
        A[i][i] = sum+1
    return A

def jacobi(A,b,tol,maxiter):
    n = len(b)
    error = 10 * tol
    iter = 0
    r = [1 for i in range(n)]
    x1 = [1 for i in range(n)]
    x = [1 for i in range(n)]
    while error > tol and iter < maxiter:
        for i in range(n):
            r[i] = b[i]
            for j in range(i-1):
                r[i] = r[i] - A[i][j]*x[j]
        for i in range(n):
            x1[i] = x[i] - r[i]/A[i][i]
        error = Task92.l2Err(x,x1)
        iter += 1
        for i in range(n):
            x[i]=x1[i]
    return x1

def mrGauss():
    print(Matrix.gauss(LUDecomp.hilbertMatrix(3),[1,1,1])[1])
#mrGauss()
#print(jacobi(LUDecomp.hilbertMatrix(3),[1,1,1],.1,1000))

def bigBoy():
    A = diagDomSym(100)
    b = LUDecomp.matVecMult(A,[1 for i in range(len(A))])
    err = Task92.l2Err(Matrix.gauss(A,b)[1],[1 for i in range(len(A))])
    print("gaussian error:", err)
    err = Task92.l2Err(jacobi(A,b,.01,100),[1 for i in range(len(A))])
    print("jacobi error:", err)
bigBoy()
