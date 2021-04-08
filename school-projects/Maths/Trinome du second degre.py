from math import *
from sympy import *
import sympy as sp
import matplotlib.pyplot as plt
from numpy.linalg.linalg import solve

#inputs
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

#Variables
D = b**2 - 4*a*c
X = []
Y = []
Y2 = []
X2 = []

def racines(): #Calcul des racines
    
    if D > 0: #Delta positif -> 2 racines
        r1 = (-b - sqrt(D)) / 2*a
        r2 = (-b + sqrt(D)) / 2*a
        print("x1 =",r1," ;x2 =",r2)
    
    elif D == 0: #Delta nul -> une racine
        r = b/2*a
        print("x =",r)
    
    elif D < 0: #Delta négatif -> pas de racines
        print("Aucunes racines")

def derive(): #Calcul de la dérivée
    x = sp.Symbol('x')
    f = a*x**2+b*x+c
    f2 = sp.diff(f,x)

    #Affichage
    print("La dérivée de f(x) est :",f2)
    return(f2)

def courbe(a1,b1): #Fonction de création de la courbe de f et f'
    #Calculer coordonnées fonction
    for i in range(a1,b1):
        X.append(i)
        Y.append(a*i**2+b*i+c)

    #Calculer coordonnées dérivée
    for k in range(a1,b1-1):
        X2.append((X[k] + X[k+1]) / 2)
        Y2.append((Y[k+1] - Y[k]) / 1)

    #Configuration graphique
    plt.plot(X,Y)
    plt.plot(X2,Y2)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(color="gray",linestyle='-')
    plt.show()

def main(): #Fonction principale
    racines()
    derive()
    courbe(-10,10)

main()