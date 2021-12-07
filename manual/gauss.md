Routine Name: gauss

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/a8dc1a242474c7e1d07c295b3fc340ca410e3de3/software/Matrix.py)

Purpose: This routine attempts to row reduce a matrix and use that to solve a system of equations. 

Input: You must input a matrix and a vector.

Output: This routine returns the reduced matrix and the solution to the system of equations.

Code:
```
def gauss(A,b):
    n=len(b)
    for k in range(n)
        for i in range(k+1,n):
            factor=A[i][k]/A[k][k]
# determine your factor to use in the computation.
            for j in range(n):
                A[i][j]=A[i][j]-factor*A[k][j]
# for each entry of A in the ith row, calculate the new value (and for b)
            b[i] -= factor*b[k]
    x = [1 for i in range(n)]
# Use the row reduced matrix to solve the system of equations.
    for i in range(n - 1, -1, -1):
        factor = b[i]
        for j in range(0, n):
            factor -= A[i][j] * x[j] if i != j else 0
        x[i] = factor / A[i][i]
    return(A,x)
# Return the solution.
```
Example input:

![image](https://user-images.githubusercontent.com/89805209/144941685-6fe55896-b21c-4587-afc2-844e35b7ccda.png)

output:

![image](https://user-images.githubusercontent.com/89805209/144941709-a4261f51-f7dd-42e1-a953-510e09d02809.png)


Last modified 12/2021
