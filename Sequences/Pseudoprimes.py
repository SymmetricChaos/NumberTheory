from Sequences.Primes import primes
from Sequences.Divisibility import composites
from Sequences.MathUtils import factor_out_twos, coprime_to
from Sequences.NiceErrorChecking import require_integers, require_geq
from Sequences.Weird import selfridge

from sympy import jacobi_symbol
from sympy.ntheory.primetest import is_square
from math import gcd

def fermat_pseudoprimes(a):
    """
    Fermat Pseudoprimes to Base a
    
    Args:
        a -- integer greater than 1
    
    OEIS A001567, A005935-A005939
    """
    
    require_integers(["a"],[a])
    require_geq(["a"],[a],2)
    
    for c in composites():
        if pow(a,c-1,c) == 1:
            yield c


def cipolla_pseudoprimes(a):
    """
    Cipolla Pseudoprimes to Base a: A subset of Fermat pseudoprimes to the base a genereated by Cipolla's method'
    
    Args:
        a -- integer greater than 1
    
    OEIS A210454, A210461
    """
    
    A = a*(a*a-1)
    d = (a+1)*(a-1)
    
    for p in primes():
        if A % p != 0:
            yield ((a**p-1)*(a**p+1))//d


#Absurdly inefficient. Must be a better way.
def carmichael_numbers():
    """
    Charmichael Numbers: Composite numbers that are Fermat Pseudoprimes to all bases\n
    OEIS A002997
    """
    
    def all_fermat_test(n):
        B = coprime_to(n)
        for b in B:
            if pow(b,n-1,n) != 1:
                return False
        return True
    
    for c in composites():
        if all_fermat_test(c):
            yield c


def weak_pseudoprimes(a):
    """
    Weak Pseudoprimes to Base a
    
    Args:
        a -- integer greater than 1
    
    OEIS
    """
    
    require_integers(["a"],[a])
    require_geq(["a"],[a],2)
    
    yield 1
    
    for c in composites():
        if pow(a,c,c) == a:
            yield c


def strong_pseudoprimes(a):
    """
    Strong Pseudoprimes to Base a
    
    Args:
        a -- integer greater than 1
    
    OEIS
    """
    
    require_integers(["a"],[a])
    require_geq(["a"],[a],2)
    
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


