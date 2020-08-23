from math import floor, sqrt

def factorization(n):
    """All Unique Factors"""
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = floor(sqrt(n))+1
    
    L = []
    
    for i in range(2,lim):
        f,r = divmod(n,i)
        if r == 0:
            L.append(i)
            L.append(f)
            
    L = list(set(L))
    L.sort()
    
    return L


def all_factorizations_inner(n,m=1):
    
    F = [f for f in factorization(n) if f > m]
    
    if len(F) == 0:
        yield [n]
    
    else:
        for f in F:
            for a in all_factorizations_inner(n//f,f):
                yield [f] + a


def all_factorizations(n):
    S = set([])
    for i in all_factorizations_inner(n):
        S.add(tuple(sorted(i)))
    S = list(S)
    S = sorted(S,key=lambda x: x[0])
    return S


def prod(L):
    p = 1
    for i in L:
        p *= i
    return p

for i in all_factorizations(216):
    print(" × ".join([str(t) for t in i]))