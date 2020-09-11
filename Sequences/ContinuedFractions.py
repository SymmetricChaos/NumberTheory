from math import isqrt
from Sequences.Simple import arithmetic

def cfrac(n,d):
    """
    Terms of the simple continued fraction representation of n/d
    """
    
    while d != 0:
        i = n//d
        yield i
        
        n,d = d,n-(d*i)


def cfrac_convergents(S):
    """
    Convergents of the simple continued fraction representation of n/d
    """
    
    n0,n1 = 0,1
    d0,d1 = 1,0
    
    for c in S:
        n0,n1 = n1,c*n1 + n0
        d0,d1 = d1,c*d1 + d0
        
        yield n1
        yield d1


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


# def pi_continued_fraction():





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Continued Fraction for 649/200")
    simple_test(cfrac(649,200),18,
                "3, 4, 12, 4")
    
    print("\nContinued Fraction Convergents for √2")
    simple_test(cfrac_convergents(sqrt_cfrac(2)),14,
                "1, 1, 3, 2, 7, 5, 17, 12, 41, 29, 99, 70, 239, 169")
    
    print("\nContinued Fraction for the √144")
    simple_test(sqrt_cfrac(114),16,
                "10, 1, 2, 10, 2, 1, 20, 1, 2, 10, 2, 1, 20, 1, 2, 10")
    
    print("\nContinued Fraction for Euler's Number")
    simple_test(e_cfrac(),17,
                "2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1")
    