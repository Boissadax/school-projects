from numpy import *
from numpy.linalg import *

A = array([[-8, 4, -2], [-1, 1, -1], [1, 1, 1]])
B = array([-2, 4, 4])

X = dot(inv(A), B)
print(X)
