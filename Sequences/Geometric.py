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


def hypotenuse():
    """Primitive Hypotenuse Numbers"""
    
    for m in naturals(1):
        print("!")
        if m % 2 == 0:
            for n in range(1,m):
                if gcd(m,n) == 1:
                    yield m*m+n*n
        else:
            for n in range(2,m,2):
                if gcd(m,n) == 1:
                    yield m*m+n*n

for n,v in enumerate(hypotenuse()):
    if n > 20:
        break
    print(v)