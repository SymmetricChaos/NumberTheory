def naturals(n=0):
    """Natural Numbers"""
    
    assert type(n) == int
    assert n >= 0
    
    ctr = n
    
    while True:
        yield ctr
        
        ctr += 1
        

def integers():
    """Integers"""
    
    yield 0
    
    for n in naturals(1):
        yield n
        yield -n


def arithmetic(b=0,n=1):
    """Arithmetic Sequence"""
    
    assert type(b) == int
    assert type(n) == int
        
    out = b
    
    while True:
        
        yield out
        
        out += n


def geometric(b=1,n=2):
    """Geometric Sequence"""
    
    assert type(b) == int
    assert type(n) == int
        
    out = b
    
    while True:
        
        yield out
        
        out *= n


def powers(n):
    """Powers of N"""
    
    assert type(n) == int
    assert n >= 0
    
    pw = 1
    
    while True:
        yield pw
        
        pw *= n


def exponent(e=1):
    """Exponent Numbers"""
    
    assert type(e) == int
    assert e >= 0
    
    for n in naturals():
        yield n**e


def fermat():
    """Fermat Numbers"""
    
    for n in naturals():
        yield 2**2**n+1
