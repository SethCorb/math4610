Routine Name: matrix_addition

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the sum of two matrices.

Input: You must input two matrices of the same size.

Output: This routine returns you the sum matrix.

Code:
```
def matrix_addition(m1, m2):
    result = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return result
```
Last modified 12/2021

---

Routine Name: matrix_subtraction

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the difference of two matrices.

Input: You must input two matrices of the same size.

Output: This routine returns you the difference matrix.

Code:
```
def matrix_subtraction(m1, m2):
    result = [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return result
```
Last modified 12/2021

---

Routine Name: matrix_scalar_multiplication

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the scalaar multiple of a matrix.

Input: You must input one matrix and a scalar.

Output: This routine returns you the scaled matrix.

Code:
```
def matrix_scaler_multiplication(c, m1):
    result = [[m1[i][j] * c for j in range(len(m1[0]))] for i in range(len(m1))]
    return result
```
Last modified 12/2021

---

Routine Name: matrix_transpose

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the transpose of a matrix.

Input: You must input one matrix.

Output: This routine returns you transpose of the matrix.

Code:
```
def matrix_transpose(m):
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return result
```
Last modified 12/2021

---

Routine Name: matrix_vector_multiplication

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the product of a matrix and a vector.

Input: You must input a matrix and a vector.

Output: This routine returns you the product vector .

Code:
```
def matrix_vector_multiplication(m, v):
    return [np.dot(row, v) for row in m]
```
Last modified 12/2021

---

Routine Name: matrix_multiplication

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/9682f574bf3247ed5e3c9609ecdcf4031f47aad2/software/matvecop.py)

Purpose: This routine will give you the product of two matrices.

Input: You must input two matrices of compatible sizes.

Output: This routine returns you the product matrix.

Code:
```
def matrix_multiplication(m1, m2):
    result = np.eye(len(m1), dtype=np.double)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i, j] += m1[i][k] * m2[k][j]
    return result
```
Last modified 12/2021

---
