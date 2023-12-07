#Exemple 1 avec les 2 tarifs#
'''

d=int(input("Donnez l'heure de début de la location (en heures) : "))
f=int(input("Donnez l'heure de fin de la location (en heures ) : "))
prix=int()
heures2=int()
erreur=int()
while erreur!=(d == f) :
    print("Attention ! l'heure de fin est identique à l'heure de début.\n")
    d=int(input("Donnez une nouvelle heure de début : "))
    f=int(input("Donnez une nouvelle horaire de fin : "))
while erreur!=(d > f) :
        print("Attention ! le début de la location est après la fin...\n")
        d=int(input("Donnez une nouvelle heure de début : "))
        f=int(input("Donnez une nouvelle horaire de fin : "))
while (erreur!=(d < 0 or d > 24)) or (erreur!=(f < 0 or f > 24)) :
    print("Les heures doivent êtres comprises entre 0 et 24 !\n")
    d=int(input("Donnez une nouvelle heure de début : "))
    f=int(input("Donnez une nouvelle horaire de fin : "))
prix=f-d
if (7 < d < 17 or 7==d) and (f > 16):
    heures2=17-d
    prix=heures2*2+(f-17)
elif (7 < f < 17 or f==17) and (d < 8):
    heures2=17-f
    prix=heures2*2+(7-d)
elif (d < 7) and (f > 17):
    heures2=17-7
    prix=heures2*2+(8-d)+(f-16)
elif ((d < 8) and (f < 8)) or ((d > 16) and (f > 16)):
    heures=f-d
    prix=heures
else :
    heures2=f-d
    prix=heures2*2
heures=f-d-(heures2)
print("Vous avez loué votre vélo pendant\n{} heures au tarif horarire de 1 euro\n{} heures au tarif horaire de 2 euros".format(heures,heures2))
print("Le montant total à payer est de {} euros".format(prix))

'''

#exemple 2 à tarif unique#
'''

d=int(input("Donnez l'heure de début de la location (en heures) : "))
f=int(input("Donnez l'heure de fin de la location (en heures ) : "))
prix=int()
heures2=int()
erreur=int()
while erreur!=(d == f) :
    print("Attention ! l'heure de fin est identique à l'heure de début.\n")
    d=int(input("Donnez une nouvelle heure de début : "))
    f=int(input("Donnez une nouvelle horaire de fin : "))
while erreur!=(d > f) :
        print("Attention ! le début de la location est après la fin...\n")
        d=int(input("Donnez une nouvelle heure de début : "))
        f=int(input("Donnez une nouvelle horaire de fin : "))
while (erreur!=(d < 0 or d > 24)) or (erreur!=(f < 0 or f > 24)) :
    print("Les heures doivent êtres comprises entre 0 et 24 !\n")
    d=int(input("Donnez une nouvelle heure de début : "))
    f=int(input("Donnez une nouvelle horaire de fin : "))
prix=f-d
if (7 < d < 17 or 7==d) and (f > 16):
    heures2=17-d
    prix=heures2*2+(f-17)
elif (7 < f < 17 or f==17) and (d < 8):
    heures2=17-f
    prix=heures2*2+(7-d)
elif (d < 7) and (f > 17):
    heures2=17-7
    prix=heures2*2+(8-d)+(f-16)
elif ((d < 8) and (f < 8)) or ((d > 16) and (f > 16)):
    heures=f-d
    prix=heures
else :
    heures2=f-d
    prix=heures2*2
heures=f-d
print("Vous avez loué votre vélo pendant\n{} heures".format(heures))
print("Le montant total à payer est de {} euros".format(prix)) 

'''

#Exemple impliquant 2 tarifs quand nécessaire et seulement 1 si un seul tarif actif#

d=int(input("Donnez l'heure de début de la location (en heures) : "))
f=int(input("Donnez l'heure de fin de la location (en heures ) : "))
prix=int()
heures2=int()
erreur=int()
while erreur!=(d == f) :
    print("Attention ! l'heure de fin est identique à l'heure de début.\n")
    d=int(input("Donnez une nouvelle heure de début : "))
    f=int(input("Donnez une nouvelle horaire de fin : "))
while erreur!=(d > f) :
        print("Attention ! le début de la location est après la fin...\n")
        d=int(input("Donnez une nouvelle heure de début : "))
        f=int(input("Donnez une nouvelle horaire de fin : "))
while (erreur!=(d < 0 or d > 24)) or (erreur!=(f < 0 or f > 24)) :
    print("Les heures doivent êtres comprises entre 0 et 24 !\n")
    d=int(input("Donnez une nouvelle heure de début : "))
    f=int(input("Donnez une nouvelle horaire de fin : "))
prix=f-d
if (7 < d < 17 or 7==d) and (f > 16):
    heures2=17-d
    prix=heures2*2+(f-17)
elif (7 < f < 17 or f==17) and (d < 8):
    heures2=17-f
    prix=heures2*2+(7-d)
elif (d < 7) and (f > 17):
    heures2=17-7
    prix=heures2*2+(8-d)+(f-16)
elif ((d < 8) and (f < 8)) or ((d > 16) and (f > 16)):
    heures=f-d
    prix=heures
else :
    heures2=f-d
    prix=heures2*2
heures=f-d-(heures2)
if heures == 0 :
    print("Vous avez loué votre vélo pendant\n{} heures au tarif horaire de 2 euros".format(heures2))
elif heures2 == 0 :
    print("Vous avez loué votre vélo pendant\n{} heures au tarif horaire de 1 euro".format(heures))
else :
    print("Vous avez loué votre vélo pendant\n{} heures au tarif horaire de 1 euro\n{} heures au tarif horaire de 2 euros".format(heures,heures2))
print("Le montant total à payer est de {} euros".format(prix))