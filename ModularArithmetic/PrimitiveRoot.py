from ModularArithmetic import coprimes

# A pimitive root modulo n g^k = a mod n for every a coprime to n
# Equivalently a primitive root is a generating element of the multiplicative 
# group modulo n

# Show all the congruences
def show_congruences(g,m):
    # choose the width 
    W = len(str(m))
    for i in range(m):
        print("{}^{:<{}} = {}".format(g,i,W,g**i % m))
    print()
    
def primitive_roots(m):
    # List the numbers coprime to m since primitive roots must be coprime and
    # they must generate the set of all the numbers coprime to m
    C = coprimes(m)
    L = []
    out = []
    
    # Try each coprime number and see if it generates the set C
    # If it does write down that number otherwise try again
    for g in C:
        for i in range(m):
            L.append(g**i % m)
        
        if set(L) == set(C):
            out.append(g)
        L = []
        
    return out

m = 18
r = primitive_roots(m)
print("numbers coprime to {}\n{}\n".format(m,coprimes(m)))
print("primitive roots mod {}\n{}\n".format(m,r))
for i in r:
    show_congruences(i,m)