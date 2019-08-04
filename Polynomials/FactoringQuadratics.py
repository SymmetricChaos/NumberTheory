from PolynomialType import Polynomial

def factor_quadratic(P):
    assert type(P) == Polynomial
    assert P.degree() == 2
    a = P[0]
    b = P[1]
    c = P[2]
    print(a,b,c)
    
P = Polynomial([2,4,10])

print(P)

factor_quadratic(P)