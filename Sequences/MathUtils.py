from math import isqrt
from itertools import chain, combinations, repeat



###################
## FACTORIZATION ##
###################

def factors(n):
    """All Unique Factors"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = isqrt(n)+1
    
    S = set([1,n])
    
    for i in range(2,lim):
        f,r = divmod(n,i)
        
        if r == 0:
            S.add(i)
            S.add(f)
    
    return S



def proper_divisors(n):
    """The proper factors of n"""
    
    if type(n) != int:
        raise Exception("n must be an integer")
    
    if n == 1:
        return set([])
    
    lim = isqrt(n)+1
    
    S = set([1])
    
    for i in range(2,lim):
        f,r = divmod(n,i)
        
        if r == 0:
            S.add(i)
            S.add(f)
    
    return S


# I just think the name is neat
def aliquot_parts(n):
    """Alias for Proper Divisors"""
    return proper_divisors(n)


def nontrivial_factors(n):
    """All Non-Trivial Factors"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = isqrt(n)+1
    
    S = set([])
    
    for i in range(2,lim):
        f,r = divmod(n,i)
        
        if r == 0:
            S.add(i)
            S.add(f)
    
    return S


def prime_factorization(n):
    """Prime Factorization: Crude brute-force method"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    L = []
    
    while n % 2 == 0:
        L.append(2)
        n //= 2
    
    d = 3
    
    while n != 1:
        while n % d == 0:
            L.append(d)
            n //= d
        
        d += 2
    
    if n != 1:
        L.append(n)
    
    return L


def sum_of_divisors(n,p=1):
    """
    Sum of the divisors of n, including itself, raised to the specified power
    Also known as the sigma function
    """
    
    if p == 0:
        return len(factors(n))
    
    elif p == 1:
        return sum(factors(n))
    
    else:
        return sum([f**p for f in factors(n)])


def aliquot_sum(n,p=1):
    """
    Sum of the proper divisors of n raised to the specified power
    """
    
    if p == 0:
        return len(aliquot_parts(n))
    
    elif p == 1:
        return sum(aliquot_parts(n))
    
    else:
        return sum([f**p for f in aliquot_parts(n)])





############################
## REAL VALUED ARITHMETIC ##
############################

def real_sum(R1,R2,B=10):
    """
    Sum of two iterables that represent real numbers in base B
    """
    
    # Extend with zeros if finite
    R1e = chain(R1,repeat(0))
    R2e = chain(R2,repeat(0))
    
    D = []
    
    for a,b in zip(R1e,R2e):
        t = a+b
        
        if t <= B-1:
            while len(D) > 0:
                yield D.pop(0)
        
        if t > B-1:
            D[-1] += 1
        
        D.append(t%B)


def real_diff(R1,R2,B=10):
    """
    Difference of two iterables that represent real numbers in base B
    """
    
    # Extend with zeros if finite
    R1e = chain(R1,repeat(0))
    R2e = chain(R2,repeat(0))
    D = []
    
    for a,b in zip(R1e,R2e):
        t = a-b
        
        if t < 0:
            D[-1] -= 1
            
        else:
            while len(D) > 0:
                yield D.pop(0)
                
        D.append(t%B)


def real_prod_nat(R,n,B=10):
    """
    Product of an iterable that represent a real numbers in base B by a positive natural in base B
    """
    
    D = []
    
    for a in R:
        q,r = divmod(a*n,B)
        
        if q == 0:
            while len(D) > 0:
                yield D.pop(0)
        
        else:
            D[-1] += q
        
        D.append(r)


def real_div_nat(R,n,B=10):
    """
    Quotient of an iterable that represent a real numbers in base B by a positive natural in base B
    """
    
    r = 0
    
    for a in R:
        r = (r*B)+a
        q,r = divmod(r,n)
        
        yield q


# def real_prod(R1,R2,B):
#     """
#     Product of two iterables that represent real numbers in base B
#     """


# def real_div(R1,R2,B):
#     """
#     Product of two iterables that represent real numbers in base B
#     """





#################
## CONVERSIONS ##
#################

def _bits_to_int(bits):
    """Convert a list of 0s and 1s representing a bigendian binary integer"""
    
    n = 0
    p = 1
    
    for b in bits:
        n += p
        p *= 2
    
    return n


def digital_sum(n,b=10):
    """Sum of the digits of n in base b"""
    
    s = 0
    
    while n != 0:
        n,r = divmod(n,b)
        s += r
    
    return s


def digital_root(n,b=10):
    """Final value of the iteration of digital sums of n in base b"""
    
    while n >= b:
        n = digital_sum(n,b)
    
    return n


def int_to_digits(n,B=10):
    """
    Convert the integer n to its digits in base B
    Finite generator
    """
    
    n = abs(n)
    D = []
    
    while n != 0:
        n,r = divmod(n,B)
        D.append(r)
    
    return [i for i in reversed(D)]


def digits_to_int(D,B=10):
    """Convert a list of digits in base B to an integer"""
    
    n = 0
    p = 1
    
    for d in D:
        n += d*p
        p *= B
    
    return n


def frac_to_digits(n,d,B=10):
    """
    Convert the fraction n/d to its digits in base B
    Infintie generator
    """
    
    n = abs(n)
    
    if n//d > 9:
        for i in int_to_digits(n//d):
            yield i
        n = (n % d) * B
    
    while True:
        n,r = divmod(n,d)
        yield n
        n = r*B





###################
## GENERAL STUFF ##
###################


def repeating_part(n,d,B=10):
    """
    Repeating part of the fraction n/d in base B
    """
    
    # Get rid of the integer part
    if n > d:
        n = n%d*B
    
    digits = []
    remainders = []
    
    while n not in remainders:
        remainders.append(n)
        q,r = divmod(n,d)
        digits.append(q)
        n = r*B
    
    for p,rem in enumerate(remainders):
        if rem == n:
            break
    
    return digits[p:]


def inds_where(L,val):
    """
    All indices of list L that equal val
    """
    
    return [i for i in range(len(L)) if L[i] == val]


def first_where(L,val):
    """
    First index of list L that equals val
    """
    
    for pos,l in enumerate(L):
        if l == val:
            return pos
    
    return None


def powerset(L):
    L = list(L)
    return chain.from_iterable(combinations(L, r) for r in range(len(L)+1))





if __name__ == '__main__':
    print("Factors of 378")
    print(factors(378))
    
    print("\nAliquot Parts of 378")
    print(aliquot_parts(378))
    
    print("\nNon-trivial Factors of 378")
    print(nontrivial_factors(378))
    
    print("\nPrime Factorization of 378")
    print(prime_factorization(378))
    
    print("\nFirst 18 digits of 92/7 ≈ 13.1428 to digits")
    F = frac_to_digits(92,7)
    print([next(F) for i in range(18)])
    
    print("\nRepeating digits of 92/7")
    print(repeating_part(92,7))
    
    print("\nPowerset of {1,2,3,4}")
    print([i for i in powerset({1,2,3})])
    