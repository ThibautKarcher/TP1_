N=int(input("Entrez un nombre entier: "))
if N < 0 :
    if N%2==0 :
        print("Le nombre est négatif et il est pair")
    else :
         print("Le nombre est négatif et il est impair")
elif N > 0 :
    if N%2==0 :
        print("Le nombre est positif et est pair")
    else :
        print("Le nombre est positif et est impair")
else :
        print("Le nombre est zéro (et il est pair)")
