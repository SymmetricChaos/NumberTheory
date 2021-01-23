from Sequences.Simple import naturals
from Sequences.NiceErrorChecking import require_integers, require_geq, require_iterable
from Sequences.MathUtils import poly_mult, poly_sum, poly_eval
from Sequences.Divisibility import odd_primes
from Sequences.Rationals.FractionUtils import _pretty_fracs, _pretty_fracs_tuple, numerators, denominators

from fractions import Fraction
from math import gcd, isqrt






def positive_rationals():
    """
    Sequence of all positive rationals
    """
    
    yield Fraction(1)
    
    for n in naturals(1):
        for d in range(1,n):
            if gcd(n,d) == 1:
                yield Fraction(n,d)


def babylonian_sqrt(n,init=None):
    """
    Esimates of the sqrt of n using the Babylonian method, defaults to using integer sqrt as a starting value
    
    Args:
        n -- positive integer to extract the square root of
        init -- initial guess for the square root
    """
    
    if init == None:
        cur = Fraction(isqrt(n))
    else:
        cur = Fraction(init)
        
    require_integers(["n"],[n])
    require_geq(["n","init"],[n,cur],0)
    
    while True:
        yield cur
        cur = (cur+(n/cur))/2


def bakhshali_sqrt(n,init=None):
    """
    Esimates of the sqrt of n using the Bakhshali method, defaults to using integer sqrt as a starting value
    
    Args:
        n -- positive integer to extract the square root of
        init -- initial guess for the square root
    """
    
    if init == None:
        cur = Fraction(isqrt(n))
    else:
        cur = Fraction(init)
        
    require_integers(["n"],[n])
    require_geq(["n","init"],[n,cur],0)
    
    while True:
        yield cur
        
        a = (n-(cur*cur))/(2*cur)
        cur = (cur+a)-((a*a)/(2*(cur+a)))


def newton_root(n,r,init=None):
    """
    Esimates of the r-th root of n using the Newton's method, defaults to using integer sqrt as a starting value
    
    Args:
        n -- positive integer to extract the root of
        r -- power of the root to extract
        init -- initial guess for the root
    """
    
    if init == None:
        cur = Fraction(isqrt(n))
    else:
        cur = Fraction(init)
    
    require_integers(["n","r"],[n,r])
    require_geq(["n","init"],[n,cur],0)
    require_geq(["r"],[r],2)
    
    while True:
        yield cur
        cur = cur-(cur**r-n)/(r*cur**(r-1))


def harmonic():
    """
    Partial sums of the Harmonic Series
    OEIS A001008, A002805
    """
    
    f = Fraction(1)
    
    for i in naturals(2):
        yield f
        
        f += Fraction(1,i)


def gen_harmonic(m):
    """
    Partial sums of the Generalized Harmonic Series of Order m
    
    Args:
        m -- exponent for the numerators of the terms
    
    OEIS
    """
    
    require_integers(["m"],[m])
    require_geq(["m"],[m],0)
    
    if m == 0:
        for i in naturals(1):
            yield Fraction(i)
    
    f = Fraction(1)
    
    for i in naturals(2):
        yield f
        
        f += Fraction(1,i**m)


def farey():
    """
    Farey Sequences for each positive integer
    """
    
    for n in naturals(1):
        a,b,c,d = 0,1,1,n
        
        while a <= b:
            yield Fraction(a,b)
            
            k = (n+b)//d
            a,b,c,d = c,d,k*c-a,k*d-b


def stern_brocot():
    """
    Stern-Brocot Tree of Fully Reduced Fractions
    """
    
    def pair_add(A,B):
        return (A[0]+B[0],A[1]+B[1])
    
    row = [(0,1),(1,0)]
    new = []
    
    while True:
        for i in range(len(row)-1):
            t = pair_add(row[i],row[i+1])
            
            yield Fraction(*t)
            
            new.append(row[i])
            new.append(t)
        
        new.append((1,0))
        row, new = new, []


#def bernoulli_numbers(n=-1):
#    
#    if n not in (1,-1):
#        raise Exception("The Bernoulli numbers should be specified by -1 for the negative version or 1 for the positive version")


