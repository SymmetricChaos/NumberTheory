from ModularArithmetic import coprimes

# A pimitive root modulo n g^k = a mod n for every a coprime to n
# Equivalently a primitive root is a generating elements for some subgroups of a multiplicative group

# Show all the congruences
def show_congruences(g,m):
    print("modulo {}".format(m))
    # choose the width 
    W = len(str(m))
    for i in range(m):
        print("{}^{:<{}} = {}".format(g,i,W,g**i % m))
    print()
    
def primitive_roots(m):
    C = coprimes(m)
    L = []
    out = []
    for g in C:
        for i in range(m):
            L.append(g**i % m)
        
        if set(L) == set(C):
            out.append(g)
        L = []
        
    return out

m = 10
r = primitive_roots(m)
print("numbers coprime to {}\n{}\n".format(m,coprimes(m)))
print("primitive roots mod {}\n{}\n".format(m,r))
for i in r:
    show_congruences(i,m)