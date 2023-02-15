from random import *
def mitulapsed(n:list,kh:list):
    """Kirjeldus....
    :param list i: Lapse järjend
    :param list p: Hinne järjend
    :rtype: list, list
    """
    x=int(input("kui palju õpilasi?"))
    for i in range(x):
        nimi= input("Sisestage nimi: ")
        n.append(nimi)
        randomHinne=round(uniform(1,5),1)
        kh.append(randomHinne)
    for o in range(len(n)):
        print(f"{n[o]} {kh[o]}") 
    return n, kh
def sortirovka(n:list,kh:list):
    """Kirjeldus....
    :param list i: Lapse järjend
    :param list p: Hinne järjend
    :rtype: list, list
    """
    for p in range(0,len(n)):
        for o in range(0,len(n)):
            if n[p]<n[0]:
                abi=n[p]
                n[p]=n[o]
                n[o]=abi
                abi=kh[p]
                kh[p]=kh[o]
                kh[o]=abi
    return n, kh
def otli4nik(n:list,kh:list):
    """Kirjeldus....
    :param list i: Lapse järjend
    :param list p: Hinne järjend
    :rtype: list, list
    """
    if n==5:
        ind=kh.index(kh)
        nimi=n[ind]
    else:
        nimi="ei ole"
    return nimi, n
def keskmine(n:list,kh:list):
    """Kirjeldus....
    :param list i: Lapse järjend
    :param list p: Hinne järjend
    :rtype: list, list
    """
    kesk=sum(kh)/len(kh)
    print(f"Keskmine palk on {kesk}")
def found(n:list,kh:list):
    """Kirjeldus....
    :param list i: Lapse järjend
    :param list p: Hinne järjend
    :rtype: list, list
    """
    x= input("Sisestage oma nimi: ")
    if x in n:
        s = n.index(x)
        b = kh[s]
        print(n[s], round(b,1))
def Lisa_andmed(n:list,kh:list):
    """Kirjeldus....
    :param list i: Lapse järjend
    :param list p: Hinne järjend
    :rtype: list, list
    """
    n=int(input("Mitu Lapsed:"))
    for j in range(n):
        laps=input("Sisesta nimi: ")
        hinne=int(input("Sisesta hinne: "))
        n.append(laps)
        kh.append(hinne)
    return n,kh