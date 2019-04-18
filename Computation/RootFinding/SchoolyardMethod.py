# A schoolyard method for finding the input of a function that gives a 
# particular output. The first guess is the output itself and the step size is 
# half of that. If the function evaluates to more than the value we want then
# subtract the step size and check again. If the sign has flipped divide the
# step size in half and begin again.

def schoolyard_method(f,val,tol=.01,max_iter=10000):
    """When does f(x) = val?"""
    x = val
    s = x/2
    for i in range(max_iter):
        
        if abs(f(x)-val) < tol:
            return x
        
        if f(x) > val:
            x -= s
            if f(x) < val:
                s = s/2
            
        if f(x) < val:
            x += s
            if f(x) > val:
                s = s/2

    return x
	
def schoolyard_method_convergents(f,val,tol=.01,max_iter=10000):
    """When does f(x) = val?"""
    x = val
    s = x/2
    for i in range(max_iter):
		yield x
        if abs(f(x)-val) < tol:
            return x
        
        if f(x) > val:
            x -= s
            if f(x) < val:
                s = s/2
            
        if f(x) < val:
            x += s
            if f(x) > val:
                s = s/2


#from math import log2, sqrt

#def f1(x):
#    return x**2

#def f2(x):
#    return 2**x

#N = 1835
#print(schoolyard_method(f1,N))
#print(sqrt(N))

#print(schoolyard_method(f2,N))
#print(log2(N))


