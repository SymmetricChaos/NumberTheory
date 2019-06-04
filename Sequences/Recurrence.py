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
    
    assert type(P) == int
    
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+P*b
        
def PQ_fibonacci(P,Q):
    """P,Q-Fibonacci Numbers"""
    
    assert type(P) == int
    assert type(Q) == int
    
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, Q*a+P*b

def P_lucas(P):
    """P-Lucas Numbers"""
    
    assert type(P) == int
    
    a = 2
    b = P
    
    while True:
        yield a
        a, b = b, a+P*b
        
def PQ_lucas(P,Q):
    """P,Q-Lucas Numbers"""
    
    assert type(P) == int
    assert type(Q) == int
    
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

def simple_recurrence(a,b):
    """Fibonnaci Type Sequence Starting with a and b"""
    assert type(a) == int
    assert type(b) == int
    
    while True:
        yield a
        a, b = b, a+b
        
def sylvesters_sequence():
    """Sylvester's Sequence"""
    L = [2]
    
    while True:
        yield L[-1]
        t = 1
        for i in L:
            t *= i
        L.append(t+1)

#def partitions(n):
#    if n == 0:
#        return 1
#    if n < 0:
#        return 0
#    else:
#        s = 0
#        k = 0
#        ctr = 1
#        while True:
#            if ctr % 2 == 1:
#                k += ctr
#            else:
#                k -= ctr
#            pent = k*(3*k-1)//2
#            if pent > n:
#                break
#            s += partitions(n-pent)*(-1)**(k+1)
#            ctr += 1
#            
#    return s
#
#print(partitions(15))