from ModularArithmetic import legendre_symbol, jacobi_symbol, kronecker_symbol
from GeneralUtils import equal_spacing_grid

print("Legendre Symbol")
G = [[" ",1,2,3,4,5,6],[]]
for p in [3,5,7,11,13,17,19]:
    R = [f"{p} "]
    for a in [1,2,3,4,5,6]:
        R.append(legendre_symbol(a,p))
    G.append(R)

equal_spacing_grid(G,3)

print("\n\n\nJacobi Symbol")

G = [[" ",1,2,3,4,5,6],[]]
for p in [1,3,5,7,9,11,13]:
    R = [f"{p} "]
    for a in [1,2,3,4,5,6]:
        R.append(jacobi_symbol(a,p))
    G.append(R)

equal_spacing_grid(G,3)


print("\n\n\nKronecker Symbol")

G = [[" ",1,2,3,4,5,6],[]]
for p in [1,2,3,4,5,6]:
    R = [f"{p} "]
    for a in [1,2,3,4,5,6]:
        R.append(kronecker_symbol(a,p))
    G.append(R)

equal_spacing_grid(G,3)