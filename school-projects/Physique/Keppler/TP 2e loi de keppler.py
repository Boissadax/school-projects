import numpy as np
import matplotlib.pyplot as plt
t = [0,2,4,6,8,10,12]
x = [0.0175,-0.017,-0.0513,-0.0857,-0.1199,-0.154,-0.1879]
y = [0.9998,0.9999,0.9987,0.9963,0.9928,0.9881,0.9822]
plt.xlabel('Coordonnees x')
plt.ylabel('Coordonnees y')
plt.title('Trajectoire de la Terre')
plt.scatter(x, y, marker = '+')
i = 1

while i < len(t)-1 :
	alpha = np.arctan(x[i]/y[i]) - np.arctan(x[i+1]/y[i+1])
	SC = np.sqrt(x[i]**2+y[i]**2)
	SB = np.sqrt(x[i+1]**2+y[i+1]**2)
	Aire = ((SB*SC*np.sin(alpha))/2)
	plt.fill([x[i+1], x[i], 0], [y[i+1], y[i], 0], label='Aire = ' + "%.2e"%Aire + ' u.a.**2')
	i += 2

plt.legend(loc='center left')
plt.savefig("Modélisation 2nd loi de Keppler.png")
plt.show()