def fibonacci_generations():
    """
    Irregular triangle of generations of the Fibonacci ordering of the rationals by rows
    """
    
    def generation(n):
        if n == 1:
            return [Fraction(1,1)]
        else:
            L = []
            for i in range(1,n):
                prev = generation(n-1)
                for p in prev:
                    add = Fraction(p.numerator+p.denominator,p.denominator)
                    inv = 1/p
                    L.append(Fraction(add))
                    L.append(Fraction(inv))
                return L
    
    for n in naturals(1):
        yield from iter(generation(n))


def fibonacci_rationals():
    """
    Fibonacci ordering of the rationals
    OEIS A226080, A226081
    """
    
    used = set([])
    gen = [Fraction(1,1)]
    
    while True:
        new = []
        for g in gen:
            if g in used:
                continue
            else:
                yield g
                used.add(g)
                
                add = Fraction(g.numerator+g.denominator,g.denominator)
                inv = 1/g
                
                new.append(add)
                new.append(inv)
        
        gen = new


def dirichlet_terms(A,s):
    """
    Terms of the given Dirichlet series
    """
    
    require_integers(["s"], [s])
    require_geq(["s"], [s], 1)
    require_iterable(["A"],[A])
    
    for n,a in enumerate(A,1):
        f = Fraction(a)/Fraction(n**s)
        yield f


def dirichlet_sums(A,s):
    """
    Partial Sums of the given Dirichlet series
    """
    
    require_integers(["s"], [s])
    require_geq(["s"], [s], 1)
    require_iterable(["A"],[A])
    
    p = Fraction(0)
    
    for f in dirichlet_terms(A,s):
        p += f
        yield p


def taylor_terms(A,c=0):
    """
    Coefficients of each term of the Talyor Series defined by the sequence A and constant c
    """
    
    require_iterable(["A"],[A])
    
    P = [Fraction(1)]
    Q = [Fraction(1),Fraction(-c)]
    
    for a in A:
        yield poly_mult([a],P)
        
        P = poly_mult(Q,P)


def taylor_sums(A,c=0):
    """
    Coefficients of each partial sum of the Talyor Series defined by the sequence A and constant c
    """
    
    require_iterable(["A"],[A])
    
    c = Fraction(c)
    S = [Fraction(0)]
    
    for P in taylor_terms(A,c):
        S = poly_sum(P,S)
        
        yield S


def taylor_convergents(A,c=0,x=0):
    """
    Convergents of the Talyor Series defined by the sequence A and constant c, at x
    """
    
    require_iterable(["A"],[A])
    
    c = Fraction(c)
    x = Fraction(x)
    
    for P in taylor_sums(A,c):
        yield poly_eval(P,x)


def gobel(k=2):
    """
    Göbel's Sequence: Each term is the sum of the kth powers of the previous term divided by the index
    """
    
    require_integers(["k"],[k])
    require_geq(["k"],[k],2)
    
    L = [1,1]
    yield from L
    
    for n in naturals(1):
        x = Fraction(sum(L),n)
        
        yield x
        
        L.append(x**k)

def leibniz_harmonic_triangle(flatten=False):
    """
    Leibniz's Harmonic Triangle: Each term is the sum of the two below\n
    
    Args:
        flatten -- boolean, if True returns one number at a time top to bottom left to right, otherwise returns on row at a time
    
    A003506
    """
    
    if flatten:
        for row in leibniz_harmonic_triangle(flatten=False):
            yield from row
    else:
        row = [1]
        
        for n in naturals(2):
            yield tuple(row)
            
            new_row = [Fraction(1,n)]
            
            for term in row:
                new_row.append(term-new_row[-1])
            
            row = new_row


def prime_coverage():
    """
    The probability that an integer is divisible by the first n primes\n
    OEIS
    """
    
    pr = [Fraction(1,2)]
    
    for p in odd_primes():
        yield pr[-1]
        
        pr.append(pr[-1] + Fraction(1,p) - pr[-1]/Fraction(p))




