from Sequences.Simple import naturals, integers
from Sequences.Utils import choose
from math import floor, log2
from Sequences.Primes import primes


def polygonal(S):
    """Polygonal Numbers"""
    
    assert type(S) == int
    assert S > 1
    
    for n in naturals():
        
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def gen_polygonal(S):
    """Generalized Polygonal Numbers"""
    
    assert type(S) == int
    assert S > 1
    
    for n in integers():
        
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def cen_polygonal(S):
    """Centered Polygonal Numbers"""
    
    assert type(S) == int
    assert S > 1
    
    for n in naturals():
        yield (S*n)//2 * (n-1)+1


def simplicial(S):
    """Simplicial Numbers"""
    
    assert type(S) == int
    assert S > 1
    
    yield 0
    
    for n in naturals():
        yield choose(n+S,S)


def perfect_powers():
    """Perfect Powers"""
    
    yield 0
    yield 1
    
    for n in naturals(2):
        
        lim = floor(log2(n))+2
        
        for i in primes():
            ctr = 2
            while True:
                pwr = ctr**i
                if pwr > n:
                    break
                if pwr == n:
                    yield n
                    break
                ctr += 1
            if i > lim:
                break


def doubly_polygonal(S):
    
    cur = 0
    P = polygonal(S)
    
    for s in polygonal(S):
        skip = s-cur-1
        
        for n in range(skip):
            next(P)
        
        yield next(P)
        
        cur = s


###  Wrappers for some common polygonal numbers ###
def triangular():
    """Triangular Numbers"""
    for p in polygonal(3):
        yield p


def square():
    """Square Numbers"""
    for n in naturals():
        yield n*n


def pentagonal():
    """Pentagonal Numbers"""
    for p in polygonal(5):
        yield p


# Used in calculating partitions
def gen_pentagonal():
    """Generalized Pentagonal Numbers"""
    for p in gen_polygonal(5):
        yield p
