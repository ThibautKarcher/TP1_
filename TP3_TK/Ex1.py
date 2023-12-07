#exercice a#
"""

N=int(input("Entrez une valeur : "))
s=int()
t=0
for i in range(0,N+1) :
    t=s
    s=i+t
print("La somme des N entiers naturels est {}".format(s))
"""
#exercice b#
'''
N=int(input("Entrez une valeur : "))
while N!=100 :
    N=int(input("Entrez une valeur : "))
print("C'est bon")

'''

#exercice c#
'''

n=0
m=0
b=0

for i in range(0,9) :
    N=float(input("Entrez une note : "))
    if N < 10 :
        n=n+1
    elif N==10 or (N > 10 and N < 15) :
        m=m+1
    else :
        b=b+1
print("Il y a {} valeurs inférieures à 10, {} valeurs entre 10 et 15 et {} valeures au dessus de 15".format(n,m,b))

'''

#exercice d#
'''

t=0
s=0
N=0
X=int(input("Entrez une valeur : "))
while X > N :
    N=N+1
    X=X-N
print(N)

'''