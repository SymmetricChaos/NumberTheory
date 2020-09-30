from Sequences.Manipulations import speed_compare, memoize_multiplicative
from itertools import count
from Sequences.MathUtils import jordan_totient


def F_fast(n):
    return jordan_totient(n,1)

def F_slow(n):
    for i in range(10):
        jordan_totient(n,1)
    return jordan_totient(n,1)

def F_fast_mem():
    yield from memoize_multiplicative(F_fast)

def F_fast_dir():
    for n in count(1,1):
        yield F_fast(n)

def F_slow_mem():
    yield from memoize_multiplicative(F_slow)

def F_slow_dir():
    for n in count(1,1):
        yield F_slow(n)

print("Quick Function")
speed_compare([F_fast_mem(),F_fast_dir()],["Memoized","Direct"],n=4000,reps=1)

print("\nSlow Function")
speed_compare([F_slow_mem(),F_slow_dir()],["Memoized","Direct"],n=2000,reps=1)