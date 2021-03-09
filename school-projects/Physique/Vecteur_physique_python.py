import matplotlib.pyplot as plt

#point souhaité
numero_point=int(input("rentrez le point souhaité :"))

# Liste contenant les abscisses des points
x=[0,0.075,0.15,0.225,0.300,0.375,0.45,0.525,0.600,0.6750,0.75,0.8250,0.900,0.9750,1.050,1.125,1.200,1.275,1.350,1.425,1.500]
# Liste contenant les ordonnées des points
y=[0,0.14,0.2630,0.3750,0.4730,0.5520,0.6130,0.6610,0.6950,0.7110,0.7110,0.6950,0.6610,0.6160,0.5520,0.4730,0.3750,0.2630,0.1340,-0.0140,-0.1650]

# Définition de l'intervalle de temps entre deux images
dt = 1 / 25

# Initialisation des tableaux avec des valeurs nulles. Les calculs seront fait par la suite
Vx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Vy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ax = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ay = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Calculer les coordonnées de v a un certain point
Vx[numero_point] = ((x[numero_point+1] - x[numero_point]) / dt)
Vy[numero_point] = ((y[numero_point+1] - y[numero_point]) / dt)

#Définir l'échelle
echelle=20
echelle_acc=2

def afficher_un_vecteur(numero_point):
    #Vecteur vitesse
    plt.arrow(x[numero_point],y[numero_point],Vx[numero_point]/echelle,Vy[numero_point]/echelle,head_width=0.04, length_includes_head=True,color="blue")
    # Affiche le nom des vecteurs
    plt.text(x[numero_point] + 0.05, y[numero_point], r"$\vec{v}$" + str(numero_point + 1), color="blue")

def afficher_tous_vecteurs():
    for i in range(0,20,4):
        Vx[i] = ((x[i + 1] - x[i]) / dt)
        Vy[i] = ((y[i + 1] - y[i]) / dt)
        # Vecteur vitesse
        plt.arrow(x[i], y[i], Vx[i] / echelle, Vy[i] / echelle,head_width=0.04, length_includes_head=True, color="blue")

        # Affiche le nom des vecteurs
        plt.text(x[i] + 0.05, y[i], r"$\vec{v}$" + str(i + 1), color="blue")

    for i in range(0,20,4):
        ax[i]=((((x[i + 2] - x[i+1]) / dt))-((x[i + 1] - x[i]) / dt))
        ay[i]=((((y[i + 2] - y[i+1]) / dt))-((y[i + 1] - y[i]) / dt))
        # Vecteur acceleration
        plt.arrow(x[i], y[i], ax[i] / echelle_acc, ay[i] / echelle_acc, head_width=0.04, length_includes_head=True,color="green")

        print("Au point ",i," la valeur de l'acclélération est : ",ay[i]*2 ,"m/s")



afficher_tous_vecteurs()

# Affiche l'échelle
plt.text(0.2, -0.5, "Echelle 1 cm $\leftrightarrow$ 20 cm/s", color="blue")

plt.scatter(x, y, marker='o', color='r')  # place les points

plt.title('Positions successives d\'un système')  # titre du graphique
plt.xlabel('x (en m)')  # légende axe X
plt.ylabel('y (en m)')  # légende axe Y
plt.axis([0, 1.6, -1, 1])  # axe à adapter au besoin
plt.grid(True)  # afficher une grille
plt.show()  # afficher le graphique
