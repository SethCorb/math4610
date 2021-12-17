Routine Name: invPowerMethod

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/f962d36897af014f3ab6303fa7e9572425761968/software/tasksheet10.py)

Purpose: This routine finds the smallest eigenvalue of a matrix 

Input: You must input a matrix.

Output: This routine returns the smallest eigenvalue of a matrix.

Code:
```
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
    return newLam
```
Last modified 12/2021

Output from example:

![image](https://user-images.githubusercontent.com/89805209/146590280-f5352c79-4497-4d70-a252-d0a2e0f7a754.png)
