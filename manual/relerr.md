Routine Name: relerr

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/64ffb6b3c6f621820d0c9aaa6d97f79fa1e7f85e/software/relerr.py)

Purpose: This routine will give you the relative error given an a number and an approximation.

Input: The two inputs are the approximation and the actual number.

Output: This routine returns you the relative error.

Code:
```
import numpy as np
c import numpy
def main(x,xapp):
    return np.abs(x-xapp)/np.abs(x)
c calculate the relative error and return it
main()
```
Last modified 9/2021
