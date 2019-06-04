# The rational root theorem makes it possible to determine all the rational
# roots of a polynomial.

from PolynomialType import Polynomial
from Rationals import Rational
from Other import factorization

P = Polynomial([-2,5,-5,3])
print(P)

n = factorization(2)
d = factorization(3)
n = [x for x in n] + [-x for x in n]
print(n,d)

for i in n:
    for j in d:
        r = Rational(i,j)
        print(r,P.evaluate(r))