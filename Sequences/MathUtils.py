from math import isqrt, gcd, comb
from itertools import chain, combinations, repeat, count
from functools import reduce
from sympy import factorint, divisors, divisor_sigma, legendre_symbol

###################
## FACTORIZATION ##
###################

def factors(n):
    """All Unique Factors"""
    
    return divisors(n)


def proper_divisors(n):
    """The proper factors of n"""
    
    if type(n) != int:
        raise Exception("n must be an integer")
    
    return divisors(n,proper=True)


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
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    F = canonical_factorization(n)
    L = []
    
    for p,e in F.items():
        L += [p]*e
    
    return sorted(L)


def unique_prime_factors(n):
    """Unique Prime Factors"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    F = canonical_factorization(n)
    L = []
    
    for p in F:
        L.append(p)
    
    return sorted(L)


def prime_power_factorization(n):
    """Factor a number into powers of primes"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    F = canonical_factorization(n)
    L = []
    
    for p,e in F.items():
        L.append(p**e)
    
    return sorted(L)


def canonical_factorization(n):
    """Prime factors and their exponents"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    if n == 0:
        raise ValueError("Prime factorization of 0 is undefined")
    
    return factorint(n)


# def special_factorization(n,W):
#     """Factor n into numbers from the list or tuple W"""
#    
#     if type(n) != int:
#         raise Exception("n must be an integer") 
#    
#     if type(W) not in (list,tuple,set):
#         raise Exception("W must be a list, tuple, or set")
#    
#     W = sorted(list(set(W)))
#    
#     L = []
#    
#     for w in W:
#         if w != 1:
#             while n % w == 0:
#                 L.append(w)
#                 n //= w
#            
#             if n == 1:
#                 break
#            
#             if w > n:
#                 break
#    
#     if n != 1:
#         return L
#    
#     else:
#         return []


def sum_of_divisors(n,p=1):
    """
    Sum of the divisors of n, including itself, raised to the specified power
    Also known as the sigma function
    """
    
    return divisor_sigma(n,p)


def aliquot_sum(n,p=1):
    """
    Sum of the proper divisors of n raised to the specified power p
    """
    
    if p == 0:
        return len(aliquot_parts(n))
    
    elif p == 1:
        return sum(aliquot_parts(n))
    
    else:
        return sum([f**p for f in aliquot_parts(n)])


def nondivisors(n):
    """
    Natural numbers less than n that are not factors of n
    """
    
    return [i for i in range(n) if i not in factors(n)]


# def antidivisors(n):
#     """
#     Natural numbers less than n that are not factors of n and for which the two nearest multiples to n are the same distance from n
#     """
#    
#     return antidivisors(n)


# TODO: Seems like a more efficient method should exist
def coprime_to(n):
    L = []
    for i in range(2,n):
        if gcd(i,n) == 1:
            L.append(i)
    return L





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
        return tuple(D)
    else:
        return tuple([i for i in reversed(D)])


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


def int_to_bits(n,width=None,bigendian=False):
    
    n = abs(n)
    D = []
    
    while n != 0:
        n,r = divmod(n,2)
        D.append(r)
    
    if D == []:
        D = [0]
    
    if width != None:
        D += [0]*(width-len(D))
    
    if bigendian:
        return tuple(D)
    else:
        return tuple([i for i in reversed(D)])


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
    
    return tuple([i for i in reversed(D)])


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
    Returns a list
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


