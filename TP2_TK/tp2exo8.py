x=float(input("Entrez un nombre réel : "))
if ((-10 < x or -10 == x) and (x < -2 or x == -2)) or (x < 3 and 2 < x or x ==2) or (x == 1 or (x < 1 and 0 < x)):
    print("x appartient à I")
else :
    print("x n'appartient pas à I")