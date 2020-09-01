from math import isqrt


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


def aliquot_parts(n):
    """All Unique Factors except n itself"""
    
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
    
    # Either include or don't include trivial factors
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


def _bits_to_int(bits):
    """Convert a list of 0s and 1s representing a bigendian binary integer"""
    
    n = 0
    p = 1
    
    for b in bits:
        if b != 0:
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
    
    for i in reversed(D):
        yield i


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
    