def fibonacci():
    """Fibonacci Numbers"""
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+b
        
def lucas():
    """Lucas Numbers"""
    a = 2
    b = 1
    
    while True:
        yield a
        a, b = b, a+b

      
def P_fibonacci(P):
    """P-Fibonacci Numbers"""
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+P*b
        
def PQ_fibonacci(P,Q):
    """P,Q-Fibonacci Numbers"""
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, Q*a+P*b

def P_lucas(P):
    """P-Lucas Numbers"""
    a = 2
    b = P
    
    while True:
        yield a
        a, b = b, a+P*b
        
def PQ_lucas(P,Q):
    """P,Q-Lucas Numbers"""
    a = 2
    b = P
    
    while True:
        yield a
        a, b = b, Q*a+P*b

def pell():
    """Pell Numbers"""
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+2*b

def pell_lucas():
    """Pell-Lucas Numbers"""
    a = 2
    b = 2
    
    while True:
        yield a
        a, b = b, a+2*b
        
def tribonacci():
    """Tribonacci Numbers"""
    a = 0
    b = 0
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b+c
        
def padovan():
    """Padovan Numbers"""
    a = 1
    b = 1
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b
    