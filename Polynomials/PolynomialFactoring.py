from sympy import Poly, symbols

from PolynomialOOP import polynomial
from math import sqrt, floor
from itertools import product as cart_product

Q = polynomial([-20,0,1,0,3])
print(Q)

# If we can find a root of the polynomial that corresponds to a factor of the 
# form x - n where n is the root.
def factor_at_zero(P):
    n = len(P)
    for i in range(0,(n//2)+1):
        print(i)
        print(P.evaluate(i))
        if P.evaluate(i)[0] == 0:
            return polynomial([-i,1])

# Factors of the number that results from evalutating a polynomial at a point
def point_factors(P,point):
    E = P.evaluate(point)[0]
    
    out = set()
    for i in range(1,floor(sqrt(abs(E)))+1):
        if E % i == 0:
            out.add(i)
            out.add(E//i)
            out.add(-i)
            out.add(-E//i)
            
    return list(out)

def flatten(L):
    flat = []
    for sublist in L:
        try: 
            iter(sublist)
        except TypeError:
            flat.append(sublist)
        else:
            for item in sublist:
                flat.append(item)
    return flat

#R = factor_at_zero(Q)
#S = Q//R
#print(Q)
#print(R)
#print(S)
#print(S*R)

PF = point_factors(Q,0)


def factor_at_nonzero(P):
    n = len(P)
    Z = point_factors(P,0)
    print(n//2+1)
    for i in range(1, n//2 + 1):
        M = point_factors(P,i)
        Z = [flatten(z) for z in cart_product(Z,M)]
        for u in Z:
            Q = polynomial(u)
            if P//Q == 0:
                return Q
    
factor_at_nonzero(Q)