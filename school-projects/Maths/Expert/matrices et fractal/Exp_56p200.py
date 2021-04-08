from numpy import *
from numpy.linalg import *
def puissance(a,b,c,d,n):
    A=array([[a,b],[c,d]])
    C=A
    for i in range(1,n):
        A=dot(A,C)
    print(A)
    return(A)

puissance(0.6, 0.4, 0.2, 0.8, 10)