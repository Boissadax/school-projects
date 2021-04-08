import numpy as np
from numpy import *

def produit(n):
    A = np.array([[8, 21], [3, 8]])
    X = np.array([[1], [0]])
    L = []
    print(dot(A, X))
    for i in range(1,n):
        L.append(dot(A,X))
        X=dot(A,X)
    print(L)

produit(10)