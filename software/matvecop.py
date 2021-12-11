import numpy as np

def vector_addition(v1, v2):
    n = len(v1)
    x = [0 for j in range(n)]
    for i in range(n):
        x[i] = v1[i] + v2[i]
    return x

def vector_subtraction(v1, v2):
    n = len(v1)
    x = [0 for j in range(n)]
    for i in range(n):
        x[i] = v1[i] - v2[i]
    return x

def scalar_mult(c, v1):
    n = len(v1)
    x = [0 for j in range(n)]
    for i in range(n):
        x[i] = c * v1[i]
    return x

def dot_product(v1, v2):
    x = 0
    for i in range(len(v1)):
        x += v1[i] * v2[i]
    return x

def outer_product(v1, v2):
    m = len(v1)
    n = len(v2)
    result = np.empty((m, n))
    for i in range(m):
        for j in range(n):
            result[i, j] = v1[i] * v2[j]
    return result



def matrix_addition(m1, m2):
    result = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return result

def matrix_subtraction(m1, m2):
    result = [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return result

def matrix_scaler_multiplication(c, m1):
    result = [[m1[i][j] * c for j in range(len(m1[0]))] for i in range(len(m1))]
    return result

def matrix_transpose(m):
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return result

def matrix_vector_multiplication(m, v):
    return [np.dot(row, v) for row in m]

def matrix_multiplication(m1, m2):
    result = np.eye(len(m1), dtype=np.double)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i, j] += m1[i][k] * m2[k][j]
    return result
