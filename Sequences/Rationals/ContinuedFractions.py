from Sequences.Simple import arithmetic
from Sequences.Rationals.CFracUtils import convergents, semiconvergents

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


def sqrt_convergents(n,mode="f"):
    """
    Each convergent of the square root of n
    OEIS
    """
    
    yield from convergents(sqrt_cfrac(n),mode=mode)



def sqrt_semiconvergents(n,mode="f"):
    """
    Each semiconvergent (best rational approximation) of the square root of n
    OEIS
    """
    
    yield from semiconvergents(sqrt_cfrac(n),mode=mode)


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


def e_convergents(mode="f"):
    """
    Convergents of Euler's Number
    OEIS A003417
    """
    
    yield from convergents(e_cfrac(),mode=mode)


def e_semiconvergents(mode="f"):
    """
    Convergents of Euler's Number
    OEIS A003417
    """
    
    yield from semiconvergents(e_cfrac(),mode=mode)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nContinued Fraction for √2")
    simple_test(sqrt_cfrac(2),18,
                "1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2")
    
    print("\nConvergents of √2")
    simple_test(sqrt_convergents(2),8,
                "1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408")
    
    print("\nSemiconvergents of √2")
    simple_test(sqrt_semiconvergents(2),9,
                "1, 2, 3/2, 4/3, 7/5, 10/7, 17/12, 24/17, 41/29")
    
    print("\nContinued Fraction for Euler's Number, e")
    simple_test(e_cfrac(),17,
                "2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1")
    
    print("\nConvergents of e")
    simple_test(e_convergents(),9,
                "2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465")
    
    print("\nSemiconvergents of e")
    simple_test(e_convergents(),9,
                "2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465")
    