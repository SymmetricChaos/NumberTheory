from math import floor, sqrt

# Copy of factorization function from Computation to prevent reference issues
def factorization(n,nontrivial=False):
    """All Unique Factors"""
    
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = floor(sqrt(n))+1
    
    # Either include or don't include trivial factors
    if nontrivial == True:
        L = []
    else:
        L = [1,n]
    
    for i in range(2,lim):
        f,r = divmod(n,i)
        
        if r == 0:
            L.append(i)
            L.append(f)
            
    L = list(set(L))
    L.sort()
    
    return L


# Copy of choose function to prevent reference issues
def choose(n,k):
    """Binomial coefficient"""
    
    if type(n) != int:
        raise TypeError("n must be an integer")
    if type(k) != int:
        raise TypeError("k must be an integer")
    
    if n < k:
        raise ValueError("n cannot be less than k")
    if k < 0:
        raise ValueError("k must be nonnegative")
        
    # Calculate the numerator and denominator seperately in order to avoid loss
    # of precision for large numbers.
    N = 1
    D = 1
    for i in range(1,k+1):
        N *= (n+1-i)
        D *= i
    return N//D


def _bits_to_int(bits):
    """Convert a list of 0s and 1s representing a bigendian binary integer"""
    
    n = 0
    p = 1
    
    for b in bits:
        if b != 0:
            n += p
        
        p *= 2
    
    return n