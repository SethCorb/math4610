Routine Name: mat1Norm

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/e5ecbf9615953f2f4ac46a5be4b117212b92743d/software/matNorms.py)

Purpose: This routine finds the 1-norm of a matrix 

Input: You must input a matrix.

Output: This routine returns the 1-norm.

Code:
```
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
```
Last modified 12/2021

Output from example:

![image](https://user-images.githubusercontent.com/89805209/146589582-0f7c54e4-43d8-48f3-a644-801a3cb767c1.png)

---

Routine Name: matInfNorm

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/e5ecbf9615953f2f4ac46a5be4b117212b92743d/software/matNorms.py)

Purpose: This routine finds the inf-norm of a matrix 

Input: You must input a matrix.

Output: This routine returns the inf-norm.

Code:
```
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
```
Last modified 12/2021

Output from example:

![image](https://user-images.githubusercontent.com/89805209/146589835-4c70434a-e95d-49e2-9691-c0718c6b412a.png)

---

Routine Name: mat2Norm

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/e5ecbf9615953f2f4ac46a5be4b117212b92743d/software/matNorms.py)

Purpose: This routine finds the 2-norm of a matrix 

Input: You must input a matrix.

Output: This routine returns the 2-norm.

Code:
```
![image](https://user-images.githubusercontent.com/89805209/146589910-4b66d06a-6dd6-4956-bdfc-5388d43350db.png)
```
Last modified 12/2021

Output from example:

![image](https://user-images.githubusercontent.com/89805209/146589990-e733d44d-7a0a-41d4-aedd-175f05e015df.png)

