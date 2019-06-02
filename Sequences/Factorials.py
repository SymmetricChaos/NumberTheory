from itertools import cycle

def factorials():
    """Factorial Numbers"""
    ctr = 1
    out = 1
    while True:
        out = out * ctr
        ctr += 1
        yield out

def alternating_factorials():
    """Alternating Factorial Numbers"""
    cyc = cycle([1,-1])
    out = 0
    for fac,p in zip(factorials(),cyc):
        out += fac*p
        yield abs(out)
        
def kempner_function():
    L = []
    for n,i in enumerate(factorials(),1):
        L.append(i)
        for ctr,f in enumerate(L,1):
            if f % n == 0:
                yield ctr
                break