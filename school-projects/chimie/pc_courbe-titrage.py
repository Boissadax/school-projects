import matplotlib.pyplot as plt
import numpy as np

Veau = float(input("Entrez le volume d'eau :"))
V_AH = float(input("Entrez le volume de solution titrée :"))
C_AH = float(input("Entrez la concentration de réactif titré :"))
C_HO = float(input("Entrez la concentration de réactif titrant :"))
VE = ((C_AH*V_AH)/C_HO)
n_AH, n_HO, n_Na, n_A, V, Conduct = [], [], [], [], [], []

def calcul_qtt_av_a_equi(i):
    V.append(i)
    n_AH.append((VE*0.01*10-0.10*i)*0.001)
    n_HO.append(0)
    n_Na.append(C_HO*i*1E-3)
    n_A.append(C_HO*i*1E-3)

def calcul_qtt_ap_equi(i):
    V.append(i)
    n_AH.append(0)
    n_HO.append((C_HO*i*1E-3) - VE*0.0001)
    n_Na.append(C_HO*i*1E-3)
    n_A.append(VE*1E-4)

def calcul_conductivite(i) :
    Conduct.append ((20*n_HO[i]+5.0*n_Na[i]+4.1*n_A[i])/(Veau*1E-3+1E-3*V[i]+V_AH*1E-3))

for i in range(0,26,1):
    if i <= VE:
        calcul_qtt_av_a_equi(i)
        calcul_conductivite(i)
    else:
        calcul_qtt_ap_equi(i)
        calcul_conductivite(i)

plt.subplot(121)
plt.plot(V,n_AH,'bx-',linewidth=0.5,label="n_AH")
plt.plot(V,n_HO,'rx-',linewidth=0.5,label="n_HO")
plt.plot(V,n_Na,'mx-',linewidth=0.5,label="n_NA")
plt.plot(V,n_A,'gx-',linewidth=0.5,label="n_A")
plt.legend()
plt.subplot(122)
plt.scatter(V, Conduct, label="Conductivité en $\mathrm{mS\cdot m^{-1}}$")
plt.legend()
plt.show()