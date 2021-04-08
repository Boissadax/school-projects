import time

#Variables
L = [i for i in range(1,101)]
A = []
B = [2,3,5]

#Fonctions
def ce(a):
    for i in range(a):
        if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
            B.append(i)
    B.sort()
    return(B)

#main function
def main():
    select_Ce = input("Souhaitez vous faire le criblage d'Eratosthène ? (O/n) :")
    if select_Ce == "O":
        a = int(input("Entrez le nombre de nombres à tester avec méthode d'Ératosthène :"))
        tps1 = time.time()
        ce(a)
        tps2 = time.time()
        print("Le crible d'ératosthène en testant de 1 à",a," est : ",B)
        print("Le nombre de nombres premiers pour cette intervalle est :",len(B))
        print("le temps d'exécution est :",tps2 - tps1)
    else:
        print("Vous n'avez pas souhaité procéder au criblage")

#On appelle la fonction main
main()

#Le programme met 0.00004s (50 microsecondes) pour tester de 0 à 100
#Le programme met 0.006s pour 10 000 nombres
