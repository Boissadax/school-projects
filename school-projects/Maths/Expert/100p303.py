from random import randint
def controle():
    L=[]
    D=[]
    for k in range(100):
        L.append(k)
    for i in range(8):
        x=L.pop(randint(0,99-i))
        D.append(x)
    return D
controle()