def euler_pseudoprimes():
    """
    Euler Pseudoprimes
    OEIS A006970
    """
    
    for c in composites():
        if c % 2 == 1:
            if 2**((c-1)//2)%c in (1,c-1):
                yield c


def euler_jacobi_pseudoprimes():
    """
    Euler-Jacobi Pseudoprimes
    OEIS A047713
    """
    
    for c in composites():
        if c % 2 == 1:
            if 2**((c-1)//2)%c == jacobi_symbol(2,c)%c:
                yield c


def lucas_pseudoprimes(P,Q):
    """
    Lucas Pseudoprimes: Composite number passing the Lucas primality test for P and Q
    
    Args:
        P -- integer greater than zero
        Q -- integer
    
    OEIS
    """
    
    require_integers(["P","Q"],[P,Q])
    require_geq(["P"],[P],1)
    
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


# def lucas_selfridge_pseudoprimes():
#     """
#     Lucas-Selfridge Pseudoprimes: Composite number passing the Lucas primality test with P and Q chosen by Selfdrige's method\n
#     OEIS
#     """
#    
#    
#     for c in composites():
#         if c % 2 == 1:
#             P = 1
#            
#             if is_square(c):
#                 continue
#            
#             for d in selfridge():
#                 if gcd(d,c) == 1:
#                     D = d
#                     break
#            
#             Q = (1-D)//4
#            
#             delta = c-jacobi_symbol(D,c)
#            
#             if delta > lucas_pos:
#                 for i in range(delta-lucas_pos):
#                     a, b = b, P*b-Q*a
#                
#                 lucas_pos += delta-lucas_pos
#            
#             if a % c == 0:
#                 yield c


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
    OEIS 
    """
    
    yield from lucas_pseudoprimes(2,-1)


def pell_pseudoprimes_2():
    """
    Pell Pseudoprimes: Passes a version of the Pell primality test
    OEIS A099011
    """
    
    lucas_pos = 0 
    a,b = 0,1
    
    for c in composites():
        if c % 2 == 1:
            
            for i in range(c-lucas_pos):
                a, b = b, 2*b+a
            
            lucas_pos += c-lucas_pos
            
            if (a-jacobi_symbol(2,c))%c == 0:
                yield c


# Only seems to work for base 1 need anotehr reference
def strong_lucas_pseudoprimes(P,Q):
    """
    Lucas Pseudoprimes: Composite numbers passing either of two the Lucas primality tests for P and Q
    """
    
    def lucas_U_test(n,d,P,Q):
        a,b = 0,1
        for i in range(d):
            a, b = b, (P*b-Q*a)%n
        if a == 0:
            return True
        return False
    
    def lucas_V_test(n,d,s,P,Q):
        a, b = 2, P
        ctr = d
        nctr = 0
        for k in range(ctr):
            a, b = b, (P*b-Q*a)%n
            nctr += 1
        if a == 0:
            return True
        while ctr < d*(2**(s-1)):
            for k in range(ctr):
                a, b = b, (P*b-Q*a)%n
                nctr += 1
            ctr *= 2
            if a == 0:
                return True
        return False
    
    D = P*P - 4*Q
    
    for n in composites():
        if n % 2 == 0:
            continue
        
        if gcd(n,D) != 1:
            continue
        
        delta = n-jacobi_symbol(D,n)
        d,s = factor_out_twos(delta)
        
        # Check with a Lucas V-Sequence
        if lucas_U_test(n,d,P,Q):
            yield n
            continue
        
        # Check with a Lucas V-Sequence
        if lucas_V_test(n,d,s,P,Q):
            yield n





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nFermat Pseudoprimes to Base 3")
    simple_test(fermat_pseudoprimes(3),10,
                "91, 121, 286, 671, 703, 949, 1105, 1541, 1729, 1891")
    
    print("\nCipolla Pseudoprimes to Base 3")
    simple_test(cipolla_pseudoprimes(3),4,
                "7381, 597871, 3922632451, 317733228541")
    
    # print("\nCharmichael Numbers")
    # simple_test(carmichael_numbers(),9,
    #             "561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841")
    
    print("\nWeak Pseudoprimes to Base 3")
    simple_test(weak_pseudoprimes(3),12,
                "1, 6, 66, 91, 121, 286, 561, 671, 703, 726, 949, 1105")
    
    print("\nStrong Pseudoprimes to Base 3")
    simple_test(strong_pseudoprimes(3),9,
                "121, 703, 1891, 3281, 8401, 8911, 10585, 12403, 16531")
    
    print("\n(3,-1)-Lucas Pseudoprimes")
    simple_test(lucas_pseudoprimes(3,-1),9,
                "119, 169, 649, 1189, 1763, 2197, 3599, 4187, 5559")
    
    print("\nFibonacci Pseudoprimes")
    simple_test(fibonacci_pseudoprimes(),9,
                "323, 377, 1891, 3827, 4181, 5777, 6601, 6721, 8149")
    
    print("\nPell Pseudoprimes")
    simple_test(pell_pseudoprimes(),10,
                "35, 169, 385, 779, 899, 961, 1121, 1189, 2419, 2555")
    
    print("\nPell Pseudoprimes (OEIS version)")
    simple_test(pell_pseudoprimes_2(),10,
                "169, 385, 741, 961, 1121, 2001, 3827, 4879, 5719, 6215")
    
    # print("\nStrong Lucas Pseudoprimes (infinite but rare and expensive to compute)")
    # simple_test(strong_lucas_pseudoprimes(1,-1),2,
    #             "4181, 5777")
    
    # print("\nLucas-Selfridge Pseudoprimes")
    # simple_test(lucas_selfridge_pseudoprimes(),2,
    #             "4181, 5777")
    
    print("\nEuler Pseudoprimes")
    simple_test(euler_pseudoprimes(),9,
                "341, 561, 1105, 1729, 1905, 2047, 2465, 3277, 4033")
    
    print("\nEuler-Jacobi Pseudoprimes")
    simple_test(euler_jacobi_pseudoprimes(),9,
                "561, 1105, 1729, 1905, 2047, 2465, 3277, 4033, 4681")