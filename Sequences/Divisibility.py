from Sequences.NiceErrorChecking import require_integers, require_geq, require_prime
from Sequences.Primes import primes, blum_primes
from Sequences.Simple import naturals
from Sequences.MathUtils import factors, prime_factorization, unique_prime_factors, \
                                jordan_totient, multi_lcm, prime_power_factorization, \
                                nth_sign
from Sequences.Manipulations import partial_sums

from collections import defaultdict
from math import prod, gcd
from itertools import takewhile, cycle
from sympy.ntheory.factor_ import core
from sympy import legendre_symbol

def smooth(B):
    """
    Smooth Numbers: Positive integers with no prime factors greater than B
    
    OEIS A003586, A051037, A002473, A051038, A080197, A080681, A080682, A080683
    
    Args:
        B -- largest prime factor allowed
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],1)
    
    P = [p for p in takewhile(lambda x: x <= B,primes())]
    
    for n in naturals(1):
        out = n
        
        for f in P:
            while n % f == 0:
                n = n // f
            
            if n == 1:
                yield out
                break


def hamming():
    """
    Hamming Numbers: The 5-Smooth numbers also known as the Regular Numbers\n
    OEIS A051037
    """
    
    yield from smooth(5)


def rough(B):
    """
    Rough Numbers: Positive integers with no prime factors less than B
    
    Args:
        B -- smallest prime factor allowed
    
    OEIS A000027, A005408, A007310, A007775, A008364, A008365, A008366, A166061, A166063
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],1)
    
    P = [p for p in takewhile(lambda x: x < B,primes())]
    
    for n in naturals(1):
        confirm = True
        
        for f in P:
            if n % f == 0:
                confirm = False
                break
        
        if confirm:
            yield n


def highly_composite():
    """
    Highly Composite Numbers: Positive integers that have more factors than any smaller positive integer\n
    OEIS A002182
    """
    
    F = 0
    
    for i in naturals(1):
        L = len(factors(i))
        
        if L > F:
            F = L
            yield i


def highly_composite_factor():
    """
    Factors of each Highly Composite Number\n
    OEIS 
    """
    
    F = 0
    
    for i in naturals(1):
        L = len(factors(i))
        
        if L > F:
            F = L
            yield F


def highly_composite_prime_factor():
    """
    Prime Factors (with multiplicity) of each Highly Composite Number\n
    OEIS A112778
    """
    
    for h in highly_composite():
        yield len(prime_factorization(h))


def divisors():
    """
    Number of Divisors: Count of divisors for each positive integer\n
    OEIS A000005
    """
    
    for i in naturals(1):
        yield len(factors(i))


def all_divisors():
    """
    Irregular Array with Divisors of Every Positive Integer\n
    OEIS A027750
    """
    
    for i in naturals(1):
        yield from factors(i)


def prime_divisors():
    """
    Number of Prime Divisors with Multiplicity: Length of prime factorization for each positive integer
    Also the big omega function\n
    OEIS A001222
    """
    
    D = defaultdict(list)
    
    yield 0
    
    for q in naturals(2):
        if q not in D:
            yield 1
            D[q + q] = [q]
        
        else:
            q_copy = q
            ctr = 0
            
            for fac in D[q]:
                while q_copy % fac == 0:
                    ctr += 1
                    q_copy //= fac
            
            yield ctr
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]


def unique_prime_divisors():
    """
    Number of Unique Prime Divisors: Count of unique prime factors for positive n
    Also the little omega function\n
    OEIS A001221
    """
    
    D = defaultdict(list)
    
    yield 0
    
    for q in naturals(2):
        if q not in D:
            yield 1
            D[q + q] = [q]
        
        else:
            yield len(D[q])
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]


def squarefree():
    """
    Squarefree Numbers: Positive integers not divisible by any prime more than once\n
    OEIS A005117
    """
    
    for n in naturals(1):
        for i in naturals(2):
            if n % i**2 == 0:
                break
            
            if (i**2) > n:
                yield n
                break


