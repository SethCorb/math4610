from matplotlib import pyplot as plt
import numpy as np
xmin = eval(input("Enter x min"))
xmax = eval(input("Enter X max"))
num = eval(input("Enter the number of values you want"))
while True:
    xpt = []
    ypt = []
    expression = input('Enter expression:\n')
    chanx = (xmax - xmin) / num
    for i in range(num):
        x = xmin + i * chanx
        xpt.append(x)
        ypt.append(eval(expression))
        i += 1
    f = input("Continue?Y/N")
    plt.plot(xpt, ypt, label=expression)
    if f == "N":
        break
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()