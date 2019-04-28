from PolynomialOOP import polynomial
from math import sqrt, floor
from itertools import product as cart_product


# Flatten a list
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

# If we can find a root of the polynomial that corresponds to a factor of the 
# form x - n where n is the root.
def factor_at_root(P):
    n = len(P)
    for i in range(0,(n//2)+1):
        if P.evaluate(i)[0] == 0:
            return polynomial([-i,1])
    return P


def factor_at_nonzero(P):
    n = len(P)
    Z = point_factors(P,0)
    for i in range(2, n//2 + 1):
        M = point_factors(P,i)
        Z = [flatten(z) for z in cart_product(Z,M)]
        for u in Z:
            Q = polynomial(u)
            S = P//Q
            if len(S) == i and S.coef[-1] == 0:
                return Q
    return P
    

def poly_factor_1L(P):
    Q = factor_at_root(P)
    if Q == P:
        Q = factor_at_nonzero(P)
    return Q

#def poly_factor(P):
#    F = []
#    Q = poly_factor_1L(P)
#    if Q == P:
#        return [P]
#    
#    F.append(Q)
#    F.append(P//Q)
#    
#    
##    out = []
##    while True:
##        R = F.pop()
##        r = poly_factor_1L(P)
##        if  ==:
            
            
        
Q = polynomial([-20,5,1,3,5])
print(Q)
F = poly_factor_1L(Q)
print(F)
print(Q//F)
print(F*(Q//F))