from time import *
def puissance_naive(a,n):
    res = a
    for i in range(2,n):
        res = res*a
    print("le temps est:",res)
    return

def puissance_rapide(a,n):
    if n == 0:
        return a
    elif n%2 == 0:
        return puissance_rapide(a,(n//2))**2
    else :
        return a * puissance_rapide(a,n//2)

t1 = time()
print("Puissance rapide :",puissance_rapide(13671,62043))
print("le temps d'execution est :",time()-t1,"s")

t2 = time()
print("Puissance naive:",puissance_naive(13671,62043))
print("le temps d'execution de la puissance naïve est:",time()-t2,"s")

L = []
#print([i**9%253 for i in L])