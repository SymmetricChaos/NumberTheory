from Polynomials.PolynomialType import Polynomial

def lagrange_interpolation(L,func):
    """Lagrange Polynomial"""
    final = Polynomial([0])
    for j in L:
        out = Polynomial([func(j)])
        for m in L:
            if m != j:
                d = Polynomial([1/(j-m)])
                X = Polynomial([-m,1])
                out *= d*X
        final += out
    return final
            