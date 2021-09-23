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
c  import numpy as np
Imports numpy to use the absolute value function
c  def main():
c      x=1
c      eps=.5
Set x=1 and our initial epsilon as .5
c      for i in range(100):
c          xapp = x+eps
c          err = np.abs(x-xapp)
Finds the difference between x and our approximation
c          if err==0:
c              print("done")
c              break
If the computer finds x to be the same as our approximation, it ends the program.
c          print("i:",i,"error:",err)
Print what step we are on, and what the difference between x and our approximation is.
c          eps=eps/2
Divide epsilon by two to try again.
c  main()
```
Last modified 9/2021
