import matplotlib.pyplot as plt
from math import *
import numpy as np

#Listes du pointage
x=[0,0.02,0.05,0.1,0.18,0.28,0.40,0.54,0.70,0.88,1.09,1.32]
y=[0.40,0.395,0.38,0.37,0.325,0.32,0.295,0.26,0.22,0.16,0.12,0.06]
t=[]
#Ajouter les valeurs du temps a la liste t
for i in range(11):
    t.append(i/10)

#Variables
m = 0.22
g = 9.81
alpha = 15
#Définition de l'intervalle de temps entre deux images
dt = 0.1

#Distance AB
AB = sqrt(x[11]**2+(y[0]-y[11])**2)

#Calcul du Poids
P=m*g

# Création de 2 tableaux pouvant accueillir les valeurs des vitesses aux divers points
# Initialisation des tableaux avec des valeurs nulles. Les calculs seront fait par la suite
Vx =[0,0,0,0,0,0,0,0,0,0,0,0]
Vy =[0,0,0,0,0,0,0,0,0,0,0,0]
V =[0,0,0,0,0,0,0,0,0,0,0,0]

#Calcule les coordonnées de V et de V
for i in range(11) :
    Vx[i]=((x[i+1]-x[i])/(dt))
    Vy[i]=((y[i+1]-y[i])/(dt))
    V[i]=(np.sqrt(Vx[i]**2+Vy[i]**2))

#Calcule de Ec
Ec = []
for i in range(11):
    Ec.append((m/2)*V[i]**2)
#Calcul de Ep
Ep = []
for i in range(11):
    Ep.append(m*g*y[i])
#Calcul de Em
Em=[]
for i in range(11):
    Em.append(Ep[i]+Ec[i])

#Calcul delta ou travail de la force dse frottement
DEm = Em[9]-Em[0]

#Donner les listes des energies
#print("Vx:",Vx)
#print("Vy:",Vy)
#print("Ec:",Ec)
#print(Ep)
#print(Em)
print("La distance parcourue est :",AB*100,"cm. Soit :",AB,"m")
print("La valeur du travail de la force de frottement f est Delta Em car la seule force non conservative ici est le frottement f.")
print("Donc:","W_A->B(f) = Delta Em")
print("Soit: W_A->B(f) = ", DEm,"J")


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
plt.axis([0, 1, 0, 2])       # définition des axes [xmin, xmax, ymin, ymax]
plt.grid(True)                                    # afficher une grille
plt.show()                                        # afficher le graphique
