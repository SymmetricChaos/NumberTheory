from Sequences.NiceErrorChecking import require_integers, require_geq
from Sequences.Manipulations import make_triangle

from itertools import count, repeat


def constant(n):
    """
    Constant Sequences: Returns n forever
    OEIS A000004, A000012, A007395, A010701
    """
    
    require_integers(["n"],[n])
    
    yield from repeat(n)


def integers():
    """
    Integers: All integers starting with zero then with positive before negative\n
    OEIS A001057
    """
    
    yield 0
    
    for n in count(1):
        yield n
        yield -n


def arithmetic(a,n):
    """
    Arithmetic Sequences: Integers with constant difference
    
    Args:
        a -- starting value
        n -- common difference
    
    OEIS
    """
    
    require_integers(["a","n"],[a,n])
    
    yield from count(a,n)


def geometric(a,n):
    """
    Geometric Sequences: Integers with constant ratio
    
    Args:
        a -- starting values
        n -- common ratio
    
    OEIS
    """
    
    require_integers(["a","n"],[a,n])
        
    out = a
    
    while True:
        yield out
        
        out *= n


def arithmetrico_geometric(a,n,b,m):
    """
    Arithmetrico-Geometric Sequences: Product of an arithmetic sequence with a geometric sequence
    
    Args:
        a -- starting value for arithmetic sequence
        n -- common difference for arithmetic sequence
        b -- starting value for geometric sequence
        m -- common ratio for geometric sequence
    
    OEIS
    """
    
    require_integers(["a","n","b","m"],[a,n,b,m])
    
    for ari,geo in zip(arithmetic(a,n),geometric(b,m)):
        yield ari*geo


def polynomial(coef):
    """
    Polynomial Functions: Integer polynomial evaluated at each non-negative integer
    
    Args:
        coef -- coefficients of the polynomial is ascending order, all integers
    
    OEIS
    """
    
    for c in coef:
        if type(c) != int:
            raise TypeError("All coefficients must be integers")
    
    for n in naturals():
        out = 0
        
        for e,c in enumerate(coef):
            out += c*n**e
        
        yield out


def gen_polynomial(coef):
    """
    Polynomial Functions: Integer polynomial evaluated at each integer
    
    Args:
        coef -- coefficients of the polynomial is ascending order, all integers
    
    OEIS
    """
    
    for c in coef:
        if type(c) != int:
            raise TypeError("All coefficients must be integers")
    
    for i in integers():
        out = 0
        
        for e,c in enumerate(coef):
            out += c*i**e
        
        yield out


def fermat():
    """
    Fermat Numbers: 2^2^n+1 for n in naturals\n
    OEIS A000215
    """
    
    for n in naturals():
        yield 2**2**n+1


def sign_sequence(n=1):
    """
    Sequence of +n and -n repeated forever\n
    OEIS A033999
    """
    
    require_integers(["n"],[n])
    
    while True:
        yield n
        yield -n


def floyd_triangle(flatten=False):
    """
    Floyd's Triangle
    """
    
    if flatten:
        yield from count(1,1)
    else:
        yield from make_triangle(count(1,1))


def magic_square():
    """
    The Magic Square Constant for each Natural
    OEIS A006003
    """
    
    for i in floyd_triangle():
        yield sum(i)





### Wrappers or more efficient versions of common cases ###
def naturals(offset=0):
    """
    Natural Numbers: Nonnegative whole numbers, special case of arithmetic
    
     Args:
        offset -- nonnegative integer how many naturals to skip before starting
        
    OEIS A001477
    """
    
    require_integers(["offset"],[offset])
    require_geq(["offset"],[offset],0)
    
    yield from count(offset,1)


def counting(offset=0):
    """
    Counting Numbers: Positive whole numbers, special case of arithmetic
    
    Args:
        offset -- nonnegative integer how many counting numbers to skip before starting
        
    OEIS A000027
    """
    
    require_integers(["offset"],[offset])
    require_geq(["offset"],[offset],0)
    
    yield from count(offset+1,1)


