import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)
A = np.zeros((50,50))
A[0][0]=1
A[49][49]=1
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
length = len(diff) -1
for i in range(len(diff)-3):
    A[i+1][i]=2/(diff[i]*(diff[i]+diff[i+1]))
    A[i+1][i+1]=-2/(diff[i+1]*diff[i+2])
    A[i+1][i+2]=2/(diff[i+2]*(diff[i+2]+diff[i+3]))
A[49-1][48-1]=2/(diff[length-3]*(diff[length-3]+diff[length-2]))
A[49-1][49-1]=-2/(diff[length-2]*diff[length-1])
A[49-1][50-1]=2/(diff[length-1]*(diff[length-1]+diff[length]))
print(A)

F = np.zeros((50,1))
F[0]=2
F[49]=3
print(F)
sol = linalg.solve(A,F)
plt.plot(weirdgrid[0:-1],linalg.solve(A,F))
plt.show()
real = "2*np.cos(x)+2.281*np.sin(x)"
rl = [0 for i in range(11)]
for i in range(11):
    x= i*.1
    rl[i] = np.abs(eval(real) - sol[i][0])
x = [(i-1)*.1 for i in range(1,12)]
plt.plot(x,rl)
plt.show()