from Combinatorics import choose
from Polynomials.PolynomialType import Polynomial

def bernstein_polynomial(v,n):
    B = Polynomial([1,-1])
    X = Polynomial([1])
    bi = choose(n,v)
    return X**v * B**(n-v) * bi
