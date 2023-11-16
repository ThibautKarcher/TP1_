nom=""
prénom=""
math=float()
info=float()
anglais=float()
promotion=int()
moy=float()
print("type de de la variable nom :")
print(type(nom))
print("type de de la variable prénom :")
print(type(prénom))
print("type de de la variable math :")
print(type(math))
print("type de de la variable info :")
print(type(info))
print("type de de la variable anglais :")
print(type(anglais))
print("type de de la variable promotion :")
print(type(promotion))
print("type de de la variable moy :")
print(type(moy))
nom="titi"
prénom="toto"
promotion=2023
math=12.5
info=12.5
anglais=12.5
moy=(math+info+anglais)/3
print("L'étudiant {} {} de la promotion {} a une moyenne de {}".format(prénom, nom, promotion, moy))
