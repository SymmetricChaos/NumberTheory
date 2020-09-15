from math import isqrt
from itertools import chain, combinations, repeat, count
from fractions import Fraction

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
    
    for d in count(3,2):
        
        while n % d == 0:
            L.append(d)
            n //= d
        
        if n == 1:
            break
    
    return L


def prime_power_factorization(n):
    """Factor a number into powers of primes"""
    
    L = []
    p = 1
    
    while n % 2 == 0:
        p *= 2
        n //= 2
    
    L.append(p)
    
    for d in count(3,2):
        p = 1
        
        while n % d == 0:
            p *= d
            n //= d
        
        if p != 1:
            L.append(p)
        
        if n == 1:
            break
    
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
    If the numbers do not have the decimal in the same place prepend 0s as needed
    Does not guarantee it will produce the canonical representation
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
            if len(D) == 0:
                D.append(0)
            D[-1] += 1
        
        D.append(t%B)


def real_diff(R1,R2,B=10):
    """
    Difference of two iterables that represent real numbers in base B
    If the numbers do not have the decimal in the same place prepend 0s as needed
    Does not guarantee it will produce the canonical representation
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
    Product of an iterable that represents a real number in base B by a positive natural in base B
    """
    
    D = []
    
    for a in R:
        q,r = divmod(a*n,B)
        
        if q == 0:
            while len(D) > 0:
                yield D.pop(0)
        
        else:
            if len(D) > 0:
                D[-1] += q
            else:
                D.append(q)
        
        D.append(r)


def real_div_nat(R,n,B=10):
    """
    Quotient of an iterable that represent a real numbers in base B by a positive natural in base B
    Prepend R with zeroes to shift decimal point
    """
    
    r = 0
    
    for a in R:
        r = (r*B)+a
        q,r = divmod(r,n)
        
        yield q





####################################
## CONTINUED FRACTION ARITHMETRIC ##
####################################

def rational_to_cfrac(n,d):
    """
    Terms of the simple continued fraction representation of n/d
    """
    
    out = []
    
    while d != 0:
        i = n//d
        
        out.append(i)
        n,d = d,n-(d*i)
    
    return out


def cfrac_to_rational(S,lim=20):
    """
    Pair representing the rational value of S out to lim terms
    """
    
    n0,n1 = 0,1
    d0,d1 = 1,0
    
    for ctr,c in enumerate(S):
        n0,n1 = n1,c*n1 + n0
        d0,d1 = d1,c*d1 + d0
        if ctr == lim:
            break
        
    return Fraction(n1,d1)


def finite_cfrac_to_rational(S):
    """
    Pair representing the rational value of S but requiring that S be finite
    """
    
    if type(S) not in (list,tuple):
        raise Exception("finite_cfrac_to_rational accepts only lists and tuples that represent a continued fraction in order to ensure cacluation terminates")
    
    n0,n1 = 0,1
    d0,d1 = 1,0
    
    for c in S:
        n0,n1 = n1,c*n1 + n0
        d0,d1 = d1,c*d1 + d0
        
    return Fraction(n1,d1)


def cfrac_convergents(S):
    """
    Convergents of the simple continued fraction S
    """
    
    n0,n1 = 0,1
    d0,d1 = 1,0
    
    for c in S:
        n0,n1 = n1,c*n1 + n0
        d0,d1 = d1,c*d1 + d0
        
        yield (n1,d1)


