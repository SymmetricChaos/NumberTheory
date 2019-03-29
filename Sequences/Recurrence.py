def fibonacci_inf():
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+b
        
def lucas_inf():
    a = 2
    b = 1
    
    while True:
        yield a
        a, b = b, a+b

      
def P_fibonacci_inf(P):
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+P*b
        
def PQ_fibonacci_inf(P,Q):
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, Q*a+P*b
        
def P_lucas_inf(P):
    a = 2
    b = P
    
    while True:
        yield a
        a, b = b, a+P*b
        
def PQ_lucas_inf(P,Q):
    a = 2
    b = P
    
    while True:
        yield a
        a, b = b, Q*a+P*b

def pell_inf():
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+2*b

def pell_lucas_inf():
    a = 2
    b = 2
    
    while True:
        yield a
        a, b = b, a+2*b
        
def tribonacci_inf():
    a = 0
    b = 0
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b+c
        
def padovan_inf():
    a = 1
    b = 1
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b
    