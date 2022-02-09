# Important packages to import
import numpy as np
import matplotlib.pyplot as pt
from tabulate import tabulate
# set our x value
x=2
# define our h values and initialize the empty lists we need.
h = [.1, .05, .01, .005, .001]
dp = []
dm = []
dz = []
dt = []
# define the true value of u'(2) where u=sin(x)
real = np.cos(2)

# for each h value, add the appropriate estimate error to the list
for i in h:
    dp.append(np.abs((np.sin(x+i)-np.sin(x))/i-real))
    dm.append(np.abs((np.sin(x)-np.sin(x-i))/i-real))
    dz.append(np.abs((np.sin(x+i)-np.sin(x-i))/(2*i)-real))
    dt.append(np.abs((2*np.sin(x+i)+3*np.sin(x)-6*np.sin(x-i)+np.sin(x-2*i))/(6*i)-real))

# Plot the h list against the errors of each method.
pt.loglog(h,dp,h,dm,h,dz,h,dt)
pt.show()
# Insert labels to make our table look nice.
h.insert(0,"h")
dp.insert(0,"D-plus")
dm.insert(0,"D-minus")
dz.insert(0,"D-zero")
dt.insert(0,"D-three")
# Define and display our table.
table = [h, dp, dm, dz, dt]
print(tabulate(table,tablefmt= "fancy_grid"))
