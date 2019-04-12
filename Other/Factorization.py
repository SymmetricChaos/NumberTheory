from math import sqrt, ceil
from Computation.Roots import int_root, is_square


# Needed to avoid circular reference with sequences
def _primes_():
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

def factorization(n,nontrivial=False):
    """All Unique Factors"""
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = ceil(sqrt(n))+1
    
    # Either include or don't include trivial factors
    if nontrivial == True:
        L = []
    else:
        L = [1,n]
    
    
    for i in range(2,lim):
        f,r = divmod(n,i)
        if r == 0:
            L.append(i)
            L.append(f)
            
    L = list(set(L))
    L.sort()
    
    return L
    
def prime_factorization(n):
    """Prime Factors with Multiplicity"""
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = ceil(sqrt(n))+1
    L = []
    
    for p in _primes_():
        while n % p == 0:
            L.append(p)
            n = n // p
            
        if n == 1:
            break
        
        if p > lim:
            L.append(n)
            break
    return L


def aliquot_sum(n):
    if n <= 0:
        raise Exception("Alquoit sum not defined") 
    if n == 1:
        return 0
    return sum(factorization(n)[:-1])


def fermats_method(n):
    a = int_root(n)
    
    while True:
        a += 1
        b2 = a**2-n
        if is_square(b2):
            break
    
    return a-int_root(b2), a+int_root(b2)