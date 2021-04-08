import matplotlib.pyplot as plt
from random import *
from numpy import *

x = [0]
y = [0]
c = 0.255
r = 0.75
q = 0.625
a = (-pi)/8
w = pi/5

def points(n):
    for i in range(1,n):
        a = randint(0,2)
        if a == 0:
            x.append(0 * x[i - 1] + 0 * y[i - 1] + 0.5)
            y.append(0 * x[i - 1] + c * y[i - 1])
        elif a == 1:
            x.append(r * cos(a) * x[i - 1] - r * sin(a) * y[i - 1] + (0.5 - 0.5 * r * cos(a)))
            y.append(r * sin(a) * x[i - 1] + r * cos(a) * y[i - 1] + (c - 0.5 * r * sin(a)))
        else:
            x.append(q * cos(w) * x[i - 1] + r * sin(a) * y[i - 1] + (0.5 - 0.5 * q * cos(w)))
            y.append(q * sin(w) * x[i - 1] + r * cos(a) * y[i - 1] + (0.6 * c - 0.5 * q * sin(w)))
    return (x, y)


points(10000)
plt.plot(x, y, ".b")
plt.show()
