from Sequences.Simple import naturals
from Sequences.Utils import factorization
from collections import defaultdict

## Generator that returns primes (not my work)
def primes():
    """Prime Numbers"""
    
    D = defaultdict(list)
    q = 2
    
    while True:
        
        if q not in D:
            yield q
            D[q * q] = [q]
        
        else:
            for p in D[q]:
                D[p+q].append(p)
            del D[q]
        
        q += 1


def composites():
    """Composite Numbers"""
    
    for n in naturals(4):
        for p in primes:
            if n % p == 0:
                yield n
                break


# Cumulative product of prime numbers.
def primorials():
    """Primoral Numbers"""
    
    out = 1
    for i in primes():
        
        yield out
        
        out *= i


def pythagorean_primes():
    """Pythagorean Primes"""
    
    for p in primes():
        if (p-1)%4 == 0:
            yield p


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


def divisors():
    """Number of Divisors"""
    
    for i in naturals(1):
        yield len(factorization(i))


def prime_divisors():
    """Number of Prime Divisors with Multiplicity"""
    
    for n in naturals(1):
        ctr = 0
        
        for p in primes():
            while n % p == 0:
                ctr += 1
                n = n // p
            
            if n == 1:
                yield ctr
                break


def unique_prime_divisors():
    """Number of Unique Prime Divisors"""
    
    for n in naturals(1):
        ctr = 0
        
        for p in primes():
            if n % p == 0:
                ctr += 1
            
            while n % p == 0:
                n = n // p
            
            if n == 1:
                yield ctr
                break


# Numbers that have no more than one prime factors. 
# Equivalently numbers those that are not divisible by any square number.
def squarefree():
    """Squarefree Numbers"""
    
    for n in naturals(1):
        for i in naturals(2):
            if n % i**2 == 0:
                break
            
            if (i**2) > n:
                yield n
                break


# The product of the unique prime factors of a number
# Equivalently the largest squarefree number that is a factor
def squarefree_kernel():
    """Squarefree Kernels"""
    
    for n in naturals(1):
        K = 1
        
        for p in primes():
            
            if n % p == 0:
                K *= p
                while n % p == 0:
                    n //= p
            
            if n == 1:
                yield K
                break


# Very slow
def euclid_mullin():
    """Euclid-Mullin Sequence"""
    
    P = 2
    
    while True:
        for i in primes():
            if (P+1) % i == 0:
                yield i
                P = P*i
                break
