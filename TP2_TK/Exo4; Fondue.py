BASE=int(4)
fromage=float(800.0)
eau=float(2)
ail=float(2)
pain=float(400)
nbConvives=int(input("Entrez le nombre de personnes conviées à la fondue : "))
quantitéFromage=(fromage*nbConvives)/BASE
quantitéEau=(eau*nbConvives)/BASE
quantitéAil=(ail*nbConvives)/BASE
quantitéPain=(pain*nbConvives)/BASE
print("Pour faire une fondue pour {} personnes, il vous faut :\n- {} gr de fromages\n- {} dL d'eau\n- {} gousse(s) d'ail\n- {} gr de pain".format(nbConvives, quantitéFromage, quantitéEau, quantitéAil, quantitéPain))