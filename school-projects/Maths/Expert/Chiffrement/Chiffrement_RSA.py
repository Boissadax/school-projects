""" C'est un première version du cryptage par RSA

Penser à ajouter :
- Corriger erreur dechiffrement
- Chiffrement de bloc de 3 lettres pour + de sécurité
- Amélioreation du Main()
"""
"""Début programme"""
import random
from random import *
from math import *
from time import *


alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def convertToList(string):
    list1=[]
    list1[:0]=string
    return(list1)

def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

def cle(p,q,n,N):
    c = randint(1,n)
    for i in range(1,n):
        if pgcd(c,n)!=1:
            c = randint(1,n)
    return(c)

def chiffrement(mot_convert,c):
    L = []
    Y = []
    for i in range(len(mot_convert)):
        for k in range(len(alphabet)):
            if mot_convert[i] == alphabet[k]:
                L.append(k)
    print("Le rang des lettres du mot à crypter est:",L)
    print()
    for i in range(len(L)):
        Y.append((L[i]**c)%253)
    #print("crypté:",Y)
    return Y

def find_inverse(c,n):
    inv = 0
    for i in range(n): 
        if (i*c)%n == 1:
            inv = i
            break
    #print("linverse de",c,"modulo",n,"est:",inv)
    return(inv)

def dechiffrement(Y,inv,N,c):
    X2=[]
    cd = inv

    for i in range(len(Y)):
        Ypcd = puissance(Y[i],cd)
        X2.append((Ypcd%N)) 
        """Erreur à cet endroit : peut etre penser à enlever le *c ou le %26. 
        """
    return(X2)

def puissance(a,n):
    if n == 0:
        return a
    elif n%2 == 0:
        return puissance(a,(n//2))**2
    else :
        return a * puissance(a,n//2)

def convert_to_letter(rankToCode):
    X_dechiffre = []
    for i in range(len(rankToCode)):
        for k in range(len(alphabet)):
            if rankToCode[i] == k:
                X_dechiffre.append(alphabet[k])
    return X_dechiffre

def joinLetter(s):
    str1 = ""
    return(str1.join(s))

"""Insertion des variables"""
p = int(input("Entrez p:"))
q = int(input("Entrez q:"))
while pgcd(p,q) != 1:
    print("p et q ne sont pas premiers entre eux, entrez les à nouveau:")
    p = int(input("Entrez p:"))
    q = int(input("Entrez q:"))
N = p*q
n = (p-1)*(q-1)
c = cle(p,q,n,N) #Génération clé
mot = input("Entrez le mot a convertir:")

def Main():
    

    """Chiffrement"""
    def RSA():
        mot_convert = convertToList(mot) #Conversion string -> list
        print()
        #print("Le mot à déchiffrer est :",mot_convert)
        Chiffred = chiffrement(mot_convert,c) #Chiffrement de la list convertie
        print("Le cryptage par RSA est :",Chiffred)
        print() 
        return Chiffred
    messageChiffreRSA = RSA()


    """Déchiffrement (à fixer)"""
    def RSA_dechiffre():
        listCode = convertToList(messageChiffreRSA)
        inverse = find_inverse(c,n)

        rankToCode =dechiffrement(listCode,inverse,N,c)
        s = convert_to_letter(rankToCode)
        lettresDechiffre = joinLetter(s)
        print("Le rang des lettres décryptées est : ",rankToCode)
        print("Le déchiffrement donne :",lettresDechiffre)
        print() 
        return(lettresDechiffre)

    RSA_dechiffre()

t=time()
Main()
print("temps d'éxecution :",time()-t)
"""Voir erreur L64"""