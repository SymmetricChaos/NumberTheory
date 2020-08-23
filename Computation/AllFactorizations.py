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
    
    F = [f for f in factorization(n) if f >= m]
    
    if len(F) == 0:
        yield [n]
    
    else:
        for f in F:
            for a in all_factorizations_inner(n//f,f):
                yield [f] + a


def all_factorizations(n):
    S = set([(n,)])
    for i in all_factorizations_inner(n):
        S.add(tuple(sorted(i)))
    return S


def prod(L):
    p = 1
    for i in L:
        p *= i
    return p


for x in range(25):
    print()
    L = []
    for i in all_factorizations(x+1):
        L.append(" × ".join([str(t) for t in i]))
    for i in sorted(L,key=len):
        print(i)