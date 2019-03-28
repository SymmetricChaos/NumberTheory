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

def pell_inf():
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+2*b
