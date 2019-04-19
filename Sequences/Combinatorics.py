def derangements():
    """Derangement numbers"""
    yield 1
    yield 0
    
    S = [1,0]
    
    ctr = 0
    while True:
        ctr += 1
        d = ctr * (S[0]+S[1])
        S[0], S[1] = S[1], d
        yield d
        
def catalan():
    """Catalan Numbers"""
    n = 0
    while True:
        N = 1
        D = 1
        for k in range(2,n+1):
            N *= n+k
            D *= k
        yield N//D
        
        n += 1