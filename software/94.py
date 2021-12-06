import Task92
import LUDecomp

def jacobi(A,b,x,tol,maxiter):
    n=len(b)
    error = 10 * tol
    iter=0
    r = [1 for i in range(n)]
    while error > tol and iter < maxiter:
        for i in range(n):
            r[i] = b[i]
            for j in range(n):
                r[i] = r[i] - A[i][j]*x[j]
        x1 = [1 for i in range(n)]
        for i in range(n):
            x1[i] = x[i] - r[i]/A[i][i]
        error = Task92.l2Err(x,x1)
        iter += 1
        for i in range(n):
            x[i]=x1[i]
    return x1

print(jacobi(LUDecomp.hilbertMatrix(3),[1,1,1],[0,0,0],.1,1000))
