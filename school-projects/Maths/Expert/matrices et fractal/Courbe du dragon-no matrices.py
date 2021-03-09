import matplotlib.pyplot as plt
from random import *

x = [0]
y = [0]


def points(n):
    for i in range(1, n):
        a = randint(0, 1)
        if a == 0:
            x.append(.5 * x[i - 1] - 0.5 * y[i - 1])
            y.append(0.5 * x[i - 1] + 0.5 * y[i - 1])
        else:
            x.append(-0.5 * x[i - 1] - 0.5 * y[i - 1] + 1)
            y.append(0.5 * x[i - 1] - 0.5 * y[i - 1])
    return (x, y)


points(10000)
plt.plot(x, y, ".b")
plt.show()