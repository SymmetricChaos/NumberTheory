from fractions import Fraction
from math import gcd


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


def convergents(cfrac,mode):
    """
    Convergents of cfrac (iterable) given either as fractions, numerators, or denominators
    """
    
    if mode == "f":
        yield from _cfrac_convergents(cfrac)
    
    elif  mode == "n":
        for i in _cfrac_convergents(cfrac):
            yield i.numerator
    
    elif mode == "d":
        for i in _cfrac_convergents(cfrac):
            yield i.denominator
    
    else:
        raise ValueError("mode must be f (fraction), n (numerator), or d (denominator)")


def _cfrac_convergents(S):
    """
    Convergents of the simple continued fraction S
    """
    
    n0,n1 = 0,1
    d0,d1 = 1,0
    
    for c in S:
        n0,n1 = n1,c*n1 + n0
        d0,d1 = d1,c*d1 + d0
        
        yield Fraction(n1,d1)


def semiconvergents(cfrac,mode):
    """
    Semiconvergents of cfrac (iterable) given either as fractions, numerators, or denominators
    """
    
    if mode == "f":
        yield from _cfrac_semiconvergents(cfrac)
    
    elif  mode == "n":
        for i in _cfrac_semiconvergents(cfrac):
            yield i.numerator
    
    elif mode == "d":
        for i in _cfrac_semiconvergents(cfrac):
            yield i.denominator
    
    else:
        raise ValueError("mode must be f (fraction), n (numerator), or d (denominator)")


def _cfrac_semiconvergents(S):
    """
    Semiconvergents of the simple continued fraction S, contains all best rational approximations
    """
    
    S = iter(S)
    A = [next(S)]
    prev_best = finite_cfrac_to_rational(A)
    
    yield prev_best
    
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
            yield semi_c
            semi[-1] += 1
        
        prev_best = next_best


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