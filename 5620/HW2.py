import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
A = np.zeros((11,11))
A[0][0]=-.1
A[0][1]=.1
for i in range(9):
    A[i+1][i]=1
    A[i+1][i+1]=-2
    A[i+1][i+2]=1
A[10][10]=.01
A=A/.01

F = np.zeros((11,1))
F[0]=1
F[10]=1
for i in range(1,10):
    F[i] = np.sin(i*.1)
sol = linalg.solve(A,F)
x = [i*.1 for i in range(1,12)]

plt.plot(x,linalg.solve(A,F))
plt.show()
real = "-np.sin(x)+2*x-.1585"
rl = [0 for i in range(11)]
for i in range(11):
    x= i*.1
    rl[i] = np.abs(eval(real) - sol[i][0])
sum = 0
for i in rl:
    sum += i**2
newsum = np.sqrt(sum)
x = [i*.1 for i in range(1,12)]
print("2-norm:", newsum)
plt.plot(x,rl)
plt.show()