def squarefree_kernel():
    """
    Squarefree Kernels: Largest squarefree factor of positive n\n
    OEIS A007947
    """
    
    D = defaultdict(list)
    
    yield 1
    
    for q in naturals(2):
        if q not in D:
            yield q
            
            D[q + q] = [q]
        
        else:
            yield prod(D[q])
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]


def squarefree_core():
    """
    Squarefree Core: Smallest integer m such that n/m is square for positive n\n
    OEIS A007913
    """
    
    for n in naturals(1):
        yield core(n,2)


def powerfree_core(p=2):
    """
    Powerfree Core: Smallest integer m such that n/m is a perfect pth power for positive n\n
    
    Args:
        p -- power
    
    OEIS
    """
    
    require_integers(["p"],[p])
    require_geq(["p"],[p],2)
    
    for n in naturals(1):
        yield core(n,p)


def powerful(n=2):
    """
    n-Powerful Numbers: Positive integers that are divisible by the nth power of each prime factor
    
    Args:
        n -- power
    
    
    OEIS A001694
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],2)
    
    def is_n_powerful(a,n):
        U = unique_prime_factors(a)
        for u in U:
            if a % (u**n) != 0:
                return False
        return True
    
    yield 1
    
    for m in naturals(4):
        if is_n_powerful(m,n):
            yield m


def totients():
    """
    Totients: Count of positive integers coprime to each positive integer\n
    OEIS A000010
    """
    
    D = defaultdict(list)
    
    yield 1
    
    for q in naturals(2):
        if q not in D:
            yield q-1
            D[q + q] = [q]
        
        else:
            n,d = 1,1
            
            for p in D[q]:
                D[p+q].append(p)
                
                n *= (p-1)
                d *= p
            
            yield q*n//d
            
            del D[q]


def cototients():
    """
    Cotients: Count of positive integers not coprime to each positive integer\n
    OEIS A051953
    """
    
    for n,t in enumerate(totients(),1):
        yield n-t


# def nontotients():


# def even_nontotients():


# def noncototient():


# def sparsely_totient():


def charmichael():
    """
    Charmichael Function: LCM of the orders of the elements of the finite multiplictive group on n\n
    OEIS A002322
    """
    
    yield 1
    
    def charm(n):
        if n > 4 and n%2 == 0:
            return jordan_totient(n)//2
        return jordan_totient(n)
    
    for n in naturals(2):
        T = [charm(p) for p in prime_power_factorization(n)]
        
        yield multi_lcm(T)


def jordan_totients(k):
    """
    Jordan's k-Totient Function
    
    Args:
        k -- power that denominator is raised to
    
    OEIS A007434, A059376, A059377, A059378, A069091-A069095
    """
    
    for n in naturals(1):
        yield jordan_totient(n,k)


def coprimes(n):
    """
    All positive integers coprime to n
    
    Args:
        n -- an integer greater than 0
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    F = unique_prime_factors(n)
    
    # Check if any of the factors of n divide a
    def divby(a,F):
        for f in F:
            if a%f == 0:
                return False
        return True
    
    for x in naturals(1):
        if divby(x,F):
            yield x


def coprime_characteristic():
    """
    Triangle of coprime pairs: 1 if the pair is coprimes and 0 if not\n
    OEIS A054521
    """
    
    for m in naturals(1):
        for n in range(1,m+1):
            if gcd(m,n) == 1:
                yield 1
            else:
                yield 0


