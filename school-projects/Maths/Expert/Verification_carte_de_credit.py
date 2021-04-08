#Variables
codeCarte = [4,9,7,5,8,9,9,1,4,4,8,7,0,8,3,7]#Le numéro insee avec la clé

#Fonction pour valider le numéro de carte
def verifLuhn(codeCarte):
    #On liste un chiffre sur 2 à partir du dernier
    s=[]
    L1=[]
    for i in 1,3,5,7,9,11,13,15:
        L1.append(codeCarte[i])
    print("Les numéros L1 sont :", L1)

    #On liste le double de tous les autres avec une condition (si le double>9 alors on additionne les deux chiffres le composants)
    L2=[]
    a=[]
    b=[]
    for i in 0,2,4,6,8,10,12,14:
        double = codeCarte[i]*2
        if double <=9 :
            L2.append(double)
        else:
            a = [int(x) for x in str(double)]
            b.append(a[0]+a[1])
    print("Les chiffres douclés inférieurs ou égaux à 9 sont :",L2)
    print("Les chiffres doublés supérieurs à 9 dont les chiffres ont étés additionnés sont:",b)

    #On fait une liste rassemblant tous les chiffres
    L_Total=L1+L2+b
    print("Les chiffres a additioner sont :",L_Total)

    #On additione tous ces chiffres
    addition = sum(L_Total)
    print("En faisant la somme on a :", addition)

    #On vérifie le critère de divisibilité
    if addition % 100 == 0:
        print("C'est un multiple de 10 donc le code de carte est bon ")
    else:
        print("Ce n'est pas un multiple de 10 donc le code de carte est faux ")

#Afficher la vérification luhn
afficherValidation = verifLuhn(codeCarte)
print(afficherValidation)