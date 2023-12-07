nombreEtudiants=int(input("Donnez le nombre d'étudiants : "))
moyenne=0.0;
notes=[]
sommeNotes=0.0
erreur=float()
for i in range(0,nombreEtudiants) :
    note=float(input("Note étudiant {} : ".format(i)))
    notes.append(note)
    while erreur!=((note > 20) or note==20) or erreur!=((note < 0) or note == 0) :
        print("La note doit être entre 0 et 20\n")
        note=float(input("Saississez une nouvelle note : "))
        notes.append(note)
    sommeNotes=sommeNotes+notes[i]
moyenne=sommeNotes/(i+1)
print("\nMoyenne de classe : {}\n".format(moyenne))
print("Numéro de l'étudiant | note | écart à la moyenne")
for i in range(0,nombreEtudiants) :
    ecart=float(notes[i]-moyenne)
    print("{} | {} | {}\n".format(i,notes[i],ecart))