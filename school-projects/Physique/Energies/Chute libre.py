import matplotlib.pyplot as plt
from math import *

x=[0,0.075,0.15,0.225,0.300,0.375,0.45,0.525,0.600,0.6750,0.75,0.8250,0.900,0.9750,1.050,1.125,1.200,1.275,1.350,1.425,1.500]
y=[0,0.14,0.2630,0.3750,0.4730,0.5520,0.6130,0.6610,0.6950,0.7110,0.7110,0.6950,0.6610,0.6160,0.5520,0.4730,0.3750,0.2630,0.1340,-0.0140,-0.1650]
t=[]
m = 0.08
g = 9.81

for i in range(20):
    t.append(i)

#Définition de l'intervalle de temps entre deux images
dt = 1/25

# Création de 2 tableaux pouvant accueillir les valeurs des vitesses aux divers points
# Initialisation des tableaux avec des valeurs nulles. Les calculs seront fait par la suite
Vx =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Vy =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
V =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Calcule les coordonnées de v
for i in range(20) :
    Vx[i]=((x[i+1]-x[i])/dt)
    Vy[i]=((y[i+1]-y[i])/dt)
    V[i]=(sqrt(Vx[i]**2+Vy[i]**2))

#Calcule de Ec
Ec = []
for i in range(20):
    Ec = Ec + [(m/2)*V[i]**2]

#Calcul de Ep
Ep = []
for i in range(20):
    Ep = Ep + [m*g*y[i]]

#Calcul de Em
Em=[]
for i in range(20):
    Em = Em + [Ep[i]+Ec[i]]

#Donner les listes des energies
print(Ec)
print(Ep)
print(Em)
#trace les points
plt.scatter(t,Ec,label='Énergie cinétique de pesanteur')
plt.scatter(t,Ep,label='Énergie potentielle de pesanteur')
plt.scatter(t,Em,label='Énergie mécanique de pesanteur')

#Légendes
plt.title('Energies du système dans le temps', fontsize =16)  # titre du graphique
plt.xlabel('$t$ (s)', fontsize =16)
plt.ylabel(r'$\mathcal{E}$ (J)', fontsize =16)
plt.tick_params(labelsize=16)

plt.legend(loc=0)
plt.subplots_adjust(hspace=0.5)

#Reglages
plt.axis([0, 20, 0, 1])       # définition des axes [xmin, xmax, ymin, ymax]
plt.grid(True)                                    # afficher une grille
plt.savefig("Energies du système dans le temps.png")
plt.show()                                        # afficher le graphique
