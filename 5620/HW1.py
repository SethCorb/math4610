import numpy as np
import matplotlib.pyplot as pt

u = "np.sin(x)"
x=2
h = [.1, .05, .01, .005, .001]
dp = []
dm = []
dz = []
dt = []
real = np.sin(2)

for i in h:
    dp.append(np.abs((np.sin(x+i)-np.sin(x))/i-real))
    dm.append(np.abs((np.sin(x)-np.sin(x-i))/i-real))
    dz.append(np.abs((np.sin(x+i)-np.sin(x-i))/(2*i)-real))
    dt.append(np.abs((2*np.sin(x+i)+3*np.sin(x)-6*np.sin(x-i)+np.sin(x-2*i))/(6*i)-real))

pt.loglog(h,dp,h,dm,h,dz,h,dt)
pt.show()