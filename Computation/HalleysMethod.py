# Halley's root finding method requires the first and second derivatives of a
# function to be known in order to find a root. It converges somewhat faster
# than Newton's method.

from warnings import warn

def halleys_method(x,f0,f1,f2,iters=10):
    t = x
    for i in range(iters):
        d0 = f0(t)
        d1 = f1(t)
        d2 = f2(t)
        t = t - ( 2*d0*d1 ) / ( 2*d1**2 - d0*d2 )
    if abs(f0(t)) > .1:
        warn("Abs Err {:.5f}".format(abs(f0(t))))
    return t

def halleys_method_convergents(x,f0,f1,f2,iters=10):
    t = x
    for i in range(iters):
        d0 = f0(t)
        d1 = f1(t)
        d2 = f2(t)
        t = t - ( 2*d0*d1 ) / ( 2*d1**2 - d0*d2 )
        yield t
