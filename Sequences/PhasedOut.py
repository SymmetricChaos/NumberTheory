from collections import defaultdict
from itertools import count


def _legendre_symbol(a,p):
    """
    The Legendre Symbol: 1 if a is a quadratic residue mod p, -1 if it is a nonresidue, 0 if a is zero
    p must be prime but this is hard to check so is not done in the function itself
    """
    if p == 2:
        if a%2 == 0:
            return 0
        if a%8 in (1,7):
            return 1
        return -1
            
    out = pow(a,(p-1)//2,p)
    if out == 1:
        return 1
    if out == 0:
        return 0
    else:
        return -1





def miller_rabin_test(n):
    """
    Miller-Rabin Primality Test
    Returns 0 for composite, 1 for prime, and 2 for probably prime
    Deterministic for n less than 3,317,044,064,679,887,385,961,981 ≈ 2^81
    For greater numbers about 99.9999985% accurate
    """
    
    W = [2,3,5,7,11,13,17,19,23,29,31,37,41]
    
    # Deal with special cases first
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    
    d = n-1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    for witness in W:
        x = pow(witness,d,n)
        
        if x == 1 or x == n-1:
            continue
        
        for i in range(0,r+1):
            x = pow(x,2,n)
            
            if x == n-1:
                return 0
    
    if n >= 3317044064679887385961981:
        return 2
    else:
        return 1





def primes():
    
    D = defaultdict(list)
    
    for q in count(2,1):
        if q not in D:
            yield q-1
            D[q + q] = [q]
        
        else:
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]