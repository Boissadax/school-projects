a = (int(input("Entrez a:")))
b = (int(input("Entrez b:")))


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print("Le pgcd est:", pgcd(a, b))
