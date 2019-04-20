from Utils import must_be_int,must_be_pos_int

def naturals(n=0):
    """Natural Numbers"""
    
    must_be_pos_int(n=n)
    
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
    
    must_be_int(b=b,n=n)
        
    out = b
    
    while True:
        
        yield out
        
        out += n
        
def geometric(b=1,n=2):
    """Geometric Sequence"""
    
    must_be_pos_int(b=b,n=n)
        
    out = b
    
    while True:
        
        yield out
        
        out *= n
        
def powers(n):
    """Powers of N"""
    must_be_pos_int(n=n)
    
    pw = 1
    
    while True:
        yield pw
        
        pw *= n
        
