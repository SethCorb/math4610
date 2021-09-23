import numpy as np
def main():
    x=1
    eps=.5
    for i in range(1000):
        xapp = x+eps
        err = np.abs(x-xapp)
        if err==0:
            print("done")
            break
        print("i:",i,"error:",err)
        eps=eps/2
main()
