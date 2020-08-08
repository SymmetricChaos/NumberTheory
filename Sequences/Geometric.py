from Sequences.Primes import pythagorean_primes
from Sequences.Simple import naturals
from math import gcd

def nonhypotenuse():
    """Nonhypotenuse Numbers"""
    
    for n in naturals(1):
        for p in pythagorean_primes():
            
            if n % p == 0:
                break
            
            if p > n//2:
                yield n
                break


# Much more memory efficient
def raw_hypotenuse():
    """Primitive Hypotenuse Numbers without order and with repetitions"""
    
    for m in naturals(1):
        lim = m*m+1 # smallest number that can be produced in this round
        if m % 2 == 0:
            for n in range(1,m,2):
                if gcd(m,n) == 1:
                    yield m*m+n*n
        else:
            for n in range(2,m,2):
                if gcd(m,n) == 1:
                    yield m*m+n*n


def hypotenuse():
    """Primitive Hypotenuse Numbers"""
    
    L = []
    for m in naturals(1):
        lim = m*m+1 # smallest number that can be produced in this round
        if m % 2 == 0:
            for n in range(1,m,2):
                if gcd(m,n) == 1:
                    p = m*m+n*n
                    if p in L:
                        continue
                    else:
                        L.append(p)
        else:
            for n in range(2,m,2):
                if gcd(m,n) == 1:
                    p = m*m+n*n
                    if p in L:
                        continue
                    else:
                        L.append(p)
        L.sort()
        for i in L:
            if i > lim:
                break
            yield L.pop(0)