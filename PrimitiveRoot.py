# A pimitive root modulo n g^k = a mod n for every a coprime to n



def congruences(g,m):
    for i in range(m):
        print("{}^{} = {} mod {}".format(g,i,g**i % m,m))

congruences(3,7)

#def primitive_root(g,n):
    