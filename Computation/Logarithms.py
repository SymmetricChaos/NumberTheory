# It is straightforward to calculate logorithms by applying some root finding
# method to them. However this can be difficult for large numbers. An
# alternative is to use the property that if log(ab) = log(a) + log(b). If the
# logarithms of the factors of an integer are known it is easy to find the
# logarithm of the number. Since the logarithm function increases slowly there
# is not much loss of accuracy from simply finding a nearby smooth number and
# factoring it.


from math import log2, ceil, sqrt

# A simple method for 
def simple_root(f,val,tol=.01,max_iter=10000):
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

def log_basis(B):
    
    f = lambda x: 2**x
    
    D = {}
    for b in B:
        D[b] = simple_root(f,b,tol=.001)
        
    return D


def prime_factorization(n):
    """Prime Factors with Multiplicity"""
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = ceil(sqrt(n))+1
    L = []
    
    p = 1
    while True:
        p += 1
        while n % p == 0:
            L.append(p)
            n = n // p
            
        if n == 1:
            break
        
        if p > lim:
            L.append(n)
            break
    return L

def find_smooth(n,B):
    while True:
        P = prime_factorization(n)
        if all([i in B for i in P]):
            return P
        n -= 1



def estimate_log(n,D,B):
    
    D = {}
    for b in B:
        D[b] = log2(b)
    
    S = find_smooth(n,B)
    print(S)
    return sum(D[s] for s in S)


B = [2,3,5,7,11,13,17,19]
D = log_basis(B)
for N in range(800,1500,37):
    print(estimate_log(N,D,B))
    print(log2(N))
    print()