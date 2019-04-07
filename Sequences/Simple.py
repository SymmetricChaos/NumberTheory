def naturals(n=0):
    """Natural Numbers"""
    ctr = n
    
    while True:
        yield ctr
        
        ctr += 1
        

def integers():
    """Integers"""
    ctr = 0
    v = 0
    
    while True:
        
        yield v
        
        ctr += 1
        if ctr % 2 == 0:
            v -= ctr
        else:
            v += ctr
        
def arithmetic(b=0,n=1):
    """Arithmetic Sequence"""
    
    if type(b) != int:
        raise Exception("b must be an integer")
    
    if type(n) != int:
        raise Exception("n must be an integer")
        
    out = b
    
    while True:
        
        yield out
        
        ctr += n
        
def geometric(b=1,n=2):
    """Geometric Sequence"""
    
    if type(b) != int:
        raise Exception("b must be an integer")
    
    if type(n) != int:
        raise Exception("n must be an integer")
        
    out = b
    
    while True:
        
        yield out
        
        ctr *= n