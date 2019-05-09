def power_series(x,A,c=0):
    
    out = 0
    for n,a in enumerate(A):
        out += a*(x-c)**n
    return out

def power_series_convergents(x,A,c=0):
    
    out = 0
    for n,a in enumerate(A):
        out += a*(x-c)**n
        yield out

def geometric_series(x,n):
    if abs(x) >= 1:
        raise Exception("Geometric series is convergent only for |x| < 1")
    
    out = 0
    for i in range(n):
        out += x**i
    return out

def geometric_series_convergents(x,n):
    if abs(x) >= 1:
        raise Exception("Geometric series is convergent only for |x| < 1")
    
    out = 0
    for i in range(n):
        out += x**i
        yield out