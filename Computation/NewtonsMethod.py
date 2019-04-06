def newtons_method(x,f0,f1,iters=10):
    
    t = x
    for i in range(iters):
        t = t-( f0(t) / f1(t) )
    
    return t

def newtons_method_convergents(x,f0,f1,iters=10):
    
    t = x
    for i in range(iters):
        t = t-( f0(t) / f1(t) )
        yield t
