import matplotlib.pyplot as plt
from random import *

x = [0]
y = [0]


def points(n):
    for i in range(1, n):
        a = randint(1, 100)
        if a == 1:
            x.append(0 * x[i - 1] + 0 * y[i - 1])
            y.append(0 * x[i - 1] + 0.16 * y[i - 1])
        elif a > 1 and a < 87:
            x.append(0.85 * x[i - 1] + 0.04 * y[i - 1])
            y.append(-0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6)
        elif a >= 87 and a <= 93:
            x.append(0.2 * x[i - 1] - 0.26 * y[i - 1])
            y.append(0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6)
        else:
            x.append(-0.15 * x[i - 1] + 0.28 * y[i - 1])
            y.append(0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44)
    return (x, y)


points(100000)
plt.plot(x, y, "!")
plt.show()
