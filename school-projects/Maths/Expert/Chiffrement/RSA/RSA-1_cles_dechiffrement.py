"""Programme permettant de creer clé public et privées OU de dechiffrer (programme Alice)"""
import random
from random import *
from math import *
from time import *

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def pgcd(a,b): #Calcul le PGCD de a et b
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

def gen_c(N): #Renvoie la clé c en fonction de p, q, n, N
    c = randint(1,N)
    for i in range(1,N):
        while pgcd(c,N)!=1:
            c = randint(1,N)
        break
    return c

def inv(a,b): #Trouve de l'inverse d de a modulo b
    for i in range(b): 
        if (i*a)%b == 1:
            return i

def puissance(a,n): #Calcul éfficacement a exposant n
    if n == 0:
        return 1
    elif n%2 == 0:
        return puissance(a*a,n//2)
    else :
        return a * puissance(a,n-1)

def convertToLetters(L): #Rang de lettre -> Lettre
    X=[ alphabet[k]  for i in range(0,len(L)) for k in range(0,len(alphabet)) if L[i] == k]
    return X

def joinLetter(s): #Liste de caractères -> chaine de caractères
    str1 = ""
    return str1.join(s)

def dechiffrementRSA(C,N,n,c): #Déchiffre une liste C chiffré par RSA grâce à la clé privée N et à c
    d = inv(c,N)
    print("d=",d)
    B = [(puissance(C[i],d)%n) for i in range(len(C))]
    B = convertToLetters(B)
    B = joinLetter(B)
    return B

def main():
    select1 = input("Souhaitez vous generer les clés publiques et privées ? 0/n:")
    if select1 == "O":
        p = int(input("Entrez p:"))
        q = int(input("Entrez q:"))
        n=p*q
        N=(p-1)*(q-1)
        print("Votre clé publique (n,c) est : (",n,",",gen_c(N),")")
        print("Votre clé privée N est :",N)
    else:
        select2 = input("Souhaitez vous déchiffrer un message RSA à l'aide de votre clé privée et publique ? O/n:")
        if select2 == "O":
            C = [int(item) for item in input("Entrez la liste chiffrée (espace entre chaque nombre) : ").split()]
            p = int(input("Entrez privé p :"))
            q = int(input("Entrez privé q :"))
            c = int(input("Entrez c publique :"))
            t=time()
            n=p*q
            N=(p-1)*(q-1)
            print("Le message déchiffré est :",dechiffrementRSA(C,N,n,c))
            print("Temps d'éxécution :",time()-t)
main()

