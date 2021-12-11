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

---

Routine Name: vector_subtraction

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the difference of two vectors.

Input: The two inputs are two vectors of the same length.

Output: This routine returns you the differ4ence of the two vectors.

Code:
```
def vector_subtraction(v1, v2):
    n = len(v1)
    x = [0 for j in range(n)]
    for i in range(n):
        x[i] = v1[i] - v2[i]
    return x
```
Last modified 12/2021

---
Routine Name: scalar_mult

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the scalar multip of a vector.

Input: The two inputs are a vector and a scalar.

Output: This routine returns a scaled vector.

Code:
```
def scalar_mult(c, v1):
    n = len(v1)
    x = [0 for j in range(n)]
    for i in range(n):
        x[i] = c * v1[i]
    return x
```
Last modified 12/2021

---

Routine Name: dot_product

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the dot product of two vectors.

Input: The two inputs are two vectors of the same length.

Output: This routine returns you dot product.

Code:
```
def dot_product(v1, v2):
    x = 0
    for i in range(len(v1)):
        x += v1[i] * v2[i]
    return x
```
Last modified 12/2021

---

Routine Name: outer_product

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the outer product of two vectors.

Input: The two inputs are two vectors of the same length.

Output: This routine returns you cross product vector.

Code:
```
def outer_product(v1, v2):
    m = len(v1)
    n = len(v2)
    result = np.empty((m, n))
    for i in range(m):
        for j in range(n):
            result[i, j] = v1[i] * v2[j]
    return result
```
Last modified 12/2021

---



