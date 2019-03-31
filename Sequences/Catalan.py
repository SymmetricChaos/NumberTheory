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
