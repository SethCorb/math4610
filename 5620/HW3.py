import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
A = np.zeros((51,51))
A[0][0]=1
A[50][50]=1
unifgrid = []
m = 49
for i in range(m+2):
    unifgrid.append(1/(m+1)*i)
weirdgrid = []
for i in unifgrid:
    weirdgrid.append(i**2)
diff = []
for i in range(len(weirdgrid)-1):
    diff.append(weirdgrid[i+1]-weirdgrid[i])
for i in range(len(diff)-2):
    A[i+1][i]=2/(diff[i]*(diff[i]+diff[i+1]))
    A[i+1][i+1]=-2/(diff[i+1]*diff[i+2])
    A[i+1][i+2]=2/(diff[i+2]*(diff[i+2]+diff[i+3]))
    print(i)
print(A)

F = np.zeros((51,1))
F[0]=2
F[50]=3
sol = linalg.solve(A,F)
plt.plot(weirdgrid,linalg.solve(A,F))
plt.show()
real = "-np.sin(x)+2*x-.1585"
rl = [0 for i in range(11)]
for i in range(11):
    x= i*.1
    rl[i] = np.abs(eval(real) - sol[i][0])
x = [(i-1)*.1 for i in range(1,12)]
#plt.plot(x,rl)
#plt.show()