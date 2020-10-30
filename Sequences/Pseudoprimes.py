from Sequences.Primes import composites

from sympy import jacobi_symbol
from math import gcd

def fermat_pseudoprimes(a):
    """
    Fermat Pseudoprimes to Base a\n
    OEIS
    """
    
    yield 1
    
    for c in composites():
        if pow(a,c-1,c) == 1:
            yield c


def weak_pseudoprimes(a):
    """
    Weak Pseudoprimes to Base a\n
    OEIS
    """
    
    yield 1
    
    for c in composites():
        if pow(a,c,c) == a:
            yield c


def strong_pseudoprimes(a):
    """
    Strong Pseudoprimes to Base a\n
    OEIS
    """
    
    for c in composites():
        if c % 2 == 1:
            d = c-1
            r = 0
            
            while d % 2 == 0:
                d //= 2
                r += 1
            
            if (a**d)%c == 1:
                yield c
                continue
            
            for e in range(0,r):
                if (a**(d*2**e))%c == c-1:
                    yield c
                    continue


def lucas_pseudoprimes(P,Q):
    
    D = P*P - 4*Q
    for c in composites():
        if c % 2 == 1:
            if gcd(c,Q) == 1:
                delta = c-jacobi_symbol(D,c)
                
                a,b = 0,1
                
                for i in range(delta):
                    a, b = b, P*b-Q*a
                
                if a % c == 0:
                    yield c


def fibonacci_pseudoprimes():
    """
    Fibonacci Pseudoprimes: Special case of Lucas Pseudoprimes 
    """
    
    for c in composites():
        if c % 2 == 1 and c % 5 != 0:
            delta = c-jacobi_symbol(5,c)
            
            a,b = 0,1
            
            for i in range(delta):
                a, b = b, b+a
            
            if a % c == 0:
                yield c



if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nFermat Pseudoprimes to Base 3")
    simple_test(fermat_pseudoprimes(3),11,
                "1, 91, 121, 286, 671, 703, 949, 1105, 1541, 1729, 1891")
    
    print("\nWeak Pseudoprimes to Base 3")
    simple_test(weak_pseudoprimes(3),12,
                "1, 6, 66, 91, 121, 286, 561, 671, 703, 726, 949, 1105")
    
    print("\nStrong Pseudoprimes to Base 3")
    simple_test(strong_pseudoprimes(3),9,
                "121, 703, 1891, 3281, 8401, 8911, 10585, 12403, 16531")
    
    # print("\n(1,-1)-Lucas Pseudoprimes")
    # simple_test(lucas_pseudoprimes(1,-1),9,
    #             "121, 703, 1891, 3281, 8401, 8911, 10585, 12403, 16531")
    
    print("\nFibonacci Pseudoprimess")
    simple_test(fibonacci_pseudoprimes(),9,
                "323, 377, 1891, 3827, 4181, 5777, 6601, 6721, 8149")
    