    # Import needed packages
import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from math import e
def main():
    # Define our matrix A
    A = np.zeros((11,11))
    A[0][0]=-.1
    A[0][1]=.1
    for i in range(9):
        A[i+1][i]=1
        A[i+1][i+1]=-2
        A[i+1][i+2]=1
    A[10][10]=.01
    A=A/.01

    # Define our vector F
    F = np.zeros((11,1))
    F[0]=1
    F[10]=e
    for i in range(1,10):
        F[i] = 2*np.exp(i*.1)
    sol = linalg.solve(A,F)

    # Define x vector
    x = [(i-1)*.1 for i in range(1,12)]

    # plot the solution
    plt.plot(x,linalg.solve(A,F))
    plt.show()

    # Define real solution to determine error
    real = "np.exp(x)"
    # Create rl as place holder for error
    rl = [0 for i in range(11)]
    for i in range(11):
        x= i*.1
        rl[i] = np.abs(eval(real) - sol[i][0])
    sum = 0

    # Find the 2-norm
    for i in rl:
        sum += i**2
    newsum = np.sqrt(sum*.1)
    x = [(i-1)*.1 for i in range(1,12)]
    # Plot error and print 2-norm
    print("2-norm:", newsum)
    plt.plot(x,rl)
    plt.show()

def alt():
    # Define our matrix A
    A = np.zeros((11,11))
    A[0][0]=-.1
    A[0][1]=.1
    for i in range(9):
        A[i+1][i]=np.exp((i+1/2)*.1)
        A[i+1][i+1]=-np.exp((i+1/2)*.1)-np.exp((i+3/2)*.1)
        A[i+1][i+2]=np.exp((i+3/2)*.1)
    A[10][10]=.01
    A=A/.01
    # Define our vector F
    F = np.zeros((11,1))
    F[0]=1+.1
    F[10]=e
    for i in range(1,10):
        F[i] = 2*np.exp(2*i*.1)
    sol = linalg.solve(A,F)
    # Define x vector
    x = [(i-1)*.1 for i in range(1,12)]

    # plot the solution
    plt.title("Solution")
    plt.plot(x,linalg.solve(A,F))
    plt.show()

    # Define real solution to determine error
    real = "np.exp(x)"
    # Create rl as place holder for error
    rl = [0 for i in range(11)]
    for i in range(11):
        x= i*.1
        rl[i] = np.abs(eval(real) - sol[i][0])
    sum = 0

    x = [(i-1)*.1 for i in range(1,12)]
    # Plot error and Flux
    plt.title("Error")
    plt.plot(x,rl)
    plt.show()

    up = []
    J = []
    x = [(i+1)*.1 for i in range(1,10)]
    for i in range(len(sol)-2):
        up.append((sol[i+2][0]-sol[i][0])*5)
    for i in range(len(up)):
        J.append(-np.exp((i+2)*.1)*up[i])
    plt.title("Flux")
    plt.plot(x,J)
    plt.show()

alt()