def powers(n):
    """
    Powers of n: Special case of geometric
    
    Args:
        n -- constant multiple
        
    OEIS A000079, A000244, A000302, A000351, A000400, A000420, A001018-A001027, 
         A001029, A009964-A009992, A011557, A159991, A165800
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],0)
    
    yield from geometric(1,n)


def self_powers():
    """
    Self Powers: Each non-negative integer raised to the power of itself\n
    OEIS A000312
    """
    
    for n in naturals():
        yield n**n


def evens():
    """
    Even Numbers: Non-negative integers divisible by 2, special case of arithmetic\n
    OEIS A005843
    """
    
    yield from arithmetic(0,2)


def gen_evens():
    """
    Even Numbers: Integers divisible by 2, special case of arithmetic\n
    OEIS A137501 (differs by including zero only once)
    """
    
    yield 0
    
    for i in arithmetic(2,2):
        yield i
        yield -i


def odds():
    """
    Odd Numbers: Non-negative integers not divisible by 2, special case of arithmetic\n
    OEIS A005408
    """
    
    yield from arithmetic(1,2)


def gen_odds():
    """
    Odd Numbers: Integers not divisible by 2, special case of arithmetic\n
    OEIS A296063
    """
    
    for i in arithmetic(1,2):
        yield i
        yield -i





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Counting Numbers")
    simple_test(counting(),16,
                "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16")
    
    print("\nNatural Numbers")
    simple_test(naturals(),16,
                "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15")
    
    print("\nIntegers")
    simple_test(integers(),16,
                "0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8")
    
    print("\nEven Naturals")
    simple_test(evens(),15,
                "0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28")
    
    print("\nEven Integers")
    simple_test(gen_evens(),14,
                "0, 2, -2, 4, -4, 6, -6, 8, -8, 10, -10, 12, -12, 14")
    
    print("\nOdd Naturals")
    simple_test(odds(),15,
                "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29")
    
    print("\nOdd Integers")
    simple_test(gen_odds(),14,
                "1, -1, 3, -3, 5, -5, 7, -7, 9, -9, 11, -11, 13, -13")
    
    print("\nPolynomial 2x^2 - 10x + 1 Evaluated at Naturals")
    simple_test(polynomial([1,-10,2]),13,
                "1, -7, -11, -11, -7, 1, 13, 29, 49, 73, 101, 133, 169")
    
    print("\nPolynomial 2x^2 - 10x + 1 Evaluated at Integers")
    simple_test(gen_polynomial([1,-10,2]),13,
                "1, -7, 13, -11, 29, -11, 49, -7, 73, 1, 101, 13, 133")
    
    print("\nArithmetic Sequence 5+2n")
    simple_test(arithmetic(5,2),14,
                "5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31")
    
    print("\nGeometric Sequence 5*2^n")
    simple_test(geometric(5,2),11,
                "5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120")
    
    print("\nArithmetrico-Geometric Sequence (1+2n)(3*4^n)")
    simple_test(arithmetrico_geometric(1,2,3,4),9,
                "3, 36, 240, 1344, 6912, 33792, 159744, 737280, 3342336")
    
    print("\nPowers of 3")
    simple_test(powers(3),11,
                "1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049")
    
    print("\nFermat Numbers")
    simple_test(fermat(),7,
                "3, 5, 17, 257, 65537, 4294967297, 18446744073709551617")
    
    print("\nThe Zero Sequence")
    simple_test(constant(0), 18,
                "0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0")
    
    print("\nSelf Powers")
    simple_test(self_powers(), 9,
                "1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216")
    
    print("\nThe (1,-1) Sign Sequence")
    simple_test(sign_sequence(1), 16,
                "1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1")
    
    print("\nFloyd's Triangle")
    simple_test(floyd_triangle(), 4,
                "(1,), (2, 3), (4, 5, 6), (7, 8, 9, 10)")
    
    print("\nMagic Square Constants")
    simple_test(magic_square(), 12,
                "1, 5, 15, 34, 65, 111, 175, 260, 369, 505, 671, 870")
    