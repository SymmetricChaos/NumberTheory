from Sequences.NiceErrorChecking import require_integers, require_nonnegative
from itertools import count


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
    
    for i in count(a,n):
        yield i


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
        a -- starting value for arithmetic sequence
        n -- common difference for arithmetic sequence
        b -- starting value for geometric sequence
        m -- common ratio for geometric sequence
    """
    
    require_integers(["a","n","b","m"],[a,n,b,m])
    
    for ari,geo in zip(arithmetic(a,n),geometric(b,m)):
        
        yield ari*geo


def polynomial(coef):
    """
    Polynomial Function: Integer polynomial evaluated at each non-negative integer
    
    Args:
        coef -- coefficients of the polynomial is ascending order, all integers
    """
    
    for c in coef:
        if type(c) != int:
            raise TypeError("All coefficients must be integers")
    
    for n in naturals():
        out = 0
        for e,c in enumerate(coef):
            out += c*n**e
        yield out


def fermat():
    """Fermat Numbers: 2^2^n+1 for n in naturals"""
    
    for n in naturals():
        yield 2**2**n+1


### Wrappers for common cases ###
def naturals(offset=0):
    """
    Natural Numbers: Nonnegative whole numbers, special case of arithmetic
    
    Args:
        offset -- nonnegative integer specifying first value returned
    """
    
    require_integers(["offset"],[offset])
    require_nonnegative(["offset"],[offset])
    
    for a in arithmetic(offset,1):
        yield a


def powers(n):
    """
    Powers of N: Special case of Geometric Sequence
    
    Args:
        n -- constant multiple
    """
    
    require_integers(["n"],[n])
    require_nonnegative(["n"],[n])
    
    for g in geometric(1,n):
        yield g


def evens():
    """Even Numbers: Non-negative integers divisible by 2, special case of arithmetic"""
    
    for i in arithmetic(0,2):
        yield i


def gen_evens():
    """Even Numbers: Integers divisible by 2, special case of arithmetic"""
    
    yield 0
    
    for i in arithmetic(2,2):
        yield i
        yield -i


def odds():
    """Odd Numbers: Non-negative integers not divisible by 2, special case of arithmetic"""
    
    for i in arithmetic(1,2):
        yield i


def gen_odds():
    """Odd Numbers: Integers not divisible by 2, special case of arithmetic"""
    
    for i in arithmetic(1,2):
        yield i
        yield -i





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Natural Numbers")
    simple_test(naturals(),10,
                "0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
    
    print("\nIntegers")
    simple_test(integers(),10,
                "0, 1, -1, 2, -2, 3, -3, 4, -4, 5")
    
    print("\nEvens Naturals")
    simple_test(evens(),10,
                "0, 2, 4, 6, 8, 10, 12, 14, 16, 18")
    
    print("\nEven Integers")
    simple_test(gen_evens(),10,
                "0, 2, -2, 4, -4, 6, -6, 8, -8, 10")
    
    print("\nOdd Naturals")
    simple_test(odds(),10,
                "1, 3, 5, 7, 9, 11, 13, 15, 17, 19")
    
    print("\nOdd Integers")
    simple_test(gen_odds(),10,
                "1, -1, 3, -3, 5, -5, 7, -7, 9, -9")
    
    print("\nPolynomial 2x^2 - 10x + 1")
    simple_test(polynomial([1,-10,2]),9,
                "1, -7, -11, -11, -7, 1, 13, 29, 49")
    
    print("\nArithmetic Sequence 5+2n")
    simple_test(arithmetic(5,2),10,
                "5, 7, 9, 11, 13, 15, 17, 19, 21, 23")
    
    print("\nGeometric Sequence 5*2^n")
    simple_test(geometric(5,2),8,
                "5, 10, 20, 40, 80, 160, 320, 640")
    
    
    
    
    