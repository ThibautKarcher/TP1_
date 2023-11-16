print("Saisir le nombres de minutes écoulées depuis le début du mois :")
min=input()
min=int(min)
minutes=min%60
heures=(min/60)%24
heures=int(heures)
jour=(min/60/24)%24
jour=int(jour)
print("La date associées a ce nombre de minutes écoulées et le {} du mois à {} heures et {} minutes".format(jour, heures, minutes))
