from Sequences.Manipulations import speed_compare, memoize_multiplicative
from itertools import count
from Sequences.MathUtils import jordan_totient


def F(n):
    return jordan_totient(n,1)

def F1():
    yield from memoize_multiplicative(F)

def F2():
    for n in count(1,1):
        yield F(n)

speed_compare([F1(),F2()],["Memoized","Direct"],n=10000,reps=3)