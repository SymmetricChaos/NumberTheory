from Sequences.Simple import naturals
from Sequences.Utils import factorization

## Generator that returns primes (not my work)
def primes():
    """Prime Numbers"""
    D = {}
    q = 2
    
    while True:
        if q not in D:
            
            yield q
                
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

# Cumulative product of prime numbers.
def primorials():
    """Primoral Numbers"""

    out = 1
    for i in primes():
        
        yield out
        
        out *= i

# Positive integers with no prime factors greater than B.
def smooth(B):
    """Smooth Numbers"""
        
    for n in naturals(1):
        out = n
        for f in range(2,B+1):
            while n % f == 0:
                n = n // f
            if n == 1:
                yield out
                break


# Positive integers with no prime factors less than B.
def rough(B):
    """Rough Numbers"""
    
    for n in naturals(1):
        r = True
        for f in range(2,B):
            if n % f == 0:
                r = False
                break
        if r:
            yield n
            
# Integers that have more factors than any small positive integer.
def highly_composite():
    """Highly Composite Numbers"""
    F = 0
    for i in naturals(1):
        L = len(factorization(i))
        if L > F:
            F = L
            yield i

# Number of divisors for each positive integer.
def divisors():
    """Number of Divisors"""
    for i in naturals(1):
        yield len(factorization(i))
        
# Numbers that have no more than one prime factors. Equivalently those that are
# not divisible by any square number.
def squarefree():
    """Squarefree Numbers"""
    for n in naturals(1):
        for i in naturals(2):
            if n % i**2 == 0:
                break
            if (i**2) > n:
                yield n
                break

#def squarefree_kernel():
#    """Squarefree Kernels"""
#       for n in naturals(1):
        