def cfrac_semiconvergents(S):
    """
    Semiconvergents of the simple continued fraction S, contains all best rational approximations
    """
    
    S = iter(S)
    A = [next(S)]
    prev_best = finite_cfrac_to_rational(A)
    
    yield prev_best.numerator,prev_best.denominator
    
    for a in S:
        A.append(a)
        next_best = finite_cfrac_to_rational(A)
        cur_diff = abs(prev_best-next_best)
        
        semi = A[:-1] + [(a-1)//2+1]
        semi_c = finite_cfrac_to_rational(semi)
        
        if abs(semi_c-next_best) > cur_diff:
            semi[-1] += 1
        
        while semi[-1] <= a:
            semi_c = finite_cfrac_to_rational(semi)
            yield semi_c.numerator,semi_c.denominator
            semi[-1] += 1
        
        prev_best = next_best


def mobius(a,b,c,d,S):
    """
    The Mobius transform
    """
    
    for s in S:
        a,b,c,d = b,a+b*s,d,c+d*s
        
        while c != 0 and d != 0 and a//c == b//d:
            q = a//c
            yield q
            a,b,c,d = c,d,a-c*q,b-d*q
    
    #Final step
    a,b,c,d = b,b,d,d
    yield a//c


def double_mobius(a,b,c,d,e,f,g,h,X,Y):
    
    if 0 in [e,f,g,h]:
        raise Exception("e, f, g, and h must all be nonzero")
    
    ae = Fraction(a,e)
    bd = Fraction(b,f)
    cf = Fraction(c,g)
    dh = Fraction(d,h)
    





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
    
    while True:
        n,r = divmod(n,b)
        s += r
        if n == 0:
            return s


def digital_prod(n,b=10):
    """Product of the digits of n in base b"""
    
    s = 1
    
    while True:
        n,r = divmod(n,b)
        s *= r
        if n == 0:
            return s


def digital_root(n,b=10):
    """Final value of the iteration of digital sums of n in base b"""
    
    while n >= b:
        n = digital_sum(n,b)
    
    return n


def int_to_digits(n,B=10):
    """
    Convert the integer n to its digits in base B
    """
    
    n = abs(n)
    D = []
    
    while n != 0:
        n,r = divmod(n,B)
        D.append(r)
    
    return [i for i in reversed(D)]


def digits(n,B=10):
    """
    Number of digits of n in base B
    """
    
    n = abs(n)
    ctr = 0
    
    while n != 0:
        n //= B
        ctr += 1
    
    return ctr


def digits_to_int(D,B=10):
    """
    Convert a list of digits in base B to an integer
    """
    
    n = 0
    p = 1
    
    for d in D:
        n += d*p
        p *= B
    
    return n


def frac_to_digits(n,d,B=10):
    """
    Convert the fraction n/d to its digits in base B
    Infinite generator
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





#############################
## INFINITE ARRAY INDICIES ##
#############################

def triangle_pairs(m=0):
    """
    Indicies of a triangular array
    
    Args:
        m - minimum value of the index
    """
    
    for a in count(m,1):
        for b in range(m,a+1):
            yield (a,b)


def antidiagonal_pairs(m=0):
    """
    Indicies the antidiagonals of an infinite square array
    
    Args:
        m - minimum value of the index
    """
    
    for n in count(m,1):
        for a,b in zip(range(n,m-1,-1),range(m,n+1)):
            yield (a,b)





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
    return chain.from_iterable(combinations(list(L), r) for r in range(len(L)+1))





if __name__ == '__main__':
    print("Factors of 378")
    print(factors(378))
    
    print("\nAliquot Parts of 378")
    print(aliquot_parts(378))
    
    print("\nNon-trivial Factors of 378")
    print(nontrivial_factors(378))
    
    print("\nPrime Factorization of 378")
    print(prime_factorization(378))
    
    print("\nPrime Power Factorization of 378")
    print(prime_power_factorization(378))
    
    print("\nFirst 18 digits of 92/7 ≈ 13.1428 to digits")
    F = frac_to_digits(92,7)
    print([next(F) for i in range(18)])
    
    print("\nRepeating digits of 92/7")
    print(repeating_part(92,7))
    
    print("\nPowerset of {1,2,3,4}")
    print([i for i in powerset({1,2,3})])
    
    print("\nConvergents of Pi up to 355/113")
    print([i for i in cfrac_convergents([3, 7, 15, 1])])
    
    print("\nSemiconvergents of Pi up to 355/113")
    print([i for i in cfrac_semiconvergents([3, 7, 15, 1])])
    
    print("\nMobius Transform")
    print([ i for i in mobius(1,2,2,0,iter([1,5,2])) ])
    