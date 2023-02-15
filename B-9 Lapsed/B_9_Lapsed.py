from module1 import *
nimed=[]
keskmised_hinnad=[]
listi = mitulapsed(nimed, keskmised_hinnad)
print(nimed, keskmised_hinnad)
x=input("vali, mida teha tahad\n1 Sortida loendeid\n2Näita õpilast\n3Leidke keskmine hinnang\n4Leidke lapse keskmine hinne, sisestades tema nime\n4Lisa andmed")
if x=="1":
    sort= sortirovka(nimed, keskmised_hinnad)
    print(nimed, keskmised_hinnad)
elif x=="2":
    sort= otli4nik(nimed, keskmised_hinnad)
    print(sort)
elif x=="3":
    keskmine(nimed, keskmised_hinnad)
elif x=="4":
    found(nimed, keskmised_hinnad)
elif x=="5":
    Lisa_andmed(nimed, keskmised_hinnad)
print(nimed, keskmised_hinnad)