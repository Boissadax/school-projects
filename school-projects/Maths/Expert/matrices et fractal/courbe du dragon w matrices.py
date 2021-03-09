import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from random import *

nbpoints = 10000
tirageNombre = int
L = np.zeros(shape=(2, nbpoints))

for k in range(nbpoints - 1):
    tirageNombre = randint(0, 1)
    if tirageNombre == 0:
        A = array([[0.5, -0.5], [0.5, 0.5]])
        V = array([[0], [0]])
    else:
        A = array([[-0.5, -0.5], [0.5, -0.5]])
        V = array([[1], [0]])
    L2 = np.array([[L[0,k-1]],[L[1,k-1]]])
    P = np.dot(A,L2) + V
    L[:,k]=P[:,0]
for i in range(nbpoints-1):
    plt.plot(L[0,i],L[1,i],",",color='red')
plt.title("Courbe du dragon", fontsize=14, color='red')
plt.axis('off')
plt.show()
