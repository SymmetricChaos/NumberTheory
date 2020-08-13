from Sequences.Simple import naturals, integers, arithmetic
from Sequences.Utils import choose
from math import floor, log2
from Sequences.Primes import primes
from Sequences.NiceErrorChecking import require_integers, require_positive


def polygonal(S):
    """Polygonal Numbers"""
    
    require_integers("S",S)
    require_positive("S",S)
    
    for n in naturals():
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def gen_polygonal(S):
    """Generalized Polygonal Numbers"""
    
    require_integers("S",S)
    require_positive("S",S)
    
    for n in integers():
        yield ( n**2*(S-2)-n*(S-4) ) // 2


def cen_polygonal(S):
    """Centered Polygonal Numbers"""
    
    require_integers("S",S)
    require_positive("S",S)
    
    for n in naturals():
        yield (S*n) // 2 * (n-1)+1


def simplicial(N):
    """Simplicial Numbers: Generalization of triangular numbers to N dimensions"""
    
    require_integers("N",N)
    require_positive("N",N)
    
    yield 0
    
    for n in naturals():
        yield choose(n+N,N)


def perfect_powers():
    """Perfect Powers: Non-negative integers that can be written as a a perfect power"""
    
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
    """Doubly Polygonal Numbers"""
    
    require_integers("S",S)
    require_positive("S",S)
    
    cur = 0
    P = polygonal(S)
    
    for s in polygonal(S):
        skip = s-cur-1
        
        for n in range(skip):
            next(P)
        
        yield next(P)
        
        cur = s


### More efficient calculation for common polygonal numbers ###
def triangular():
    """Triangular Numbers"""
    
    S = 0
    
    for a in naturals():
        yield S
        S += a


def square():
    """Square Numbers"""
    
    S = 0
    
    for a in arithmetic(1,2):
        S += a
        yield S


def pentagonal():
    """Pentagonal Numbers"""
    
    for n in naturals():
        yield (3*n*n-n)//2


def gen_pentagonal():
    """Generalized Pentagonal Numbers"""
    
    for i in integers():
        yield (3*i*i-i)//2
