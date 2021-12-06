import numpy as np
import Matrix

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
    n=len(L)
    for i in range(n):
        sol.append(b[i])
        for j in range(i):
            sol[i]=sol[i]-L[i][j]*sol[j]
        sol[i] = sol[i]/L[i][i]
    return sol

def scaledPartialPivot(A,b):
    n=len(A)
    s = []
    for i in range(n):
        s.append(np.abs(A[i][0]))
        for j in range(n):
            temp1=np.abs(A[i][j])
            if temp1>s[i]:
                s[i]=temp1
    for k in range(n-1):
        temp1=np.abs(A[k][k]/s[k]);
        q=k
        for i in range(k+1,n):
            temp2 = np.abs(A[i][k]/s[k])
            if temp2 > temp1:
                temp1=temp2
                q=i
    for j in range(n):
        temp1=A[q][j]
        A[q][j] = A[k][j]
        A[k][j] = temp1
    temp1 = b[q]
    b[q] = b[k]
    b[k] = temp1
    temp1 = s[q]
    s[q] = s[k]
    s[k] = temp1
    for k in range(n):
        for i in range(k+1,n):
            factor=A[i][k]/A[k][k]
            for j in range(n):
                A[i][j]=A[i][j]-factor*A[k][j]
                b[i] -= factor*b[k]
    return(A)

def matVecMult(A,b):
    n=len(b)
    x = [0 for i in range(n)]
    sum=0
    for j in range(n):
        for i in range(n):
            sum += A[j][i]*b[i]
        x[j]=sum
        sum=0
    return x

#print(matVecMult(hilbertMatrix(3),[1,1,1]))

#for j in range(3,11):
#    b = matVecMult(hilbertMatrix(j),[1 for i in range(j)])
#    print("Solution for", j, "by", j, "is:")
#    print(forwardSub(scaledPartialPivot(hilbertMatrix(j),b),b))