def all_subsets(sequence):
    """
    Generalize the above powerset code to give all finite subsets of a sequences by iteratively merging prefixes
    Effectively colexicographic order
    """
    
    L = [(next(sequence),)]
    
    yield L[0]
    
    for s in sequence:
        yield (s,)
        T = [(s,)]
        
        for l in L:
            sub = l+(s,)
            yield sub
            T.append(sub)
        
        L += T


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
        g, x, y = egcd(b % a, a)
        return (g, y-(b//a) * x, x)


def lcm(a,b):
    return abs(a*b)//gcd(a,b)


def mod_inv(n,m):
    """Modular Multiplicative Inverse"""
    
    g,x,y = egcd(n,m)
    
    if g != 1:
        raise Exception("n and m are not coprime, no modular multiplicative inverse exists")
    
    return x%m


def multi_gcd(*args):
    """Pairwise GCD"""

    # Handle the case that a list is provided
    if len(args) == 1 and type(args[0]) is list:
        return multi_gcd(*args[0])
    
    # the gcd of a number with itself is iself
    if len(args) == 1:
        return args[0]
    
    # calculate gcd for two numbers
    if len(args) == 2:
        a = args[0]
        b = args[1]
        return gcd(a,b)
    
    # if more than two break it up recursively
    a = multi_gcd(*args[0:2])
    b = multi_gcd(*args[2:])
    return multi_gcd(a,b)


def multi_lcm(*args):
    """Pairwise LCM"""
    
    # Handle the case that a list is provided
    if len(args) == 1 and type(args[0]) is list:
        return multi_lcm(*args[0])
    
    # the lcm of a number with itself is iself
    if len(args) == 1:
        return args[0]
    
    # calculate lcm for two numbers
    if len(args) == 2:
        a = args[0]
        b = args[1]
        return lcm(a,b)
    
    # if more than two break it up recursively
    a = multi_lcm(*args[0:2])
    b = multi_lcm(*args[2:])
    return multi_lcm(a,b)


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


def kronecker_symbol(a,n):
    """Extend the Legendre Symbol to all naturals"""
    fac = prime_factorization(n)
    out = 1
    for f in fac:
        out *= legendre_symbol(a,f)
    return out


def factor_out_twos(n):
    """
    Returns the tuple (d,s) such that n = d*(2**s) for the smallest value of d
    """
    
    d = n
    s = 0
    
    while d % 2 == 0:
        s += 1
        d //= 2
    
    return d,s


def sign_of(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0




#################
## POLYNOMIALS ##
#################

def poly_mult(P,Q):
    """
    Product of two polynomials in ascending order
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


def poly_sum(P,Q):
    """
    Sum of two polynomials in ascending order
    """
    
    P = P[:]
    Q = Q[:]
    d = abs((len(Q)-len(P)))
    
    if len(Q) > len(P):
        P = P + [0]*d
    else:
        Q = Q + [0]*d
    
    L = []
    
    for p,q in zip(P,Q):
        L.append(p+q)
    
    return L


def poly_eval(P,x):
    """
    Evaluate the polynomial P at x
    """
    
    out = 0
    e = 1
    
    for coef in P:
        out += coef*e
        e *= x
    
    return out





#######################
## LIST MANIPULATION ##
#######################

def list_diffs(L):
    
    out = []
    
    for i in range(len(L)-1):
        a,b = L[i], L[i+1]
        out.append(b-a)
    
    return out





if __name__ == '__main__':
    print("Factors of 378")
    print(factors(378))
    
    print("\nAliquot Parts of 378")
    print(aliquot_parts(378))
    
    print("\nNon-trivial Factors of 378")
    print(nontrivial_factors(378))
    
    print("\nPrime Factorization of 378")
    print(prime_factorization(378))
    
    print("\nUnique Prime Factors of 378")
    print(unique_prime_factors(378))
    
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
    
    print("\nSum of 2 + 3x + 5x^2 with 7 + 11x + 13x^2 + 17x^3")
    print(poly_sum([2,3,5],[7,11,13,17]))
    
    print("\nArithmetic Derivative of 72")
    print(arithmetic_derivative(72))
    
    print("\nJordan 2-Totient of 4")
    print(jordan_totient(4,2))
    
    print("\nAll Subsets of [1,2,3,4,5]")
    print([i for i in all_subsets(iter([1,2,3,4,5]))])
    
    print("\n5-Combination Associated with 72")
    print(int_to_comb(72,5))
    
    print("\nInteger Associated with the 5-Combination (8,6,3,1,0)")
    print(comb_to_int([8,6,3,1,0]))
    
    print("\nIndicator Vector for Above Combination")
    print(comb_to_vector([8,6,3,1,0]))
