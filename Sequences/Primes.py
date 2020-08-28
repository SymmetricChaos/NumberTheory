from Sequences.Simple import naturals, arithmetic
from Sequences.MathUtils import factorization
from collections import defaultdict
from itertools import takewhile
from Sequences.NiceErrorChecking import require_integers, require_positive
from math import prod, gcd

## Generator that returns primes (not my work)
def primes():
    """
    Prime Numbers: Positive integers with exactly two factors
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
    Composite Numbers: Positive integers with more than two factors
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


def primorials():
    """
    Primoral Numbers: Cumulative product of primes
    OEIS A002110
    """
    
    out = 1
        
    for i in primes():
        yield out
        
        out *= i


def compositorial():
    """
    Compositorial Numbers: Cumulative product of composite numbers
    OEIS A036691
    """
    
    out = 1
    
    for i in composites():
        yield out
        
        out *= i


def prime_powers():
    """
    Prime Powers: Powers of prime numbers
    OEIS A000961
    """
    
    pass


def pythagorean_primes():
    """
    Pythagorean Primes: Primes that can be the hypotenuse of an integer right triangle
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
    Hamming Numbers: The 5-Smooth numbers also known as the Regular Numbers
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
    Highly Composite Numbers: Positive integers that have more factors than any smaller positive integer
    OEIS A002182
    """
    
    F = 0
    for i in naturals(1):
        L = len(factorization(i))
        
        if L > F:
            F = L
            yield i


def divisors():
    """
    Number of Divisors: Count of divisors for each positive integer
    OEIS A000005
    """
    
    for i in naturals(1):
        yield len(factorization(i))


def prime_divisors():
    """
    Number of Prime Divisors with Multiplicity: Length of prime factorization for each positive integer
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
    Number of Unique Prime Divisors: Count of unique prime factors for each positive integer
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
    Squarefree Numbers: Positive integers not divisible by any prime more than once
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
    Squarefree Kernels: Largest squarefree factor of each positive integer
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
    Prime Counting Function: Count of primes less than each non-negative integer
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
    Characteristic Function of the Primes: For each positive integer 1 if the number is prime otherwise 0
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
    Totients: Count of positive integers coprime to each positive integer
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


def coprime_characteristic():
    """
    Triangle of coprime pairs: 1 if the pair is coprimes and 0 if not
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
    
    for o in arithmetic(5,2):
        if update():
            terms.append(o)
            ctrs.append(nth)
            nth += 1
            yield o



if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Primes")
    simple_test(primes(),10,
                "2, 3, 5, 7, 11, 13, 17, 19, 23, 29")
    
    print("\nComposites")
    simple_test(composites(),10,
                "4, 6, 8, 9, 10, 12, 14, 15, 16, 18")
    
    print("\nPrimorials")
    simple_test(primorials(),8,
                "1, 2, 6, 30, 210, 2310, 30030, 510510")
    
    print("\nCompositorial")
    simple_test(compositorial(),7,
                "1, 4, 24, 192, 1728, 17280, 207360")
    
    print("\nPythagorean Primes")
    simple_test(pythagorean_primes(),10,
                "5, 13, 17, 29, 37, 41, 53, 61, 73, 89")
    
    print("\n5-Smooth (Hamming)")
    simple_test(smooth(5),11,
                "1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15")
    
    print("\n5-Rough")
    simple_test(rough(5),10,
                "1, 5, 7, 11, 13, 17, 19, 23, 25, 29")
    
    print("\nHighly Composite")
    simple_test(highly_composite(),10,
                "1, 2, 4, 6, 12, 24, 36, 48, 60, 120")
    
    print("\nNumber of Divisors")
    simple_test(divisors(),10,
                "1, 2, 2, 3, 2, 4, 2, 4, 3, 4")
    
    print("\nNumber of Prime Divisors (with multiplicity)")
    simple_test(prime_divisors(),10,
                "0, 1, 1, 2, 1, 2, 1, 3, 2, 2")
    
    print("\nNumber of Unique Prime Divisors")
    simple_test(unique_prime_divisors(),10,
                "0, 1, 1, 1, 1, 2, 1, 1, 1, 2")
    
    print("\nSquarefree Numbers")
    simple_test(squarefree(),10,
                "1, 2, 3, 5, 6, 7, 10, 11, 13, 14")
    
    print("\nSquarefree Kernels")
    simple_test(squarefree_kernel(),10,
                "1, 2, 3, 2, 5, 6, 7, 2, 3, 10")
    
    print("\nPrime Counting Function")
    simple_test(prime_counting(),10,
                "0, 0, 1, 2, 2, 3, 3, 4, 4, 4")
    
    print("\nCharacteristic Function of the Primes")
    simple_test(prime_characteristic(),10,
                "0, 1, 1, 0, 1, 0, 1, 0, 0, 0")
    
    print("\nCharacteristic Triangle of Coprimes")
    simple_test(coprime_characteristic(),10,
                "1, 1, 0, 1, 1, 0, 1, 0, 1, 0")
    
    print("\nNaturals Coprime to 24")
    simple_test(coprimes(24),10,
                "1, 5, 7, 11, 13, 17, 19, 23, 25, 29")
    
    print("\nLucky Numbers")
    simple_test(lucky(),10,
                "1, 3, 7, 9, 13, 15, 21, 25, 31, 33")
    