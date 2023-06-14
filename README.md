# Least-Squares Rigid Motion Using SVD

This repo summarizes the steps to computing the best-fitting rigid transformation that aligns
two sets of corresponding points.

A rigid transformation is composed of 2 terms, a rotation matrix R and a translation vector t. 

In the beggining we can see the same body (torus) but in a different location , (blue & red). 
In the second phase we calculate R & t from the red body to the blue on and plot it in yellow. 

We can see that the error between the oroginal blue body and the artificial yellow one tends to zero. 


![](https://github.com/Raviv-Herrera/Rigid-Body-Transformation/blob/main/example.gif)


### References
[1] Least-Squares Rigid Motion Using SVD, Olga Sorkine-Hornung and Michael Rabinovich, Department of Computer Science, ETH Zurich, January 16, 2017
