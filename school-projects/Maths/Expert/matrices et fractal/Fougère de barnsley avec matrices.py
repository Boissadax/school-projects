import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from random import *

nbpoints = 10000
tirageNombre = int
L = np.zeros(shape=(2, nbpoints))

for k in range(nbpoints - 1):
    tirageNombre = randint(1,100)
    if tirageNombre == 1:
        A = array([[0, 0], [0, 0.16]])
        V = array([[0], [0]])
    elif tirageNombre >1 and tirageNombre < 87:
        A = array([[0.85, 0.04], [-0.04, 0.85]])
        V = array([[0], [1.6]])
    elif tirageNombre >= 87 and tirageNombre <= 93:
        A = array([[0.2, -0.26], [0.23, 0.22]])
        V = array([[0], [1.6]])
    else :
        A = array([[-0.15, 0.28], [0.26, 0.24]])
        V = array([[0], [0.44]])

    L2 = np.array([[L[0,k-1]],[L[1,k-1]]])
    P = np.dot(A,L2) + V
    L[:,k]=P[:,0]
for i in range(nbpoints-1):
    plt.plot(L[0,i],L[1,i],",",color='green')
plt.title("Fougère de barnsley", fontsize=14, color='green')
plt.axis('off')
plt.show()
