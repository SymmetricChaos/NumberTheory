# A schoolyard method for finding the input of a function that gives a 
# particular output. The first guess is the output itself and the step size is 
# half of that. If the function evaluates to more than the value we want then
# subtract the step size and check again. If the sign has flipped divide the
# step size in half and begin again.

def schoolyard_method(x,f,step=1,tol=.01,max_iter=100):
    """When does f(x) = val?"""
    s = step
    for i in range(max_iter):
        
        if abs(f(x)-0) < tol:
            return x
        
        if f(x) > 0:
            x -= s
            if f(x) < 0:
                s = s/2
            
        if f(x) < 0:
            x += s
            if f(x) > 0:
                s = s/2

    return x
	
def schoolyard_method_convergents(x,f,step=1,tol=.01,max_iter=100):
    """When does f(x) = val?"""
    s = step
    for i in range(max_iter):
        yield x
        if abs(f(x)-0) < tol:
            return x
        
        if f(x) > 0:
            x -= s
            if f(x) < 0:
                s = s/2
            
        if f(x) < 0:
            x += s
            if f(x) > 0:
                s = s/2


#from math import log2, sqrt
#
#N = 1835
#def f1(x):
#    return x**2 - N
#
#def f2(x):
#    return 2**x - N
#
#print(schoolyard_method(0,f1))
#print(sqrt(N))
#
#print(schoolyard_method(0,f2))
#print(log2(N))
#
#
