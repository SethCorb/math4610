import numpy as np

def luDecomp(A):
    n=len(A)
    lMatrix = [[0] * n for i in range(n)]
    uMatrix = [[0] * n for i in range(n)]
    U = A.copy()
    for i in range(n):
        L[i][i] = 1

