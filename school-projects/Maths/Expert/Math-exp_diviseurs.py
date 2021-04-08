n=int(input("Entrez le nombre souhaité:"))
L=[]
for i in range(1,n+1):
    if n%i==0:
        L.append(i)
        #L.append(-i)
L.sort()
print(L)
print(n," à ",len(L)," diviseurs.")

#Les couples

if a*b==60:
