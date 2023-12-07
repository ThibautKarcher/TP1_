#exemple boucle for#
'''

f=1
n=int(input("Donnez un nombre : "))
for i in range(1,n+1) :
    f=f*i
    print("La valeur de la factorielle est {} après {} itérations".format(f,i))
print("La valeur finale de la factorielle de {} est donc {}".format(n,f))

'''

#exemple boucle while#
'''

i=0
f=1
n=int(input("Donnez un nombre : "))
t=n
while n != 1 :
    i=i+1
    f=f*n
    n=n-1
    print("La valeur est de {} après {} itérations".format(f,i))
print("La valeur finale de la factorielle de {} est donc : {}".format(t,f))

'''