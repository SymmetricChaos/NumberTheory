from RationalType import Rational

def harmonic_series(n):
    H = Rational(1,1)
    ctr = 2
    while True:
        yield H
        if ctr > n:
            break
        H += Rational(1,ctr)
        ctr += 1
        
def alternating_harmonic_series(n):
    H = Rational(1,1)
    ctr = 2
    alt = 1
    while True:
        yield H
        if ctr > n:
            break
        H += Rational(alt,ctr)
        alt *= -1
        ctr += 1