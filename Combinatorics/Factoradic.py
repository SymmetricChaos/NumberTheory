def factoradic(n):
    L = []
    ctr = 1
    while n > 0:
        n, l = divmod(n,ctr)
        L.append(l)
        ctr += 1
    L.reverse()
    return L

def factoradic_permutation(L,f):
    assert type(f) == int
    assert f >= 0
    F = factoradic(f)
    out = []
    while len(L) > len(F):
        out.append( L.pop(0) )
    for i in F:
        out.append( L.pop(i) ) 
    return out