if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    from Sequences.Simple import sign_sequence
    
    print("\nHarmonic Sequence")
    simple_test(_pretty_fracs(harmonic()),8,
                "1/1, 3/2, 11/6, 25/12, 137/60, 49/20, 363/140, 761/280")
    
    print("\nHarmonic Denominators")
    simple_test(denominators(harmonic()),11,
                "1, 2, 6, 12, 60, 20, 140, 280, 2520, 2520, 27720")
    
    print("\nGeneralized Harmonic Sequence of Order 2")
    simple_test(_pretty_fracs(gen_harmonic(2)),6,
                "1/1, 5/4, 49/36, 205/144, 5269/3600, 5369/3600")
    
    print("\nGeneralized Harmonic Numerators of Order 2")
    simple_test(numerators(gen_harmonic(2)),9,
                "1, 5, 49, 205, 5269, 5369, 266681, 1077749, 9778141")
    
    print("\nIrregular Triangle of Farey Sequences")
    simple_test(_pretty_fracs(farey()),11,
                "0/1, 1/1, 0/1, 1/2, 1/1, 0/1, 1/3, 1/2, 2/3, 1/1, 0/1")
    
    print("\nStern-Brocot Tree")
    simple_test(_pretty_fracs(stern_brocot()),11,
                "1/1, 1/2, 2/1, 1/3, 2/3, 3/2, 3/1, 1/4, 2/5, 3/5, 3/4")
    
    print("\nGenerations of the Fibonacci Production of Rationals")
    simple_test(_pretty_fracs(fibonacci_generations()),11,
                "1/1, 2/1, 1/1, 3/1, 1/2, 2/1, 1/1, 4/1, 1/3, 3/2, 2/1")
    
    print("\nFibonacci Ordering of Rationals")
    simple_test(_pretty_fracs(fibonacci_rationals()),11,
                "1/1, 2/1, 3/1, 1/2, 4/1, 1/3, 3/2, 5/1, 1/4, 4/3, 5/2")
    
    print("\nTerms of Dirichlet Series (-1)^n/(n^2)")
    simple_test(_pretty_fracs(dirichlet_terms(sign_sequence(1),2)),9,
                "1/1, -1/4, 1/9, -1/16, 1/25, -1/36, 1/49, -1/64, 1/81")
    
    print("\nPartial Sums of Dirichlet Series (-1)^n/(n^2)")
    simple_test(_pretty_fracs(dirichlet_sums(sign_sequence(1),2)),6,
                "1/1, 3/4, 31/36, 115/144, 3019/3600, 973/1200")
    
    print("\nExpansion of each Term of a Taylor Series")
    simple_test(_pretty_fracs_tuple(taylor_terms(naturals(1),1)),4,
                "(1/1), (2/1, -2/1), (3/1, -6/1, 3/1), (4/1, -12/1, 12/1, -4/1)")
    
    print("\nExpansion of the Partials Sums of a Taylor Series")
    simple_test(_pretty_fracs_tuple(taylor_sums(naturals(1),1)),4,
                "(1/1), (3/1, -2/1), (6/1, -8/1, 3/1), (10/1, -20/1, 15/1, -4/1)")
    
    print("\nConvergents of a Taylor Series")
    simple_test(taylor_convergents(naturals(1),1,0),10,
                "1, 3, 6, 10, 15, 21, 28, 36, 45, 55")
    
    print("\nPositive Rationals")
    simple_test(_pretty_fracs(positive_rationals()),11,
                "1/1, 2/1, 3/1, 3/2, 4/1, 4/3, 5/1, 5/2, 5/3, 5/4, 6/1")
    
    print("\nBabylonian Convergents of √2")
    simple_test(babylonian_sqrt(2),5,
                "1, 3/2, 17/12, 577/408, 665857/470832")
    
    print("\nBakhshali Convergents of √2")
    simple_test(bakhshali_sqrt(2),3,
                "1, 17/12, 665857/470832")
    
    print("\nNewton Convergents of Cube Root of 2")
    simple_test(newton_root(2,3),4,
                "1, 4/3, 91/72, 1126819/894348")
    
    print("\nGöbel's Sequence (noninteger at term 43)")
    simple_test(gobel(),10,
                "1, 1, 2, 3, 5, 10, 28, 154, 3520, 1551880")
    
    print("\nLeibniz's Harmonic Triangle")
    simple_test(_pretty_fracs_tuple(leibniz_harmonic_triangle()),4,
                "(1/1), (1/2, 1/2), (1/3, 1/6, 1/3), (1/4, 1/12, 1/12, 1/4)")
    
    print("\nChance of Being Divisible by any of the first n primes")
    simple_test(_pretty_fracs(prime_coverage()),7,
                "1/2, 2/3, 11/15, 27/35, 61/77, 809/1001, 13945/17017")
    
    