from Sequences.Manipulations import offset, make_triangle
from Sequences.Simple import naturals, sign_sequence
from Sequences.MathUtils import poly_mult
from Sequences.Divisibility import primes

from itertools import cycle

def factorials():
    """
    Factorial Numbers: Product of the the first n positive integers\n
    OEIS A000142
    """
    
    out = 1
    
    yield out
    
    for n in naturals(1):
        out = out * n
        yield out


def superfactorials():
    """
    Superfactorials: Partial products of the factorials\n
    OEIS A000178
    """
    
    out = 1
    
    for f in factorials():
        out *= f
        yield out


def left_factorials():
    """
    Left Factorials: Partial sums of the factorials
    OEIS A003422
    """
    out = 0
    
    for f in factorials():
        yield out
        out += f


def alternating_factorials_1():
    """
    Alternating Factorial Numbers: Absolute value of each term\n
    OEIS A005165
    """
    
    cyc = sign_sequence(1)
    F = offset(factorials(),1)
    out = 0
    
    for f,s in zip(F,cyc):
        yield abs(out)
        out += f*s


def alternating_factorials_2():
    """
    Alternating Factorial Numbers: Integer value of each term\n
    OEIS A058006
    """
    
    cyc = sign_sequence(1)
    F = factorials()
    out = 0
    
    for f,s in zip(F,cyc):
        out += f*s
        yield out


def kempner():
    """
    Kempner Numbers: Smallest positive integer m such that n divides m!\n
    OEIS A002034
    """
    
    yield 1
    
    for n in naturals(2):
        for i,f in enumerate(factorials()):
            if f%n == 0:
                yield i
                break


def double_factorials():
    """
    Double Factorials: Double factorial of each non-negative integer\n
    OEIS A006882
    """
    
    odd = 1
    even = 2
    
    odd_ctr = 1
    even_ctr = 2
    
    yield 1
    
    while True:
        yield odd
        yield even
        
        odd_ctr += 2
        even_ctr += 2
        
        odd = odd*odd_ctr
        even = even*even_ctr


def odd_double_factorials():
    """
    Odd Double Factorials: Double factorial of each odd non-negative integer\n
    OEIS A001147
    """
    
    odd = 1
    odd_ctr = 1
    
    while True:
        yield odd
        
        odd_ctr += 2
        odd = odd*odd_ctr


def even_double_factorials():
    """
    Even Double Factorials: Double factorial of each even non-negative integer\n
    OEIS A000165
    """
    
    even = 2
    even_ctr = 2
    
    yield 1
    
    while True:
        yield even
        
        even_ctr += 2
        even = even*even_ctr


def rising_factorial():
    """
    Coefficients of the Polynomial Expansions of the Rising Factorials\n
    OEIS A132393
    """
    
    P = [1]
    
    for n in naturals(0):
        for i in P:
            yield i
        
        P = poly_mult(P,[n,1])


def rising_factorial_triangle():
    """
    Triangle of Coefficients of the Polynomial Expansions of the Rising Factorials\n
    OEIS A132393
    """
    
    yield from make_triangle(rising_factorial())


def falling_factorial():
    """
    Coefficients of the Polynomial Expansions of the Falling Factorials\n
    OEIS A048994
    """
    P = [1]
    
    for n in naturals(0):
        for i in P:
            yield i
        
        P = poly_mult(P,[-n,1])


def falling_factorial_triangle():
    """
    Triangle of Coefficients of the Polynomial Expansions of the Falling Factorials\n
    OEIS A132393
    """
    
    yield from make_triangle(falling_factorial())


def wilson():
    """
    Wilson's Sequence: (n-1)! % n, for primes p-1, otherwise 0 except at four where it equals 2\n
    OEIS A061006
    """
    
    yield 0
    yield 1
    yield 2
    yield 2
    
    oldp = 5
    for p in offset(primes(),2):
        for i in range(p-oldp-1):
            yield 0
        
        yield p-1
        oldp = p


