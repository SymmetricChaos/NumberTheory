from Sequences.Simple import naturals, arithmetic
from Sequences.Manipulations import partial_prods, prepend, hypersequence, differences, offset
from Sequences.NiceErrorChecking import require_integers, require_geq, require_iterable

from collections import defaultdict
from sympy import sieve, isprime
from math import prod

##############################
## CLASSES OF PRIME NUMBERS ##
##############################

def primes():
    """
    Prime Numbers: Positive integers with exactly two factors\n
    OEIS A000040
    """
    
    upper = 2
    while True:
        upper *= 2
        yield from sieve.primerange(upper//2, upper)


def odd_primes():
    """
    Odd Primes: Primes that are odd positive integer\n
    OEIS A065091
    """
    
    yield from offset(primes(),1)


def twin_primes():
    """
    Twin Primes: Primes that are two more or less than another prime\n
    OEIS A001097
    """
    
    P = primes()
    
    a,b,c = next(P),next(P),next(P)
    
    while True:
        if b-2 == a or b+2 == c:
            yield b
        a,b,c = b,c,next(P)


def twin_prime_pairs():
    """
    Twin Prime Pairs: Primes that are two more or less than another prime\n
    OEIS A077800
    """
    
    P = primes()
    
    a,b = next(P),next(P)
    
    while True:
        if a+2 == b:
            yield (a,b)
        a,b = b,next(P)


def n_gap_prime_pairs(n):
    """
    Pairs of primes (p,q) such that p+n = q\n
    OEIS A077800, A156274, A156320, A140445, A156323, A140446, A272815, 
         A156328, A272816, A140447
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    if n % 2 == 1:
        raise ValueError("n must be even, for odd n either there is no pair or the only pair is (2,2+n)")
    
    else:
        P = primes()
        lo = next(P)
        hi = [next(P)]
        
        while True:
            while hi[-1] < lo+n:
                hi.append(next(P))
            
            if lo+n in hi:
                yield (lo,lo+n)
            
            lo = hi.pop(0)


def prime_tuples(K):
    """
    Tuples of primes (p,q,r...) with gaps specified by K\n
    OEIS
    """
    
    for gap in K:
        if gap % 2 != 0:
            raise ValueError("gaps must be even, the only odd gaps are between 2 and another prime")
    
    P = primes()
    L = []
    
    def all_gaps(K,L):
        T = tuple([L[0]+k for k in K])
        for t in T:
            if t not in L:
                return ()
        return T
    
    while True:
        while len(L) <= len(K):
            L.append(next(P))
        
        while L[-1] <= L[0]+(max(K)):
            L.append(next(P))
        
        T = all_gaps(K,L)
        if T:
            yield T
        
        L = L[1:]


def superprimes():
    """
    Prime Indexed Primes: The pth primes for p in primes\n
    OEIS A006450
    """
    
    yield from hypersequence(primes())


def sophie_germain_primes():
    """
    Sophie Germain Primes: Primes such that 2p+1 is prime\n
    OEIS A005384
    """
    
    S = set([2])
    
    for p in odd_primes():
        S.add(p)
        if (p-1)//2 in S:
            yield (p-1)//2
        
        S = {s for s in S if s > (p-1)//2}


def safe_primes():
    """
    Safe Primes: Primes such that (p-1)/2 is prime\n
    OEIS A005385
    """
    
    S = set([2])
    
    for p in odd_primes():
        S.add(p)
        if (p-1)//2 in S:
            yield p
        
        S = {s for s in S if s > (p-1)//2}


def pythagorean_primes():
    """
    Pythagorean Primes: Primes that can be the hypotenuse of an integer right triangle\n
    OEIS A002144
    """
    
    for p in primes():
        if (p-1)%4 == 0:
            yield p


def linear_primes(a,b):
    """
    Primes of the form a*n+b for naturals n
    
    Args:
        a -- multiplicative constant
        b -- additive constant
    
    OEIS A002145
    """
    
    for p in primes():
        if (p-a)%b == 0:
            yield p


def congruent_primes(n,k):
    """
    Primes that are congruent to n modulo k
    
    Args:
        n -- remainder
        k -- modulus
    
    OEIS A002145
    """
    
    for p in primes():
        if p%k == n:
            yield p


def blum_primes():
    """
    Primes such that P = 2p+1 and p = 2q+1 where p and q are odd primes\n
    OEIS
    """
    
    for p in congruent_primes(3,4):
        a = (p-1)//2
        b = (a-1)//2
        
        if a%2 == 1 and b % 2 == 1:
            if isprime(a) and isprime(b):
                yield p





#####################
## CLOSELY RELATED ##
#####################

def prime_gaps():
    """
    Prime Gaps: Gaps between successive primes\n
    OEIS A001223
    """
    
    yield from differences(primes())


def primorial():
    """
    Primoral Numbers: Cumulative product of primes\n
    OEIS A002110
    """
    
    yield from  prepend(1,partial_prods(primes()))


def prime_powers():
    """
    Prime Powers: Powers of prime numbers\n
    OEIS A000961
    """
    
    yield 1
    
    D = defaultdict(list)
    
    for q in naturals(2):
        if q not in D:
            yield q
            D[q + q] = [q]
        
        else:
            if len(D[q]) == 1:
                yield q
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]


def prime_characteristic():
    """
    Characteristic Function of the Primes: For each positive integer 1 if the number is prime otherwise 0\n
    OEIS A010051
    """
    
    cur = 1
    
    for p in primes():
        for i in range(p-cur):
            yield 0
            
        yield 1
        
        cur = p+1


def prime_counting():
    """
    Prime Counting Function: Count of primes less than each non-negative integer\n
    OEIS A000720
    """
    
    ctr = 0
    cur = 0
    
    for p in primes():
        for i in range(p-cur):
            yield ctr
        
        ctr += 1
        cur = p


def prime_product(P,inclusive=False):
    """
    Naturals such that all prime factors are in the set P
    
    Args:
        P -- an interable consisting of primes
        inclusive -- bool, if True only numbers divisible by all elements of P are included
    
    OEIS
    """
    
    require_iterable(["P"],[P])
    
    P = set(P)
    I = prod(P)
    
    for p in P:
        if not isprime(p):
            raise Exception(f"All elements of P must be prime, {p} is not prime")
    
    if inclusive:
        for n in arithmetic(I,I):
            m = n
            
            for p in P:
                while m % p == 0:
                    m //= p
            
            if m == 1:
                yield n
    
    
    else:
        for n in naturals(2):
            m = n
            
            for p in P:
                while m % p == 0:
                    m //= p
            
            if m == 1:
                yield n


def prime_signatures():
    """
    Prime Signatures: The prime signature of each positive integer, returns tuples\n
    OEIS A124010
    """
    
    D = defaultdict(list)
    
    yield ()
    
    for q in naturals(2):
        if q not in D:
            yield (1,)
            D[q + q] = [q]
        
        else:
            T = []
            r = q
            
            for p in D[q]:
                T.append(0)
                D[p+q].append(p)
                
                while r % p == 0:
                    r //= p
                    T[-1] += 1
                
            yield tuple(T)
            
            del D[q]


def odius_signature():
    """
    Positive integers which have an odd number of 1s in the binary expansions of their prime signatures
    OEIS A000028
    """
    
    for n,f in enumerate(prime_signatures(),1):
        total = 0
        for m in f:
            while m != 0:
                m,r = divmod(m,2)
                total ^= r
        if total == 1:
            yield n


def evil_signature():
    """
    Positive integers which have an odd number of 1s in the binary expansions of their prime signatures
    OEIS A000379
    """
    
    for n,f in enumerate(prime_signatures(),1):
        total = 0
        for m in f:
            while m != 0:
                m,r = divmod(m,2)
                total ^= r
        if total == 0:
            yield n



if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Primes")
    simple_test(primes(),15,
                "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47")
    
    print("\nPrimorials")
    simple_test(primorial(),9,
                "1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690")
    
    print("\nPrime Powers")
    simple_test(prime_powers(),16,
                "1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27")
    
    print("\nPythagorean Primes")
    simple_test(pythagorean_primes(),13,
                "5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109")
    
    print("\nPrime Counting Function")
    simple_test(prime_counting(),18,
                "0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7")
    
    print("\nCharacteristic Function of the Primes")
    simple_test(prime_characteristic(),18,
                "0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0")
    
    print("\nSuperprimes")
    simple_test(superprimes(),13,
                "3, 5, 11, 17, 31, 41, 59, 67, 83, 109, 127, 157, 179")
    
    print("\nSophie Germain Primes")
    simple_test(sophie_germain_primes(),13,
                "2, 3, 5, 11, 23, 29, 41, 53, 83, 89, 113, 131, 173")
    
    print("\nSafe Primes")
    simple_test(safe_primes(),13,
                "5, 7, 11, 23, 47, 59, 83, 107, 167, 179, 227, 263, 347")
    
    print("\nTwin Primes")
    simple_test(twin_primes(),14,
                "3, 5, 7, 11, 13, 17, 19, 29, 31, 41, 43, 59, 61, 71")
    
    print("\nTwin Prime Pairs")
    simple_test(twin_prime_pairs(),6,
                "(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)")
    
    print("\nSexy Prime Pairs")
    simple_test(n_gap_prime_pairs(6),5,
                "(5, 11), (7, 13), (11, 17), (13, 19), (17, 23)")
    
    print("\nPrime Tuples of form (0, 4, 6, 10, 12)")
    simple_test(prime_tuples((0, 4, 6, 10, 12)),2,
                "(7, 11, 13, 17, 19), (97, 101, 103, 107, 109)")
    
    print("\nPrime Gaps")
    simple_test(prime_gaps(),18,
                "1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6")
    
    print("\nPrimes of form 3k+4")
    simple_test(linear_primes(3,4),14,
                "3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103")
    
    print("\nBlum's Special Primes")
    simple_test(blum_primes(),10,
                "23, 47, 167, 359, 719, 1439, 2039, 2879, 4079, 4127")
    
    print("\n(3,5)-Prime Product Numbers")
    simple_test(prime_product([3,5]),13,
                "3, 5, 9, 15, 25, 27, 45, 75, 81, 125, 135, 225, 243")
    
    print("\n(3,5)-Prime Product Numbers (requiring both)")
    simple_test(prime_product([3,5],inclusive=True),11,
                "15, 45, 75, 135, 225, 375, 405, 675, 1125, 1215, 1875")
    
    print("\nPrime Signatures")
    simple_test(prime_signatures(),9,
                "(), (1,), (1,), (2,), (1,), (1, 1), (1,), (3,), (2,)")
    
    print("\nMOdius Signature Numbers")
    simple_test(odius_signature(),16,
                "2, 3, 4, 5, 7, 9, 11, 13, 16, 17, 19, 23, 24, 25, 29, 30")
    
    print("\nEvil Signature Numbers")
    simple_test(evil_signature(),15,
                "1, 6, 8, 10, 12, 14, 15, 18, 20, 21, 22, 26, 27, 28, 32")
    