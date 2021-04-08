import matplotlib.pyplot as plt
import numpy as np
pKAH2=float(input('pKA du couple AH / A-  ?'))
pKA=float(input('pKA du couple AH2 / AH  ?'))

pH = np.linspace(0,14,1000)

pAH2 = [100/(1+10**(pKAH2-i))for i in pH]
pA = [100/(1+10**(pKA-i))for i in pH]

pAH =[(100-100/(1+10**(pKAH2-i)))-100/(1+10**(pKA-i)) for i in pH]
print(pAH)

plt.title('Diagramme de distribution d\'un couple HA/A-')
plt.xlabel('pH')
plt.ylabel('%')
plt.axis(xmin=0,xmax=14,ymin=0, ymax=100)
plt.xticks(range(15))
plt.yticks(range(0,110,10))
plt.grid(linestyle="-.")
plt.plot(pH, pAH, color='r', label='% en AH' )
plt.plot(pH, pAH2, color='b',label='% en AH2' )
plt.plot(pH, pA, color='b',label='% en A-' )
plt.show()