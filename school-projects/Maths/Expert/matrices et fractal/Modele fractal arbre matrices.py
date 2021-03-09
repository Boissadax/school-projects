import matplotlib.pyplot as plt
import numpy as np
from random import *
from numpy import *

nbpoints = 100000
L = np.zeros(shape=(2, nbpoints))

c = 0.255
r = 0.75
q = 0.625
a = (-pi)/8
w = pi/5

for k in range(nbpoints - 1):
    tirageNombre = randint(0,2)
    if tirageNombre == 0:
        A = array([[0, 0], [0, c]])
        V = array([[0.5], [0]])
    elif tirageNombre == 1:
        A = array([[r*cos(a), -r*sin(a)], [r*sin(a), r*cos(a)]])
        V = array([[0.5-0.5*r*cos(a)], [c-0.5*r*sin(a)]])
    else:
        A = array([[q*cos(w), r*sin(a)], [q*sin(w), r*cos(a)]])
        V = array([[0.5-0.5*q*cos(w)], [0.6*c-0.5*q*sin(w)]])

    L2 = np.array([[L[0,k-1]],[L[1,k-1]]])
    P = np.dot(A,L2) + V
    L[:,k]=P[:,0]
for i in range(nbpoints-1):
    plt.plot(L[0,i],L[1,i],",",color='green')
plt.title("Modèle d'arbre fractal", fontsize=14, color='green')
plt.axis('off')
plt.show()

