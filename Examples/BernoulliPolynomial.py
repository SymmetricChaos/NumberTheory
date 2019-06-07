from Rationals import bernoulli_number, Rational
from Polynomials import Polynomial
from Other import choose

for n in range(1,9):
    P = Polynomial([0])
    for k in range(n+1):
        b = bernoulli_number(n-k)
        c = choose(n,k)
        co = b*c
        P += Polynomial([0]*k+[co])
    
    print(P)
    print()