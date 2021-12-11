Routine Name: vector_addition

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This will find the sum of two vectors

Input: The two inputs two vectors of the same length.

Output: This routine returns you the sum of the vectors.

Code:
```
def vector_addition(v1, v2):
    n = len(v1)
    x = [0 for j in range(n)]
    for i in range(n):
        x[i] = v1[i] + v2[i]
    return x
```
Last modified 12/2021
