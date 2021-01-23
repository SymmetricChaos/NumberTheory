from fractions import Fraction
from math import gcd, isqrt, ceil

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


def frac_to_engel(F):
    """
    Take a type can can be coerced to a Fraction and return the Engel expansion
    Finite generator
    """
    
    F = Fraction(F)
    
    u = F
    
    while u != 0:
        a = ceil(1/u)
        yield a
        u = (u*a)-1


def frac_to_engel_egyption(F):
    """
    Take a type can can be coerced to a Fraction and return the Egyptian fraction representation as calculated from the Engel expansion as a tuple
    """
    
    out = []
    pr = 1
    u = Fraction(F)
    
    while u != 0:
        a = ceil(1/u)
        u = (u*a)-1
        pr *= a
        out.append(Fraction(1,pr))
    
    return tuple(out)


def frac_greedy_egyption(F):
    """
    Take a type can can be coerced to a Fraction and return the greedy Egyptian fraction representation as a tuple
    """
    
    out = []
    u = Fraction(F)
    
    return tuple(out)



if __name__ == '__main__':
    engel = [i for i in frac_to_engel(Fraction(47,40))]
    print("\nEngel Expansion of 47/40")
    print(engel)
    
    engel_egypt =  frac_to_engel_egyption(Fraction(47,40))
    print("\nEngel's Egyptian Fraction for 47/40")
    print(engel_egypt)