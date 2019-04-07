# Newton's root finding method it a way of finding where a function equals zero.
# It requires knowing the first derivative of the function.

from warnings import warn

def newtons_method(x,f0,f1,iters=10):
    
    t = x
    for i in range(iters):
        t = t-( f0(t) / f1(t) )
    
    if abs(f0(t)) > .1:
        warn("Abs Err {:.5f}".format(abs(f0(t))))
    return t

def newtons_method_convergents(x,f0,f1,iters=10):
    
    t = x
    for i in range(iters):
        t = t-( f0(t) / f1(t) )
        yield t