def principal_character(n):
    """
    Principal Dirichlet Character: For each positive integer yield 1 of it is coprime to n otherwise 0
    
    Args:
        n -- an integer greater than 0
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    L = []
    
    for a in range(1,11):
        if gcd(a,n) == 1:
            L.append(1)
        else:
            L.append(0)
    
    yield from cycle(L)


def p_adic_order(p):
    """
    p-adic Orders: Exponent of the greatest power of p that divides each positive integer\n
    
    Args:
        p -- a prime
    
    OEIS A007814, A007949, A235127, A112765
    """
    
    require_integers(["p"],[p])
    require_prime(["p"],[p])
    
    for n in naturals(1):
        ctr = 0
        
        while n%p == 0:
            ctr += 1
            n //= p
        
        yield ctr


def n_adic_order(n):
    """
    n-adic Orders: Exponent of the greatest power of n that divides each positive integer
    Identical to p_adic_order but allowing nonprime inputs
    
    Args:
        n -- an integer greater than zero
    
    OEIS A007814, A007949, A235127, A112765
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    for i in naturals(1):
        ctr = 0
        
        while i%n == 0:
            ctr += 1
            i //= n
        
        yield ctr


def liouville():
    """
    Liouville's Lambda Function: 1 if n is a product of an even number of primes, otherwise -1\n
    OEIS A008836
    """
    
    yield 1
    
    for n in naturals(2):
        P = prime_factorization(n)
        yield nth_sign(len(P))


def liouville_sums():
    """
    Liouville's L Function: Partial sums of Liouville's Lambda Function\n
    OEIS A002819
    """
    
    yield from partial_sums(liouville())


def semiprimes():
    """
    The Semiprimes: Positive integers that are the product of exactly two primes\n
    OEIS A001358
    """
    
    for n in naturals(1):
        if len(prime_factorization(n)) == 2:
            yield n


