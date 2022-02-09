import numpy as np
import tasksheet10
import matvecop

def mat1Norm(A):
    oldsum= 0
    newsum=0
    n = len(A)
    for i in range(n):
        for j in range(n):
            newsum += A[i][j]
        if newsum > oldsum:
            oldsum = newsum
    return oldsum

def matInfNorm(A):
    oldsum = 0
    newsum = 0
    n = len(A)
    for i in range(n):
        for j in range(n):
            newsum += A[j][i]
        if newsum > oldsum:
            oldsum = newsum
    return oldsum

def mat2Norm(A):
    return np.sqrt(tasksheet10.powerMethod(matvecop.matrix_multiplication(matvecop.matrix_transpose(A),A)))

print(mat2Norm(tasksheet10.diagDomSym(100)))