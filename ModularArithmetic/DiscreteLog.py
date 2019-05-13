# The discrete log is only guaranteed t exist when b is a primitive root of m
# (ie when it is a generator)

def discrete_log(a,b,m):
    """integer k such that b^k = a (mod m)"""
    if a == 1:
        return 0
    t = 1
    for k in range(1,m):
        # To save some work we multiply by b at each step rather than
        # going to the trouble of calculating b^k each time
        t = (t*b) % m
        if t == a:
            return k

# A much more efficient method
from math import ceil, sqrt
def baby_step_giant_step(a,b,m):
    """integer k such that b^k = a (mod m)"""
    lim = ceil(sqrt(m))
    
    table = {}
    
    for j in range(lim):
        table[pow(b,j,m)] = j
    
    c = pow(b,lim*(m-2),m)
    y = a
    for i in range(m):
        y = ( a * pow(c,i,m) ) % m
        if y in table:
            return i*lim+table[y]
