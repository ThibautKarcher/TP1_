x=int()
y=int()
z=int()
x=input("Entrez x: ")
y=input("Entrez y: ")
print("\nAvant permutation:\nx : {}\ny : {}\n".format(x, y))
z=x
x=y
y=z
print("Après permutation:\nx : {}\ny : {}\n".format(x, y))