import numpy as np
import Matrix

def luDecomp(A):
    n=len(A)
    for i in range(0,n-1):
        for j in range(i+1,n):
            factor = A[j][i]/A[i][i]
            A[j][i+1:n] = A[j][i+1:n] - factor * A[i][i+1:n]
            A[j][i] = factor
    return A

def lu(A):
    n=len(A)
    L=[]
    for i in range(n):
        L.append([])
    for i in L:
        for j in range(n):
            i.append(0)
    for i in range(n):
        L[i][i]=1
    for k in range(n):
        for i in range(k+1,n):
            factor=A[i][k]/A[k][k]
            L[i][k] = factor
            for j in range(n):
                A[i][j]=A[i][j]-factor*A[k][j]
  #  print(np.dot(L,A))
    return(A,L)

def hilbertMatrix(n):
    H = []
    for i in range(n):
        H.append([])
    for i in range(len(H)):
        for j in range(n):
            H[i].append(1/(i+1+j))
    return H

def forwardSub(L,b):
    sol = []
    for i in range(len(b)):
        sol.append(b[i])
        for j in range(i):
            sol[i]=sol[i]-L[i,j]*sol[j]
        x[i] = x[i]/L[i,i]
    return x

#print(lu(Matrix.RandSqMat(3)))
print(Matrix.gauss([[3,-2,1],[1,-3,2],[-1,2,4]],[1,2,4]))
#print(Matrix.gauss([[-4,2,1],[1,6,2],[1,-2,5]],[1,2,5]))
#print(Matrix.gauss([[1,2,4],[2,4,8],[4,8,16]],[1,1,1]))
#print(Matrix.RandSqMat(3))

