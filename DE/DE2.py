import numpy as np
G = [0 for i in range(10)]
x = [0 for i in range(10)]
for i in range(len(G)):
    G[i] = 1/h**2 *(u[i-1]-2*u[i]+u[i+1])-np.sin(i)
G[0] = 1/h**2 *(-2*u[i]+u[i+1])-np.sin(i)