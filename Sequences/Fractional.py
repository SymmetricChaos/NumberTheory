from Sequences.Simple import naturals
from Sequences.NiceErrorChecking import require_integers, require_nonnegative
from math import gcd


def numerators(sequence):
    """
    Numerators of a sequence of rational numbers
    Equivalently first value from each pair in a sequence
    """
    
    for a,b in sequence:
        yield a


def denominators(sequence):
    """
    Denominators of a sequence of rational numbers
    Equivalently second value from each pair in a sequence
    """
    
    for a,b in sequence:
        yield b


def harmonic_pairs():
    """
    Harmonic series by pairs
    OEIS A001008, A002805
    """
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield (n0,d0)
        
        n = n0*i+d0
        d = d0*i
        g = gcd(n,d)
        
        n0, d0 = n//g,d//g


def gen_harmonic_pairs(m):
    """
    Generalized harmonic series of order m by pairs
    
    Args:
        m -- exponent for the numerators of the terms
    
    OEIS
    """
    
    require_integers(["m"],[m])
    require_nonnegative(["m"],[m])
    
    if m == 0:
        for i in naturals(1):
            yield i
    
    n0, d0 = 1,1
    
    for i in naturals(2):
        yield (n0,d0)
        
        n = n0*i+d0
        d = d0*(i**m)
        g = gcd(n,d)
        
        n0, d0 = n//g,d//g





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nHarmonic Sequence")
    simple_test(harmonic_pairs(),5,
                "(1, 1), (3, 2), (11, 6), (25, 12), (137, 60)")
    
    print("\nHarmonic Denominators")
    simple_test(denominators(harmonic_pairs()),11,
                "1, 2, 6, 12, 60, 20, 140, 280, 2520, 2520, 27720")
    
    print("\nGeneralized Harmonic Sequence of Order 2")
    simple_test(gen_harmonic_pairs(2),5,
                "(1, 1), (3, 4), (13, 36), (11, 72), (127, 1800)")
    
    print("\nGeneralized Harmonic Denominators of Order 2")
    simple_test(denominators(gen_harmonic_pairs(2)),9,
                "1, 4, 36, 72, 1800, 10800, 529200, 4233600, 38102400")
    