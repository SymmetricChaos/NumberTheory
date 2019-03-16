from PolynomialRepresentation import *

P = [1,-42,1,-12,-1,0,0]
Q = [-3,1,0,0]

print(P)
poly_print(P)
print()

P = [0,1,1,1,1,1,1,0,1,1,1,1,1,1]
Q = [1,1,0,1,1,0,0,0,1]

#print(polyadd(P,Q,2))
#print(polymult([1,0,2,1,0],[1,1,2,1],3))

print(P)
print(Q)
print()
print(poly_divmod(P,Q,2))