def factoradic(full=False):
    """
    Factoradic Number System: The integers written in the factorial base, returns tuples
    
    Args:
        full -- bool, if True appends 0 to the end of the tuple to give the full factoradic number
    
    OEIS A007623
    """
    
    # The maxiumim digit value in the factoradic system goes up by one each place
    max_val = 1
    
    # Counting up the digits of the factoradic numbers cycle at slower and slower paces
    # The lowest place goes 0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1
    # The next place goes   0,0,1,1,2,2,0,0,1,1,2,2,0,0,1,1,2,2,0,0,1,1,2,2
    # The next place goes   0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3
    # We will generate the factoradics using this pattern and the cycle() function
    cycle_len = 1
    cycles = [cycle([1,0])]
    
    yield (0,)
    ctr = 0
    
    while True:
        ctr += 1
        N = []
        
        for n in reversed(cycles):
            N.append(next(n))
        
        if ctr == cycle_len*max_val:
            ctr = 0
            max_val += 1
            cycle_len *= max_val
            
            L = []
            for i in range(1,max_val+1):
                L += [i]*cycle_len
            L += [0]*cycle_len
            
            cycles.append(cycle(L))
        
        if full:
            N.append(0)
        
        yield tuple(N)


def factorial_chain_length():
    """
    Smallest number of factorials needed to sum to n
    """
    
    for i in factoradic():
        yield sum(i)


def triple_factorial():
    """
    Triple Factorial: Version of 
    OEIS A007661
    """
    
    a,b,c = 1,1,2
    
    for n in naturals(3):
        yield n*a
        a,b,c = b,c,n*a





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Factorials")
    simple_test(factorials(),11,
                "1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800")
    
    print("\nAlternating Factorials (A005165)")
    simple_test(alternating_factorials_1(),11,
                "0, 1, 1, 5, 19, 101, 619, 4421, 35899, 326981, 3301819")
    
    print("\nAlternating Factorials (A058006)")
    simple_test(alternating_factorials_2(),10,
                "1, 0, 2, -4, 20, -100, 620, -4420, 35900, -326980")
    
    print("\nKempner Function")
    simple_test(kempner(),17,
                "1, 2, 3, 4, 5, 3, 7, 4, 6, 5, 11, 4, 13, 7, 5, 6, 17")
    
    print("\nDouble Factorials")
    simple_test(double_factorials(),12,
                "1, 1, 2, 3, 8, 15, 48, 105, 384, 945, 3840, 10395")
    
    print("\nOdd Double Factorials")
    simple_test(odd_double_factorials(),9,
                "1, 3, 15, 105, 945, 10395, 135135, 2027025, 34459425")
    
    print("\nEven Double Factorials")
    simple_test(even_double_factorials(),9,
                "1, 2, 8, 48, 384, 3840, 46080, 645120, 10321920")
    
    print("\nRising Factorials")
    simple_test(rising_factorial(),17,
                "1, 0, 1, 0, 1, 1, 0, 2, 3, 1, 0, 6, 11, 6, 1, 0, 24")
    
    print("\nTriangle of Rising Factorials")
    simple_test(rising_factorial_triangle(),4,
                "(1,), (0, 1), (0, 1, 1), (0, 2, 3, 1)")
    
    print("\nFalling Factorials")
    simple_test(falling_factorial(),16,
                "1, 0, 1, 0, -1, 1, 0, 2, -3, 1, 0, -6, 11, -6, 1, 0")
    
    print("\nTriangle of Rising Factorials")
    simple_test(falling_factorial_triangle(),4,
                "(1,), (0, 1), (0, -1, 1), (0, 2, -3, 1)")
    
    print("\nWilson's Sequence")
    simple_test(wilson(),17,
                "0, 1, 2, 2, 4, 0, 6, 0, 0, 0, 10, 0, 12, 0, 0, 0, 16")
    
    print("\nSuperfactorials")
    simple_test(superfactorials(),8,
                "1, 1, 2, 12, 288, 34560, 24883200, 125411328000")
    
    print("\nLeft Factorials")
    simple_test(left_factorials(),11,
                "0, 1, 2, 4, 10, 34, 154, 874, 5914, 46234, 409114")
    
    print("\nFactoradic Integers")
    simple_test(factoradic(),7,
                "(0,), (1,), (1, 0), (1, 1), (2, 0), (2, 1), (1, 0, 0)")
    
    print("\nMinimum Number of Factorials Needed to Sum to n")
    simple_test(factorial_chain_length(),18,
                "0, 1, 1, 2, 2, 3, 1, 2, 2, 3, 3, 4, 2, 3, 3, 4, 4, 5")
    
    print("\nTriple Factorial")
    simple_test(triple_factorial(),12,
                "3, 4, 10, 18, 28, 80, 162, 280, 880, 1944, 3640, 12320")
    