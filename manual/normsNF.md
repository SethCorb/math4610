Routine Name: l2norm

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/952fb981c136355401c3f7b99ae3217904b160eb/software/Task92.py)

Purpose: This routine finds the l-2 norm. 

Input: You must input a vector.

Output: This routine returns the l-2 norm.

Code:
```
def l2norm(x):
    n=len(x)
    doubleSum = 0
    for i in range(n):
        doubleSum +=x[i] *x[i]
    return np.sqrt(doubleSum)
```
Last modified 12/2021

---

Routine Name: l1norm

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/952fb981c136355401c3f7b99ae3217904b160eb/software/Task92.py)

Purpose: This routine finds the l-1 norm.

Input: You must input a vector.

Output: This routine the l-1 norm.

Code:
```
def l1norm(x):
    n=len(x)
    sum=0
    for i in range(n):
        sum+= np.abs(x[i])
    return(sum)
```
Last modified 12/2021

---

Routine Name: linfnorm

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/952fb981c136355401c3f7b99ae3217904b160eb/software/Task92.py)

Purpose: This routine finds the l-inf norm.

Input: You must input a vector.

Output: This routine returns the l-inf norm.

Code:
```
def lInfNorm(x):
    return max(x)
```
Last modified 12/2021

---

Routine Name: l2Err

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/952fb981c136355401c3f7b99ae3217904b160eb/software/Task92.py)

Purpose: This routine finds the l-2 error 

Input: You must input two vectors.

Output: This routine returns the l-2 error.

Code:
```
def l2Err(x,y):
    n=len(x)
    sum=0
    for i in range(n):
        diff = x[i]-y[i]
        sum+= diff * diff
    return np.sqrt(sum)
```
Last modified 12/2021

---

Routine Name: l1Err

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/952fb981c136355401c3f7b99ae3217904b160eb/software/Task92.py)

Purpose: This routine returns the l-1 error 

Input: You must input two vectors.

Output: This routine returns the l-1 error.

Code:
```
def l1Err(x,y):
    n=len(x)
    sum = 0
    for i in range(n):
        diff = x[i] - y[i]
        sum+= np.abs(diff)
    return sum
```
Last modified 12/2021

---

Routine Name: linfErr

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/952fb981c136355401c3f7b99ae3217904b160eb/software/Task92.py)

Purpose: This routine finds the l-inf error 

Input: You must input two vectors.

Output: This routine returns the l-inf error..

Code:
```
def lInfErr(x,y):
    z=[]
    for i in range(len(x)):
        z.append(np.abs(x[i]-y[i]))
    return max(z)
```
Last modified 12/2021
