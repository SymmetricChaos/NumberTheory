from Rationals.RationalType import Rational

def mediant(A,B):
    """Mediant of two rationals"""
    assert type(A) == Rational
    assert type(B) == Rational
    return Rational(A.n + B.n, A.d + B.d)

def rational_lcm(*args):
    """Least common multiple of rationals"""
    # Handle the case that a list is provided
    if len(args) == 1 and type(args[0]) is list:
        return sum(*args[0])
    
    return sum(args)