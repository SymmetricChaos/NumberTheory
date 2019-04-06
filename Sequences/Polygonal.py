from Sequences.Naturals import naturals, integers
from Other.Choose import choose
from Other.PerfectPower import perfect_power

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
    for n in naturals():
        if perfect_power(n):
            yield n


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