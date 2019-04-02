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

def factors(n,nontrivial=False):
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    L = []
    a, b = 1, n+1
    if nontrivial == True:
        a, b = 2, n
    for i in range(a,b):
        if n % i == 0:
            L.append(i)
    return L
    
def prime_factorization(n):
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    L = []
    for p in _primes_():
        while n % p == 0:
            L.append(p)
            n = n // p
        if n == 1:
            break
    return L


def aliquot_sum(n):
    if n <= 0:
        raise Exception("Alquoit sum not defined") 
    if n == 1:
        return 0
    return sum(factors(n)[:-1])
