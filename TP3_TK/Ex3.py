import random
n=0
t=0
x=random.randint(0,101)
while n != x :
    n=int(input("Devinez la valeur : "))
    t=t+1
    print("Nombre de tours : {}".format(t))
    if n < x :
        print("La valeur à trouver est plus grande")
    else :
        print("La valeur à trouver est plus petite")
print("Bravo, vous avez trouvé la valeur")
print("Il vous a fallu {} essais afin de trouver la valeur".format(t))