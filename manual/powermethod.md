Routine Name: powerMethod

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/79f166f140753e09e5b14eb2a1cec61b6a701e1d/software/tasksheet10.py)

Purpose: This routine finds the largest eigenvalue 

Input: You must input a Matrix. You may input tolerance and max iterations.

Output: This routine returns the largest eigenvalue.

Code:
```
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
```
Last modified 9/2021

Example:

![image](https://user-images.githubusercontent.com/89805209/146589145-3d72cd31-154f-44c7-a3f8-7b82e16f0ac5.png)
