from RationalType import Rational

def harmonic_sequence(n):
    H = Rational(1,1)
    ctr = 2
    while True:
        yield H
        if ctr > n:
            break
        H += Rational(1,ctr)
        ctr += 1
        
