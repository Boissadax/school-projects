"""Programme de Chiffrement RSA avec clé publique (Coté BOB)"""
import random
from random import *
from math import *
from time import *

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def convertToList(string): #Chaine de caractères -> liste
    list1=[]
    list1[:0]=string
    return list1

def joinInt(s): #Sert a convertir liste de caractère en chaine de caractères
    #str1 = ""
    string_ints = [str(int) for int in s]
    return " ".join(string_ints)

def puissance(a,n): #Calcul éfficacement a exposant n
    if n == 0:
        return 1
    elif n%2 == 0:
        return puissance(a*a,n//2)
    else :
        return a * puissance(a,n-1)

def chiffrementRSA(message,n,c): #Chiffre la liste de des rangs de chaque lettre du message en effectuant x^c=y(mod N)
    B = convertToList(message)
    L=[k for i in range(len(B))for k in range(26) if B[i] == alphabet[k]]
    C = [(puissance(L[i],c)%n) for i in range(0,len(L))]
    C = joinInt(C)
    return C

def main():
    n = int(input("Entrez n publique :"))
    c = int(input("Entrez c publique :"))
    message = input("Entrez votre message :")
    t=time()
    print("Le chiffrement RSA donne :",chiffrementRSA(message,n,c))
    print("Temps d'éxécution:",time()-t)

main()