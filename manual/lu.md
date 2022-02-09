Routine Name: lu

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/8b40911bc14e1a378849802ab5b3bc9fb9e13a24/software/LUDecomp.py)

Purpose: This routine attempts to find the LU factorization of a matrix 

Input: You must input a matrix.

Output: This routine returns an upper and a lower matrix.

Code:
```
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
    return(A,L)
```
Last modified 12/2021
