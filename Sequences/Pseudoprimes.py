from Sequences.Primes import composites
from Sequences.MathUtils import factor_out_twos

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
            
            d,r = factor_out_twos(d)
            
            if (a**d)%c == 1:
                yield c
                continue
            
            for e in range(0,r):
                if pow(a,(d*2**e),c) == c-1:
                    yield c
                    continue


def lucas_pseudoprimes(P,Q):
    """
    Lucas Pseudoprimes: Composite number passing the Lucas primality test for P and Q
    """
    
    D = P*P - 4*Q
    
    #rather than recompute we will step the sequence as needed
    lucas_pos = 0
    a,b = 0,1
    
    for c in composites():
        if c % 2 == 1:
            if gcd(c,Q) == 1:
                delta = c-jacobi_symbol(D,c)
                
                if delta > lucas_pos:
                    for i in range(delta-lucas_pos):
                        a, b = b, P*b-Q*a
                    
                    lucas_pos += delta-lucas_pos
                
                if a % c == 0:
                    yield c


def fibonacci_pseudoprimes():
    """
    Fibonacci Pseudoprimes: Special case of Lucas Pseudoprimes, also excluding multiples of 5
    OEIS A081264
    """

    lucas_pos = 0 
    a,b = 0,1
    
    for c in composites():
        if c % 2 == 1 and c % 5 != 0:
            delta = c-jacobi_symbol(5,c)
            
            if delta > lucas_pos:
                for i in range(delta-lucas_pos):
                    a, b = b, b+a
                
                lucas_pos += delta-lucas_pos
            
            if a % c == 0:
                yield c


def pell_pseudoprimes():
    """
    Pell Pseudoprimes: Special case of Lucas Pseudoprimes
    OEIS A081264
    """
    
    lucas_pos = 0 
    a,b = 0,1
    
    for c in composites():
        if c % 2 == 1:
            delta = c-jacobi_symbol(8,c)
            
            if delta > lucas_pos:
                for i in range(delta-lucas_pos):
                    a, b = b, b+a
                
                lucas_pos += delta-lucas_pos
            
            if a % c == 0:
                yield c


# def strong_lucas_pseudoprimes(P,Q):
#     """
#     Lucas Pseudoprimes: Composite number passing the Lucas primality test for P and Q
#     """
    
#     def lucas_U_test(n,d,P,Q):
#         a,b = 0,1
#         for i in range(d):
#             a, b = b, (P*b-Q*a)%c
#         if a == 0:
#             return True
#         return False
    
#     def lucas_V_test(d,s,P,Q):
#         a, b = 2, P
#         for i in range(s):
#             for k in range(d):
#                 a, b = b, P*b-Q*a
#             if a%c == 0:
#                 return True
#         return False
    
#     D = P*P - 4*Q
#     for c in composites():
#         if c % 2 == 1:
#             if gcd(c,D) == 1:
#                 delta = c-jacobi_symbol(D,c)
#                 s,d = factor_out_twos(delta)
                
#                 # Check with a Lucas U-Sequence
#                 if lucas_U_test(c,d,P,Q):
#                     yield c
#                     continue
                
#                 # Check with a Lucas V-Sequence
#                 if lucas_V_test(d,s,P,Q):
#                     yield c




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
    
    print("\n(3,-1)-Lucas Pseudoprimes")
    simple_test(lucas_pseudoprimes(3,-1),9,
                "119, 169, 649, 1189, 1763, 2197, 3599, 4187, 5559")
    
    print("\nFibonacci Pseudoprimess")
    simple_test(fibonacci_pseudoprimes(),9,
                "323, 377, 1891, 3827, 4181, 5777, 6601, 6721, 8149")
    
    # print("\nPell Pseudoprimess")
    # simple_test(pell_pseudoprimes(),9,
    #             "35, 169, 385, 779, 899, 961, 1121, 1189, 2419")
    
    # print("\nStrong Lucas Pseudoprimess")
    # simple_test(strong_lucas_pseudoprimes(1,-1),2,
    #             "323, 377, 1891, 3827, 4181, 5777, 6601, 6721, 8149")
    