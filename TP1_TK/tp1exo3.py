print("Saisir le jour du mois :")
jour=input()
jour=int(jour)
print("Saisir l'heure :")
heures=input()
heures=int(heures)
print("Saisir la minute :")
minutes=input()
minutes=int(minutes)
heures=(jour*24)+heures
minutes=(heures*60)+minutes
print("Il y a donc eu {} minutes écoulées depuis le début du mois".format(minutes))
