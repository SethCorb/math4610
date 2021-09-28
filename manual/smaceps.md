Routine Name: smaceps

Author: Seth Corbridge

Language: Python

Link to file: [link](https://github.com/SethCorb/math4610/blob/46a380677a52ce87d4617387b39acd7e1b416ec4/software/smaceps.py)

Purpose: This routine will compute the single precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

Input: There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

Output: This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

Code:
```
import numpy as np
c import numpy
def main():
    macheps = np.finfo(np.float32).eps
c find the single precision
    print(macheps)
c print the precision
main()
c call main.
```
Last modified 9/2021
