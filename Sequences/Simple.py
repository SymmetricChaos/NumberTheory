from Sequences.NiceErrorChecking import require_integers, require_nonnegative

def naturals(offset=0):
    """
    Natural Numbers: Nonnegative whole numbers
    
    Args:
        offset -- nonnegative integer specifying first value returned
    """
    
    require_integers(["offset"],[offset])
    require_nonnegative(["offset"],[offset])
    
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
        a -- starting value
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
        a -- starting values
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
    require_nonnegative(["n"],[n])
    
    pw = 1
    
    while True:
        yield pw
        
        pw *= n


def power_function(e):
    """
    Power Function: Each non-negative natural raised to the same exponent
    
    Args:
        e -- exponent to raise each natural number to
    """
    
    require_integers(["e"],[e])
    require_nonnegative(["e"],[e])
    
    for n in naturals():
        yield n**e


def fermat():
    """Fermat Numbers: 2^2^n+1 for n in naturals"""
    
    for n in naturals():
        yield 2**2**n+1


### Wrappers for common cases ###
def evens():
    """Even Numbers: Non-negative integers divisible by 2"""
    
    for i in arithmetic(0,2):
        yield i


def gen_evens():
    """Even Numbers: Integers divisible by 2"""
    
    yield 0
    
    for i in arithmetic(2,2):
        yield i
        yield -i


def odds():
    """Odd Numbers: Non-negative integers not divisible by 2"""
    
    for i in arithmetic(1,2):
        yield i


def gen_odds():
    """Odd Numbers: Integers not divisible by 2"""
    
    for i in arithmetic(1,2):
        yield i
        yield -i

