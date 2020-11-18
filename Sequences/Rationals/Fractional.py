from Sequences.Simple import naturals
from Sequences.NiceErrorChecking import require_integers, require_geq, require_iterable
from Sequences.MathUtils import poly_mult, poly_sum, poly_eval

from fractions import Fraction
from math import gcd

def numerators(sequence):
    """
    Numerators of a sequence of rational numbers
    Equivalently first value from each pair in a sequence
    """
    
    for f in sequence:
        yield f.numerator


def denominators(sequence):
    """
    Denominators of a sequence of rational numbers
    Equivalently second value from each pair in a sequence
    """
    
    for f in sequence:
        yield f.denominator


def _pretty_fracs(sequence):
    """
    Internal function to show fractions more compactly
    """
    
    for f in sequence:
        a,b = f.numerator,f.denominator
        yield f"{a}/{b}"


def _pretty_fracs_tuple(sequence):
    """
    Internal function to show tuples of fractions more compactly
    """
    
    for f in sequence:
        L = []
        for e in f:
            a,b = e.numerator,e.denominator
            L.append(f"{a}/{b}")
        yield "(" + ", ".join(L) + ")"





def positive_rationals():
    """
    Sequence of all positive rationals
    """
    
    yield Fraction(1)
    
    for n in naturals(1):
        for d in range(1,n):
            if gcd(n,d) == 1:
                yield Fraction(n,d)


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
    