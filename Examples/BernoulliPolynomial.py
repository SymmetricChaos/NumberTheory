from Rationals import bernoulli_number, Rational
from Polynomials import Polynomial
from Other import choose

P = Polynomial([0])
n = 4
for k in range(n+1):
    b = bernoulli_number(n-k)
    c = choose(n,k)
    co = b*c
    P = P + Polynomial([0]*k+[co])
print(P)