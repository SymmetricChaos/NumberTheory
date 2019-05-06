# The bisection method finds a 

from warnings import warn
from GeneralUtils import sign

def bisection_method(a,b,func,iters=10):
    
    fa = func(a)
    fb = func(b)
    
    if sign(fa) == sign(fb):
        raise Exception("Points must have opposite signs.")
    
    # Guarantee that a is the negative side and b is the positive side
    # This makes it easier to place the new value
    if sign(fa) == 1:
        a,b = b,a
    
    for i in range(iters):
        c = (a+b)/2
        x = func(c)
        if x < 0:
            a = c
        elif x > 0:
            b = c
        elif x == 0:
            return c
        
        
    if abs(func(c)) > .1:
        warn("Abs Err {:.5f}".format(abs(func(c))))
    return c

def bisection_method_convergents(a,b,func,iters=10):
    
    fa = func(a)
    fb = func(b)
    
    if sign(fa) == sign(fb):
        raise Exception("Points must have opposite signs.")
    
    if sign(fa) == 1:
        a,b = b,a
    
    for i in range(iters):
        c = (a+b)/2
        x = func(c)
        if x < 0:
            a = c
        elif x > 0:
            b = c
        yield c

