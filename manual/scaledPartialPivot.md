Routine Name: bisection

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/8b40911bc14e1a378849802ab5b3bc9fb9e13a24/software/LUDecomp.py)

Purpose: This uses sclaed partial pivoting to reduce a matrix A 

Input: You must input a matrix and a vector.

Output: This routine returns a reduced matrix.

Code:
```
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
```
Last modified 12/2021
