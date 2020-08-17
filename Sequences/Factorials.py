from SequenceManipulation import offset
from Sequences.Simple import naturals
from itertools import cycle


def factorials():
    """
    Factorial Numbers: Product of the the first n positive integers\n
    OEIS A000142
    """
    
    ctr = 1
    out = 1
    
    yield out
    
    while True:
        out = out * ctr
        ctr += 1
        yield out


def alternating_factorials_1():
    """
    Alternating Factorial Numbers\n
    OEIS A005165
    """
    
    cyc = cycle([1,-1])
    F = offset(factorials(),1)
    out = 0
    
    yield 0
    
    for f,s in zip(F,cyc):
        out += f*s
        yield abs(out)


def alternating_factorials_2():
    """
    Alternating Factorial Numbers\n
    OEIS A058006
    """
    
    cyc = cycle([1,-1])
    F = factorials()
    out = 0
    
    for f,s in zip(F,cyc):
        out += f*s
        yield out


def kempner():
    """
    Kempner Numbers: smallest positive integer m such that n divides m!\n
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
    
    """
    
    even = 2
    even_ctr = 2
    
    yield 1
    
    while True:
        yield even
        
        even_ctr += 2
        even = even*even_ctr





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Factorials")
    simple_test(factorials(),8,
                "1, 1, 2, 6, 24, 120, 720, 5040")
    
    print("\nAlternating Factorials (A005165)")
    simple_test(alternating_factorials_1(),8,
                "0, 1, 1, 5, 19, 101, 619, 4421")
    
    print("\nAlternating Factorials (A058006)")
    simple_test(alternating_factorials_2(),8,
                "1, 0, 2, -4, 20, -100, 620, -4420")
    
    print("\nKempner Function")
    simple_test(kempner(),10,
                "1, 2, 3, 4, 5, 3, 7, 4, 6, 5")
    