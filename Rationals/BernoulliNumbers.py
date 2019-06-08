from Combinatorics import choose
from Rationals.RationalType import Rational

def bernoulli_number(m):
    if m > 2 and m % 2 == 1:
        return Rational(0)
    out = 0
    for k in range(m+1):
        for v in range(k+1):
            
            c = choose(k,v)
            R = Rational(v**m,k+1)
            out += R*c*(-1)**v
    return out

