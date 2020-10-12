from Sequences.Simple import arithmetic
from Sequences.MathUtils import rational_to_cfrac, cfrac_convergents, cfrac_semiconvergents, homographic_convergents

from math import isqrt

# This can be sped up in the extreme case by using cycle detection
def sqrt_cfrac(n):
    """
    Terms of the simple continued fraction of the square root of n
    OEIS
    """
    
    a = a0 = isqrt(n)
    m,d = 0,1
    
    while True:
        yield a
        
        m = d*a-m
        d = (n-(m*m))//d
        a = (a0+m)//d


def sqrt_convergents(n):
    """
    Numerator then denominator of each convergent of the square root of n
    OEIS
    """
    
    yield from cfrac_convergents(sqrt_cfrac(n))


def sqrt_convergents_num(n):
    """
    Numerator then denominator of each convergent of the square root of n
    OEIS
    """
    
    for n,d in cfrac_convergents(sqrt_cfrac(n)):
        yield n


def sqrt_convergents_den(n):
    """
    Numerator then denominator of each convergent of the square root of n
    OEIS
    """
    
    for n,d in cfrac_convergents(sqrt_cfrac(n)):
        yield d


def sqrt_semiconvergents(n):
    """
    Numerator then denominator of each best rational approximation for the square root of n
    OEIS
    """
    
    yield from cfrac_convergents(sqrt_cfrac(n))



def sqrt_semiconvergents_num(n):
    """
    Numerator then denominator of each best rational approximation for the square root of n
    OEIS
    """
    
    for n,d in cfrac_semiconvergents(sqrt_cfrac(n)):
        yield n


def sqrt_semiconvergents_den(n):
    """
    Numerator then denominator of each best rational approximation for the square root of n
    OEIS
    """
    
    for n,d in cfrac_semiconvergents(sqrt_cfrac(n)):
        yield d


def e_cfrac():
    """
    Terms of the simple continued fraction of Euler's Number 
    OEIS A003417
    """
    
    M = arithmetic(2,2)
    
    yield 2
    
    while True:
        yield 1
        yield next(M)
        yield 1





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Continued Fraction for 649/200")
    simple_test(rational_to_cfrac(649,200),18,
                "3, 4, 12, 4")
    
    print("\nContinued Fraction for √2")
    simple_test(sqrt_cfrac(2),18,
                "1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2")
    
    print("\nNumerators of Continued Fraction Convergents for √2")
    simple_test(sqrt_convergents_num(2),11,
                "1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119")
    
    print("\nDenominators of Continued Fraction Convergents for √2")
    simple_test(sqrt_convergents_den(2),11,
                "1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741")
    
    print("\nContinued Fraction Convergents of Pi")
    simple_test(cfrac_convergents([3,7,15,1,292]),6,
                "(3, 1), (22, 7), (333, 106), (355, 113), (103993, 33102)")
    
    print("\nContinued Fraction Semi-Convergents of Pi")
    simple_test(cfrac_semiconvergents([3,7,15,1,292]),6,
                "(3, 1), (13, 4), (16, 5), (19, 6), (22, 7), (179, 57)")
    
    print("\nContinued Fraction for the √144")
    simple_test(sqrt_cfrac(114),16,
                "10, 1, 2, 10, 2, 1, 20, 1, 2, 10, 2, 1, 20, 1, 2, 10")
    
    print("\nContinued Fraction for Euler's Number, e")
    simple_test(e_cfrac(),17,
                "2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1")
    
    print("\nRational Convergents of (1+2e)/(1+3e)")
    simple_test(homographic_convergents(1,2,1,3,e_cfrac()),5,
                "(5, 7), (7, 10), (19, 27), (26, 37), (45, 64)")
    