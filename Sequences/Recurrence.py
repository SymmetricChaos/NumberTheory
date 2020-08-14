from NiceErrorChecking import require_integers

def fibonacci():
    """Fibonacci Sequence"""
    
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, a+b


def lucas():
    """Lucas Sequence"""
    
    a = 2
    b = 1
    
    while True:
        yield a
        a, b = b, a+b


def PQ_fibonacci(P=1,Q=1):
    """
    P,Q-Fibonacci Sequence
    
    Args:
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["P","Q"],[P,Q])
    
    a = 0
    b = 1
    
    while True:
        yield a
        a, b = b, Q*a+P*b


def PQ_lucas(P=1,Q=1):
    """
    P,Q-Lucas Sequence

    Args:
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["P","Q"],[P,Q])
    
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
    """Tribonacci Sequence"""
    
    a = 0
    b = 0
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b+c


def padovan():
    """Padovan Sequence"""
    
    a = 1
    b = 1
    c = 1
    
    while True:
        yield a
        a, b, c = b, c, a+b


def simple_recurrence(a,b):
    """
    Additive recurrence based relation on two terms
    
    Args:
        a -- first term
        b -- second term
    """
    
    require_integers(["a","b"],[a,b])
    
    while True:
        yield a
        a, b = b, a+b


def PQ_simple_recurrence(a,b,P,Q):
    """
    Additive recurrence based relation on two terms
    
    Args:
        a -- first term
        b -- second term
        P -- multiplier for second addend
        Q -- multiplier for first addend
    """
    
    require_integers(["a","b","P","Q"],[a,b,P,Q])
    
    while True:
        yield a
        a, b = b, Q*a+P*b


def arbitrary_recurrence(S,func):
    """
    Recurrence based sequence given a starting tuple and a function
    
    Args:
        S -- Starting tuple
        func -- A function that takes a tuple with the same length of S and
                returns a tuple of the same length
    """
    
    while True:
        yield S[0]
        S = func(S)


def sylvesters_sequence():
    """Sylvester's Sequence"""
    
    L = [2]
    
    while True:
        yield L[-1]
        t = 1
        
        for i in L:
            t *= i
        
        L.append(t+1)


def leonardo():
    """Leonardo Numbers"""
    
    a,b = 1,1
    
    while True:
        yield a
        a,b = b,a+b+1