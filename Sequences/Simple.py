from Sequences.NiceErrorChecking import require_integers

def naturals(offset=0):
    """
    Natural Numbers: Nonnegative whole numbers
    
    Args:
        offset -- nonnegative integer specifying first value returned
    """
    
    require_integers(["offset"],[offset])
    assert offset >= 0
    
    ctr = offset
    
    while True:
        yield ctr
        
        ctr += 1


def integers():
    """Integers: All integers starting with zero then with positive before negative"""
    
    yield 0
    
    for n in naturals(1):
        yield n
        yield -n


def arithmetic(a,n):
    """
    Arithmetic Sequence: Integers with constant difference
    
    Args:
        a -- starting value\n
        n -- common difference
    """
    
    require_integers(["a","n"],[a,n])
        
    out = a
    
    while True:
        
        yield out
        
        out += n


def geometric(a,n):
    """
    Geometric Sequence: Integers with constant ratio
    
    Args:
        a -- starting values\n
        n -- common ratio
    """
    
    require_integers(["a","n"],[a,n])
        
    out = a
    
    while True:
        
        yield out
        
        out *= n


def arithmetrico_geometric(a,n,b,m):
    """
    Arithmetrico-Geometric Sequence: Product of an arithmetic sequence with a geometric sequence
    
    Args:
        a -- starting value for arithmetic sequence\n
        n -- common difference for arithmetic sequence\n
        b -- starting value for geometric sequence\n
        m -- common ratio for geometric sequence
    """
    
    require_integers(["a","n","b","m"],[a,n,b,m])
    
    for ari,geo in zip(arithmetic(a,n),geometric(b,m)):
        
        yield ari*geo


def powers(n):
    """
    Powers of N: Special case of Geometric Sequence
    
    Args:
        n -- constant multiple
    """
    
    require_integers(["n"],[n])
    assert n >= 0
    
    pw = 1
    
    while True:
        yield pw
        
        pw *= n


def exponent(e):
    """
    Exponent Numbers: All naturals raised to the same exponent
    
    Args:
        e -- exponent to raise each natural number to
    """
    
    assert type(e) == int
    assert e >= 0
    
    for n in naturals():
        yield n**e


def fermat():
    """Fermat Numbers: 2^2^n+1 for n in naturals"""
    
    for n in naturals():
        yield 2**2**n+1