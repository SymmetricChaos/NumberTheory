from math import isqrt, gcd
from itertools import chain, combinations, repeat, count
from functools import reduce
from fractions import Fraction
from collections import defaultdict

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


# To avoid potential circular reference from Sequences.Primes in following functions
def _primes_copy():
    D = defaultdict(list)
    
    for q in count(2,1):
        if q not in D:
            yield q
            D[q * q] = [q]
        
        else:
            for p in D[q]:
                D[p+q].append(p)
            del D[q]


def prime_factorization(n):
    """Prime Factorization: Crude brute-force method"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    if n == 1:
        return []
    
    L = []
    
    for p in _primes_copy():
        while n % p == 0:
            L.append(p)
            n //= p
        
        if n == 1:
            break
    
    return L


def unique_prime_factors(n):
    """Unique Prime Factors"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    L = []
    
    for p in _primes_copy():
        if n % p == 0:
            L.append(p)
            while n % p == 0:
                n //= p
        
        if n == 1:
            break
    
    return L


def prime_power_factorization(n):
    """Factor a number into powers of primes"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    L = []
    
    for p in _primes_copy():
        q = 1
        
        while n % p == 0:
            q *= p
            n //= p
        
        if q != 1:
            L.append(q)
        
        if n == 1:
            break
    
    return L


def canonical_factorization(n):
    """Prime factors and their exponents"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    F = {}
    
    for p in _primes_copy():
        ctr = 0
        
        while n % p == 0:
            ctr += 1
            n //= p
        
        if ctr != 0:
            F[p] = ctr
        
        if n == 1:
            break
    
    return F


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
                if D[-1] >= B:
                    print("ISSUE")
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


def homographic_convergents(a,b,c,d,S):
    """
    Rational convergents of (a+bx)/(c+dx) where x is the real represented by S
    """
    
    for s in S:
        a,b,c,d = b,a+b*s,d,c+d*s
        
        g = gcd(b,d)
        yield (b//g,d//g)


# def bihomographic_convergents(a,b,c,d,e,f,g,h,X,Y):


# def digits_to_cfrac(D,chunk_size=10):
#     """
#     Convert a stream of decimal digits to a stream of continued fraction convergents
#     """
#    
#     # Calculate the terms for the first n terms, then check what happens if the
#     # next term is 9. All digits that match (and haven't been output yet) can be given
#     # https://x.st/continued-fraction-streams/
#     # Not sure how to handle number greater than 9
#    
#     # For efficiency, because this method recomputes the terms, digits should be taken in chunks
#    
#     C = []
#    
#     for n,d in enumerate(D,1):
#         if n % 10 == 0:
#             # use C to compute all terms
#         else:
#             C.append(d)





#################
## CONVERSIONS ##
#################

def int_to_digits(n,B=10,bigendian=False):
    """
    Convert the integer n to its digits in base B
    """
    
    n = abs(n)
    D = []
    
    while n != 0:
        n,r = divmod(n,B)
        D.append(r)
    
    if bigendian:
        return D
    else:
        return [i for i in reversed(D)]


def digits_to_int(D,B=10,bigendian=False):
    """
    Convert a list of digits in base B to an integer
    """
    
    n = 0
    p = 1
    
    if bigendian:
        for d in D:
            n += d*p
            p *= B
        
        return n
    
    else:
        for d in reversed(D):
            n += d*p
            p *= B
        
        return n


def frac_to_digits(n,d,B=10):
    """
    Convert the rational n/d to its digits in base B
    Infinite generator, little-endian only
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


def int_to_balt(n):
    """
    Convert an integer to a list of its digits in balanced ternary
    """
    
    D = []
    
    while n != 0:
        n,r = divmod(n,3)
        if r == 2:
            n += 1
            D.append(-1)
        else:
            D.append(r)
    
    return [i for i in reversed(D)]


def balt_to_int(D):
    """
    Convert a list of balanced ternary digits to an integer
    """
    
    return reduce(lambda y,x: x + 3 * y,D,0)





########################
## DIGIT MANIPULATION ##
########################

def digital_sum(n,B=10):
    """Sum of the digits of n in base B"""
    
    s = 0
    
    while True:
        n,r = divmod(n,B)
        s += r
        if n == 0:
            return s


def digital_prod(n,B=10):
    """Product of the digits of n in base B"""
    
    s = 1
    
    while True:
        n,r = divmod(n,B)
        s *= r
        if n == 0:
            return s


def digital_root(n,B=10):
    """Final value of the iteration of digital sums of n in base B"""
    
    while n >= B:
        n = digital_sum(n,B)
    
    return n


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


def nth_sign(n):
    """
    (-1)^n
    """
    
    if n % 2 == 0:
        return 1
    
    return -1


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b//a) * x, x)


def _legendre_symbol(a,p):
    """
    The Legendre Symbol: 1 if a is a quadratic residue mod p, -1 if it is a nonresidue, 0 if a is zero
    p must be prime but this is hard to check so is not done in the function itself
    """
    if p == 2:
        if a%2 == 0:
            return 0
        if a%8 in (1,7):
            return 1
        return -1
            
    out = pow(a,(p-1)//2,p)
    if out == 1:
        return 1
    if out == 0:
        return 0
    else:
        return -1


def kronecker_symbol(a,n):
    """Extend the Legendre Symbol to all naturals"""
    fac = prime_factorization(n)
    out = 1
    for f in fac:
        out *= _legendre_symbol(a,f)
    return out


def poly_mult(P,Q):
    """
    Product of two polynomials, both in ascending order
    """
    
    L = [0]*(len(P)+len(Q))
    
    for i in range(len(P)):
        for j in range(len(Q)):
            L[i+j] += P[i]*Q[j]
    
    for x in L[::-1]:
        if x == 0:
            L.pop()
        else:
            break
    return L


def kronecker_delta(i,j):
    """
    The Kronecker Delta Function
    (actually might be unnecessary in Python)
    """
    
    if i == j:
        return 1
    return 0


def arithmetic_derivative(n):
    
    if n in (0,1):
        return 0
    
    lim = isqrt(n)+1
    
    for i in range(2,lim):
        if n % i == 0:
            p,q = i,n//i
            return q + p*arithmetic_derivative(q)
    
    return 1


def jordan_totient(n,k=1):
    """
    Jordan's Totient Function: Number of sets of size k with positive integers less than n such that with n add the they are setwise coprime
    """
    
    F = unique_prime_factors(n)
    
    num = 1
    den = 1
    for p in F:
        num *= p**k-1
        den *= p**k
    
    return (n**k*num)//den





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
    
    print("\nCanonical Factorization of 378")
    print(canonical_factorization(378))
    
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
    
    print("\nBalanced Ternary Representation of -378")
    print(int_to_balt(-378))
    
    print("\nConvert Balanced Ternary Number -+++000 to an integer")
    print(balt_to_int([-1, 1, 1, 1, 0, 0, 0]))
    
    print("\nConvert 387 to decimal digits")
    print(int_to_digits(387))
    
    print("\nConvert the decimal digits [3,8,7] to an integer")
    print(digits_to_int([3,8,7]))
    
    print("\nProduct of 1 + 2x + 3x^2 + 4x^3 with 9 + 3x + 2x^2 + x^3")
    print(poly_mult([1,2,3,4],[9,3,2,1]))
    
    print("\nArithmetic Derivative of 72")
    print(arithmetic_derivative(72))
    
    print("\nJordan 2-Totient of 4")
    print(jordan_totient(4,2))
    