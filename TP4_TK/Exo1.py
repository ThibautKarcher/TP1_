N=float(input("Vous cherchez la table de multiplication de quel nombre ? : "))
L=['0','1','2','3','4','5','6','7','8','9']
for i in range(10) :
    m=int(L[i])
    r = m*N
    print("{} * {} = {}".format(N,m,round(r,2)))