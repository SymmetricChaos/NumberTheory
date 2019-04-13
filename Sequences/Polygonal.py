from Sequences.Simple import naturals, integers
from Sequences.Utils import choose
from math import floor, log2
from Sequences.Primes import primes

def polygonal(S):
    """Polygonal Numbers"""
    
    for n in naturals():
        
        yield ( n**2*(S-2)-n*(S-4) ) // 2

def gen_polygonal(S):
    """Generalized Polygonal Numbers"""
    
    for n in integers():
        
        yield ( n**2*(S-2)-n*(S-4) ) // 2
        
def cen_polygonal(S):
    """Centered Polygonal Numbers"""
    
    for n in naturals():
        yield (S*n)//2 * (n-1)+1
        
def simplicial(D):
    """Simplicial Numbers"""
    
    for n in naturals():
        yield choose(n+D,D)



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
    
# Wrappers for some common polygonal numbers
def triangular():
    """Triangular Numbers"""
    for p in polygonal(3):
        yield p
        
def gen_triangular():
    """Generalized Triangular Numbers"""
    for p in gen_polygonal(3):
        yield p
        
def cen_triangular():
    """Centered Triangular Numbers"""
    for p in cen_polygonal(3):
        yield p
        
def square():
    """Square Numbers"""
    for p in polygonal(4):
        yield p
        
def gen_square():
    """Generalized Square Numbers"""
    for p in gen_polygonal(4):
        yield p
        
def cen_square():
    """Centered Square Numbers"""
    for p in cen_polygonal(4):
        yield p
        
def pentagonal():
    """Pentagonal Numbers"""
    for p in polygonal(5):
        yield p
        
def gen_pentagonal():
    """Generalized Pentagonal Numbers"""
    for p in gen_polygonal(5):
        yield p
        
def cen_pentagonal():
    """Centered Pentagonal Numbers"""
    for p in cen_polygonal(5):
        yield p