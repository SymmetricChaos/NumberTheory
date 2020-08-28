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


# Copy of choose function to prevent reference issues
def choose(n,k):
    """Binomial Coefficient"""
    
    if type(n) != int:
        raise TypeError("n must be an integer")
    if type(k) != int:
        raise TypeError("k must be an integer")
    
    if n < k:
        raise ValueError("n cannot be less than k")
    if k < 0:
        raise ValueError("k must be nonnegative")
        
    # Calculate the numerator and denominator seperately in order to avoid loss
    # of precision for large numbers.
    N = 1
    D = 1
    
    for i in range(1,k+1):
        N *= (n+1-i)
        D *= i
    
    return N//D


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





if __name__ == '__main__':
    print("Factors of 378")
    print(factors(378))
    
    print("\nAliquot Parts of 378")
    print(aliquot_parts(378))
    
    print("\nAliqot Parts of 378")
    print(nontrivial_factors(378))
    
    print("\nPrime Factorization of 378")
    print(prime_factorization(378))