def almost_primes(n):
    """
    The Almost Prime Numbers: Positive integers that are the product of exactly n primes\n
    OEIS A000040, A001358, A014612, A014613, A014614, A046306, A046308, A046310, 
         A046312, A046314, A069276-A069281
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    for i in naturals(1):
        if len(prime_factorization(i)) == n:
            yield i


def blum():
    """
    The Blum Integers: Integers that are the product of distinct primes both congruent to 3 mod 4
    OEIS A016105
    """
    
    for n in naturals(1):
        P = prime_factorization(n)
        
        if len(P) == 2:
            if P[0] == P[1]:
                continue
            
            if P[0]%4 == 3 and P[1]%4 == 3:
                yield n


def blum_blum_shub_integers():
    """
    Integers that maximize the period of the Blum-Blum-Shub PRNG
    """
    
    P = blum_primes()
    
    S = []
    K = {}
    T = []
    
    for s in P:
        S.append(s)
        K[s] = legendre_symbol(2,(s-1)//2)
        
        while len(T) > 0 and T[0] < s*S[0]:
            yield T.pop(0)
        
        for t in S[:-1]:
            if K[t] + K[s] != 2:
                T.append(t*s)
        
        T.sort()

# Version of above for OEIS designed to print the first N numbers and also
# include a generator for the relevant primes
# from sympy.ntheory import , isprime, sieve
# def BBSI(N):
#     def BBS_primes():
#         p = 1
#         S = sieve
#         while True:
#             p += 1
#             if p in S:
#                 if p%4 == 3:
#                     a = (p-1)//2
#                     b = (a-1)//2
#                     if a%2 == 1 and b % 2 == 1:
#                         if isprime(a) and isprime(b):
#                             yield p
#     S = []
#     K = {}
#     T = []
#     ctr = 0
#     for s in BBS_primes():
#         S.append(s)
#         K[s] = legendre_symbol(2,(s-1)//2)
#         while len(T) > 0 and T[0] < s*S[0]:
#             print(T.pop(0))
#             ctr += 1
#             if ctr >= N:
#                 return None
#         for t in S[:-1]:
#             if K[t] + K[s] != 2:
#                 T.append(t*s)
#         T.sort()


def odd_parts():
    """
    The odd part of each positive integer\n
    OEIS A000265
    """
    
    for n in naturals(1):
        while n % 2 == 0:
            n //= 2
        yield n





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nTotient Numbers")
    simple_test(totients(),17,
                "1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16")
    
    print("\nCototient Numbers")
    simple_test(cototients(),18,
                "0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, 1, 8, 7, 8, 1, 12")
    
    print("\n5-Smooth (Hamming)")
    simple_test(smooth(5),16,
                "1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25")
    
    print("\n5-Rough")
    simple_test(rough(5),14,
                "1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41")
    
    print("\nHighly Composite")
    simple_test(highly_composite(),13,
                "1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360")
    
    print("\nNumber of Divisors")
    simple_test(divisors(),18,
                "1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6")
    
    print("\nNumber of Prime Divisors (with multiplicity)")
    simple_test(prime_divisors(),18,
                "0, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 3, 1, 2, 2, 4, 1, 3")
    
    print("\nNumber of Unique Prime Divisors")
    simple_test(unique_prime_divisors(),18,
                "0, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2")
    
    print("\nSquarefree Numbers")
    simple_test(squarefree(),15,
                "1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22")
    
    print("\nSquarefree Kernels")
    simple_test(squarefree_kernel(),16,
                "1, 2, 3, 2, 5, 6, 7, 2, 3, 10, 11, 6, 13, 14, 15, 2")
    
    print("\nCharacteristic Triangle of Coprimes")
    simple_test(coprime_characteristic(),18,
                "1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0")
    
    print("\nNaturals Coprime to 24")
    simple_test(coprimes(24),14,
                "1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41")
    
    print("\nPowerful Numbers")
    simple_test(powerful(),14,
                "1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81, 100")
    
    print("\n3-Powerful Numbers")
    simple_test(powerful(3),13,
                "1, 8, 16, 27, 32, 64, 81, 125, 128, 216, 243, 256, 343")
    
    print("\nCount of Factors for each Highly Composite Number")
    simple_test(highly_composite_factor(),15,
                "1, 2, 3, 4, 6, 8, 9, 10, 12, 16, 18, 20, 24, 30, 32")
    
    print("\nCount of Prime Factors (with multiplicity) for each Highly Composite Number")
    simple_test(highly_composite_prime_factor(),18,
                "0, 1, 2, 2, 3, 4, 4, 5, 4, 5, 5, 6, 6, 7, 6, 6, 7, 7")
    
    print("\nJordan 2-Totients")
    simple_test(jordan_totients(2),13,
                "1, 3, 8, 12, 24, 24, 48, 48, 72, 72, 120, 96, 168")
    
    print("\nCharmichael Function")
    simple_test(charmichael(),17,
                "1, 1, 2, 2, 4, 2, 6, 2, 6, 4, 10, 2, 12, 6, 4, 4, 16")
    
    print("\n3-adic Orders")
    simple_test(p_adic_order(3),18,
                "0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 2")
    
    print("\nLiouville's Lambda Function")
    simple_test(liouville(),15,
                "1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1")
    
    print("\nLiouville's L Function")
    simple_test(liouville_sums(),15,
                "1, 0, -1, 0, -1, 0, -1, -2, -1, 0, -1, -2, -3, -2, -1")
    
    print("\nPricipal Character of 10")
    simple_test(principal_character(10),18,
                "1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0")
    
    print("\nSemiprimes")
    simple_test(semiprimes(),14,
                "4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38")
    
    print("\nTriprimes")
    simple_test(almost_primes(3),14,
                "8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66")
    
    print("\nBlum Integers")
    simple_test(blum(),12,
                "21, 33, 57, 69, 77, 93, 129, 133, 141, 161, 177, 201")
    
    print("\nBlum-Blum-Shub Integers")
    simple_test(blum_blum_shub_integers(),8,
                "1081, 3841, 7849, 8257, 16537, 16873, 33097, 46897")
    
    print("\nArray of All Divisors")
    simple_test(all_divisors(),18,
                "1, 1, 2, 1, 3, 1, 2, 4, 1, 5, 1, 2, 3, 6, 1, 7, 1, 2")
    
    print("\nOdd Parts")
    simple_test(odd_parts(),17,
                "1, 1, 3, 1, 5, 3, 7, 1, 9, 5, 11, 3, 13, 7, 15, 1, 17")
    