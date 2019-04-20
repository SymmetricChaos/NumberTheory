from math import sqrt, ceil
from Computation.RootFinding import int_root, is_square


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
    
    lim = int_root(n)+1
    
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


def fermats_method(n,iters=0):
    a = int_root(n)
    fct = False
    if iters == 0:
        while True:
            a += 1
            b2 = a**2-n
            if is_square(b2):
                fct = True
                break
    else:
        for i in range(iters):
            a += 1
            b2 = a**2-n
            if is_square(b2):
                fct = True
                break
    
    if fct == True:
        return a-int_root(b2), a+int_root(b2)
    
    return 1,n


def fermat_and_trial(n,lim=None):
    
    a = int_root(n)
    
    if lim == None:
        lim = a//2
    
    factor_found = False
    while True:
        a += 1
        b2 = a**2-n
        b = int_root(b2)
            
        if b**2 == b2:
            factor_found = True
            break
    
        if a - b < lim:
            break
        
    if factor_found == True:
        return a-int_root(b2), a+int_root(b2)
        
    else:
        for i in range(2,lim):
            if n % i == 0:
                return i,n//i
    
    return 1,n

