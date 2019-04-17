# Logarithm by factorization method


from math import log2, ceil, sqrt

def prime_factorization(n):
    """Prime Factors with Multiplicity"""
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = ceil(sqrt(n))+1
    L = []
    
    p = 1
    while True:
        p += 1
        while n % p == 0:
            L.append(p)
            n = n // p
            
        if n == 1:
            break
        
        if p > lim:
            L.append(n)
            break
    return L

def find_smooth(n,B):
    while True:
        P = prime_factorization(n)
        if all([i in B for i in P]):
            return P
        n -= 1

def estimate_log(n,B=[2,3,5,7,11,13,17,19]):
    
    D = {}
    for b in B:
        D[b] = log2(b)
    
    S = find_smooth(n,B)
    print(S)
    return sum(D[s] for s in S)

N = 765
print(estimate_log(N))
print(log2(N))