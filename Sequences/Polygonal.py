from Sequences.Naturals import naturals, integers
def polygonal(S):
    """S-Polygonal Numbers"""
    
    for n in naturals():
        
        yield ( n**2*(S-2)-n*(S-4) ) // 2

def gen_polygonal(S):
    """Generalized S-Polygonal Numbers"""
    
    for n in integers():
        
        yield ( n**2*(S-2)-n*(S-4) ) // 2
        
def triangular():
    """Triangular Numbers"""
    out = 0
    
    for n in naturals():
        
        yield out
        
        out += n

def pentagonal():
    """Pentagonal Numbers"""
    for n in naturals():
        out = (3*(n*n)-n)//2
        
        yield out
        

def gen_pentagonal():
    """Generalized Pentagonal Numbers"""
    for z in integers():
        out = (3*(z*z)-z)//2
        
        yield out