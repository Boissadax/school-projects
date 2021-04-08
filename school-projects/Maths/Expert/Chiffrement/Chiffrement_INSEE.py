#Variables
N=[8,7,7,0,8,1,2,0,2,5,0,2,2] #Les 13 premiers chiffres du numéro INSEE
C=0 #Initialisation de la clé
insee = [8,7,7,0,8,1,2,0,2,5,0,2,2,9,7]#Le numéro insee avec la clé
checked = 0 #La variable qui renvoie si la clé est bonne ou non

#Fonction pour calculer la clé
def cle(N):
    s = [str(i) for i in N]
    n = int("".join(s))
    R=n%97
    C=97-R
    return C

#Fonction pour valider la clé
def checkKey(insee):
    #On calcule la clé du numéro insee
    s=[]
    L1=[]
    for i in range (0,13):
        L1.append(insee[i])
        s.append(str(L1[i]))
    n = int("".join(s))
    print("Le numéro de sécurité sociale est :", n)
    R=n%97
    C=97-R
    print("La clé de ce numéro est :",C)

    #On prend la clé de la liste insee
    s2 = []
    L2=[]
    for i in range(13,15):
        L2.append(insee[i])
        s2.append(str(L2[i-13]))
    keyToCheck = int("".join(s2))
    print("La clé à vérifier est :", keyToCheck)

    #Vérification de la clé
    if keyToCheck == C:
        print("La clé est bonne")
    else:
        print("La clé est éronnée")


#Afficher la clé
afficherCle = cle(N)
print(afficherCle)

#Afficher la validation de la clé
afficherValidation = checkKey(insee)
print(afficherValidation)