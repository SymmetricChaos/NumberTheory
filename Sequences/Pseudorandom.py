def LCG(x,a,c,m):
    """Linear Congruential Generator"""
    
    while True:
        yield x
        x = ((a*x)+c)%m


def LFG(a,b,m):
    """Lagged Fibonacci Generator"""
    
    while True:
        yield a
        a,b = b,(a+b)%m