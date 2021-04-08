LA = "abcdefghijklmnopqrstuvwxyz"
texte2 ="maitrecorbeausurnarbreperchetenaitensonbecunfromaitrerenrdparlodeurallecheluitintapeuprescelangageetbonjourmonsieurducorbeauquevousetesjoliquqvousmesemblezbeausansmentirsivotreramageserapporteavotrepluragevouseteslephenixdeshotesdecesboisacesmotslecorbeauneseentpasdejoieetpourmontrersabellevoixilouvreunlargebeclaissetombersaproie"
#texte ="L'histoire de Rome s'étend sur plus de vingt-huit siècles, depuis sa fondation mythique par Romulus en 753 av. J.-C. jusqu'à son rôle actuel de capitale de la république italienne. Second berceau de la civilisation occidentale après Athènes, la ville fut successivement le centre de la monarchie romaine, de la République romaine (509 av. J.-C. – 27 av. J.-C.), puis de l'Empire romain (27 av. J.-C. – 330). Durant cette période, où naît la célèbre expression proverbiale « tous les chemins mènent à Rome », la ville aurait compté entre un et deux millions d'habitants et domine l'Europe, l'Afrique du Nord et le Moyen-Orient tant militairement que culturellement, diffusant dans ces territoires la langue latine, ses arts et techniques ainsi que la religion chrétienne. Depuis le ier siècle elle abrite le siège de l'Église catholique romaine, au sein des États pontificaux (752-1870) puis de la Cité du Vatican."
#texte2 = "xltecpnzcmplfdfcylcmcpapcnspepyltepydzympnfyqczxltecpcpycoalcwzopfclwwpnspwftetyelapfacpdnpwlyrlrppemzyuzfcxzydtpfcofnzcmplfbfpgzfdpepduzwtbfbgzfdxpdpxmwpkmplfdlydxpyetcdtgzecpclxlrpdpclaazceplgzecpawfclrpgzfdpepdwpaspytiopdszepdopnpdmztdlnpdxzedwpnzcmplfypdppyealdopuztppeazfcxzyecpcdlmpwwpgztitwzfgcpfywlcrpmpnwltddpezxmpcdlacztp"
texte3="i"
car = [ ' ' , ',' , ':' , ';' , '.' , "'" , '-' , '!' , '?' ]

def a(texte):
    nbcar = 0
    for i in range (len(texte)):
        if texte[i]=="a":
            nbcar=nbcar+1
    print(nbcar)

def alphabet(texte3):
    E = []
    for i in range (len(texte3)):
        for x in range (len(LA)):
            if texte3[i]==LA[x]:
                E.append(x)
    print(E)

def freq(texte):
    d = {}
    for c in texte:
        if c.lower() not in d:
            if c not in car:
                d[c.lower()] = 1
        else:
            d[c.lower()] += 1
    return d

def freqexact(texte):
    d2, compteur = {}, 0
    for c in texte:
        if c.lower() not in d2:
            if c not in car:
                d2[c.lower()] = 1
                compteur += 1
        else:
            d2[c.lower()] += 1
            compteur += 1

    return d2, compteur

d2 , compteur = freqexact(texte2)

def decodage(texte2):
    LT=[]
    for i in range(0,15):
        LT.append(LA[i+11])
    for i in range(14,26):
        LT.append(LA[i-14])
    textedecode=[]
    for k in range(len(texte2)):
        textedecode.append(LA[LT.index(texte2[k])])
    print("".join(textedecode))
    return("".join(textedecode))

decodage(texte2)
#a(texte)
#alphabet(texte3)
#L = sorted(freq(texte).items())
#for i in L:
#    print('{} : {}'.format(i[0], i[1]))
L2 = sorted(d2.items(), key = lambda colonne: colonne[1] , reverse = True)
for i in L2:
    print('{} : {}'.format(i[0],i[1]/compteur))