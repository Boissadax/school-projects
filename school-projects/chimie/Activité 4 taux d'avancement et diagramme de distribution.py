#Taux d'avancement
pH=float(input('pH de la solution ? pH ='))
C=float(input('Concentration en soluté apporté en mol/L ? C ='))
V=float(input('Volume de la solution en L ? V ='))
xf=round(10**-pH*V,5)
xmax=C*V
nfAH=(C*V) - xf
nfA=xf
tau=round(xf/xmax,2)
if tau>1 : print('taux d\'avancement =', tau,'impossible')
else :
    if tau==1 : print('taux d\'avancement =',tau,'Acide fort')
    else :
        print('taux d\'avancement =',tau,'Acide faible')
if tau < 0.1: print("l'acide est donc faiblement dissocié dans l'eau")
else :
    print("l'acide n'est pas faiblement dissocié dans l'eau")

print("xf:",xf)
print("xmax (C*V) =",xmax)
print("La quantité de matière finale du réactif acide est :", nfAH)
print("La quantité de matière finale du produit base est :", nfA)
