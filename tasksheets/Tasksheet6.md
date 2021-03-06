# Task 1

Output for bisection method:

![image](https://user-images.githubusercontent.com/89805209/140004388-80c5c0e0-8def-46e0-b8ce-c16553127b7d.png)

[link to code](https://github.com/SethCorb/math4610/blob/2149fb53709fdae5e3d46aa2625f7cb32a8adfb1/software/Bisection.py)


Output for secant method:

![image](https://user-images.githubusercontent.com/89805209/140004339-4dd07157-8fcf-49cd-878a-8cf5c79b5556.png)

[link to code](https://github.com/SethCorb/math4610/blob/2149fb53709fdae5e3d46aa2625f7cb32a8adfb1/software/secant.py)

Output for fixed point method:

![image](https://user-images.githubusercontent.com/89805209/140004421-1704da56-2c0a-40d1-b505-962d56d2cbd6.png)

[link to code](https://github.com/SethCorb/math4610/blob/2149fb53709fdae5e3d46aa2625f7cb32a8adfb1/software/FixedPoint.py)

Output for Newton's method:

![image](https://user-images.githubusercontent.com/89805209/140004629-c6c89b86-f59f-4a54-8d53-3dd0806aa585.png)

[link to code](https://github.com/SethCorb/math4610/blob/2149fb53709fdae5e3d46aa2625f7cb32a8adfb1/software/netwon.py)


# Task 2

Output for both x=-5 and 6:

![image](https://user-images.githubusercontent.com/89805209/140004796-7b6c85fc-7ab0-4fbf-94ef-1d8367f3acb4.png)

The problem is that our derivative is very close to zero and the computer doesn't like that. I switched my x values to 2 and -1 and these were the results:

x=-1:

![image](https://user-images.githubusercontent.com/89805209/140006083-b46d0900-6aa7-435c-87b2-cb9cb5723c3c.png)

x=2:

![image](https://user-images.githubusercontent.com/89805209/140006099-4ce39786-cb73-4e25-a00f-338d942e1269.png)

This illustrates the idea that it is possible to get the "wrong" zero if you are not careful.


# Task 3

Output for this:

![image](https://user-images.githubusercontent.com/89805209/140006204-9ba94c91-2030-44d4-8a4c-27d4ac7ae47f.png)

Code: [link](https://github.com/SethCorb/math4610/blob/2149fb53709fdae5e3d46aa2625f7cb32a8adfb1/software/hybrid.py)

# Task 4

Output:

![image](https://user-images.githubusercontent.com/89805209/140840136-568b3585-a26d-4359-970f-b088ab236959.png)

[link](https://github.com/SethCorb/math4610/blob/bc91dba9a6f6ed19e8a084513ac3ad9ef8ea4a6f/software/HybridSecant.py)


# Task 5

Output:

![image](https://user-images.githubusercontent.com/89805209/140406582-2fad5669-bdf1-4844-8cbe-59512ac9c363.png)

![image](https://user-images.githubusercontent.com/89805209/140406605-6fc3c5d7-32cf-4cee-95f4-e4ad06dd8dfa.png)

[Link to Code](https://github.com/SethCorb/math4610/blob/e65edf507ee24fc65809d8a87be74c33a8c1ea49/software/Bunch%20of%20Zeroes.py)

# Task 6

There are many methods to find multiple roots. The most common one is to split up an interval into a bunch of sub intervals, and search for zeroes on each of those subintervals. The Durand-Kerner method is another method. The downside with this one is that you need a polynomial to find the roots of. No other function will work. This is very similar to teh Aberth method. Although it can take a lot of time, the most robust method seems to be to chop your interval into smaller intervals

[link](https://en.wikipedia.org/wiki/Root-finding_algorithms)
