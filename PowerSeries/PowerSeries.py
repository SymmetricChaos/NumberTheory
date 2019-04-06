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
