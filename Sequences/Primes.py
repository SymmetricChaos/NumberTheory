from Sequences.Simple import naturals, arithmetic
from Sequences.MathUtils import factors
from collections import defaultdict
from itertools import takewhile
from Sequences.NiceErrorChecking import require_integers, require_positive
from math import prod, gcd
from Sequences.SequenceManipulation import partial_prods, prepend

## Generator that returns primes (not my work)
def primes():
    """
    Prime Numbers: Positive integers with exactly two factors\n
    OEIS A000040
    """
    
    D = defaultdict(list)
    
    for q in naturals(2):
        
        if q not in D:
            yield q
            D[q * q] = [q]
        
        else:
            for p in D[q]:
                D[p+q].append(p)
            del D[q]


def composites():
    """
    Composite Numbers: Positive integers with more than two factors\n
    OEIS A002808
    """
    
    D = defaultdict(list)
    
    for q in naturals(2):
        
        if q not in D:
            D[q * q] = [q]
        
        else:
            yield q
            for p in D[q]:
                D[p+q].append(p)
            del D[q]


def primorial():
    """
    Primoral Numbers: Cumulative product of primes\n
    OEIS A002110
    """
    
    return prepend(1,partial_prods(primes()))


def compositorial():
    """
    Compositorial Numbers: Cumulative product of composite numbers\n
    OEIS A036691
    """
    
    return prepend(1,partial_prods(composites()))


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


def pythagorean_primes():
    """
    Pythagorean Primes: Primes that can be the hypotenuse of an integer right triangle\n
    OEIS A002144
    """
    
    for p in primes():
        if (p-1)%4 == 0:
            yield p


def smooth(B):
    """
    Smooth Numbers: Positive integers with no prime factors greater than B
    
    OEIS A003586, A051037, A002473, A051038, A080197, A080681, A080682, A080683
    
    Args:
        B -- largest prime factor allowed
    """
    
    require_integers(["B"],[B])
    require_positive(["B"],[B])
    
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
    
    for i in smooth(5):
        yield i


def rough(B):
    """
    Rough Numbers: Positive integers with no prime factors less than B
    
    OEIS A000027, A005408, A007310, A007775, A008364, A008365, A008366, A166061, A166063
    
    Args:
        B -- smallest prime factor allowed
    """
    
    require_integers(["B"],[B])
    require_positive(["B"],[B])
    
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


def divisors():
    """
    Number of Divisors: Count of divisors for each positive integer\n
    OEIS A000005
    """
    
    for i in naturals(1):
        yield len(factors(i))


def prime_divisors():
    """
    Number of Prime Divisors with Multiplicity: Length of prime factorization for each positive integer\n
    OEIS A001222
    """
    
    for n in naturals(1):
        ctr = 0
        
        for p in primes():
            while n % p == 0:
                ctr += 1
                n = n // p
            
            if n == 1:
                yield ctr
                break


def unique_prime_divisors():
    """
    Number of Unique Prime Divisors: Count of unique prime factors for each positive integer\n
    OEIS A001221
    """
    
    D = defaultdict(list)
    q = 2
    
    yield 0
    
    while True:
        if q not in D:
            yield 1
            D[q + q] = [q]
        
        else:
            yield len(D[q])
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]
        
        q += 1


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
    Squarefree Kernels: Largest squarefree factor of each positive integer\n
    OEIS A007947
    """
    
    D = defaultdict(list)
    q = 2
    
    yield 1
    
    while True:
        if q not in D:
            yield q
            
            D[q + q] = [q]
        
        else:
            yield prod(D[q])
            
            for p in D[q]:
                D[p+q].append(p)
            
            del D[q]
        
        q += 1


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


def totients():
    """
    Totients: Count of positive integers coprime to each positive integer\n
    OEIS A000010
    """
    
    D = defaultdict(list)
    q = 2
    
    yield 1
    
    while True:
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
        
        q += 1


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


# def charmichael():
#     """
#     Charmichael Function: Smallest 
#     OEIS A002322
#     """


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


def coprimes(n):
    """
    All positive integers coprime to n
    """
    
    require_integers(["n"],[n])
    require_positive(["n"],[n])
    
    F = []
    for p in primes():
        if n%p == 0:
            F.append(p)
        if p >= n:
            break
    
    def divby(n,F):
        for f in F:
            if x%f == 0:
                return False
        return True
    
    for x in naturals(1):
        if divby(x,F):
            yield x


def lucky():
    """
    Lucky Numbers: Prime-like integers resulting from a modified sieve of Eratosthenes\n
    OEIS A000959
    """
    
    yield 1
    yield 3
    
    # Terms of the sequence and where in the cycle each is
    terms = [3]
    ctrs = [2]
    
    # Update the cycles positions
    # If any cycle has reached zero we're not at a lucky number and no later 
    # cycles will be updated since the value has been sieved out before that
    # number is known
    def update():
        for n,t in enumerate(terms):
            ctrs[n] = (ctrs[n]+1)%t
            if ctrs[n] == 0:
                return False
        return True
    
    # Which lucky number we're currently looking for
    # This sets where the cycle for a newly found lucky number begins
    nth = 3
    
    # Go through the odds greater than 5 looking for lucky numbers
    for o in arithmetic(5,2):
        if update():
            yield o
            
            terms.append(o)
            ctrs.append(nth)
            nth += 1





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Primes")
    simple_test(primes(),15,
                "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47")
    
    print("\nComposites")
    simple_test(composites(),15,
                "4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25")
    
    print("\nPrimorials")
    simple_test(primorial(),9,
                "1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690")
    
    print("\nCompositorial")
    simple_test(compositorial(),9,
                "1, 4, 24, 192, 1728, 17280, 207360, 2903040, 43545600")
    
    print("\nPrime Powers")
    simple_test(prime_powers(),16,
                "1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27")
    
    print("\nTotient Numbers")
    simple_test(totients(),17,
                "1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16")
    
    print("\nCototient Numbers")
    simple_test(cototients(),18,
                "0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, 1, 8, 7, 8, 1, 12")
    
    print("\nPythagorean Primes")
    simple_test(pythagorean_primes(),13,
                "5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109")
    
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
    
    print("\nPrime Counting Function")
    simple_test(prime_counting(),18,
                "0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7")
    
    print("\nCharacteristic Function of the Primes")
    simple_test(prime_characteristic(),18,
                "0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0")
    
    print("\nCharacteristic Triangle of Coprimes")
    simple_test(coprime_characteristic(),18,
                "1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0")
    
    print("\nNaturals Coprime to 24")
    simple_test(coprimes(24),14,
                "1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41")
    
    print("\nLucky Numbers")
    simple_test(lucky(),15,
                "1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63")