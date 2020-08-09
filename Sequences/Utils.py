from math import ceil, sqrt

def offset(sequence,offset=0):
    
    for i in range(offset):
        next(sequence)
    
    for i in sequence:
        yield i


# Return some number of values with some offset
def partial(sequence,num_vals=0,offset=0):
    """Return num_val values from a sequence after skipping offset of them"""
    
    if type(num_vals) != int:
        raise Exception("n_vals must be an integer")
    if type(offset) != int:
        raise Exception("offset must be an integer")
            
    if num_vals < 0:
        raise Exception("n_vals must be nonnegative")
    if offset < 0:
        raise Exception("offset must be nonnegative")
    
    
    for i in range(offset):
        next(sequence)
    
    if num_vals == 0:
        for i in sequence:
            yield i
    
    else:
        for i in range(num_vals):
            yield next(sequence)


# Return values from a sequence until it returns a value above some maximum
def seq_max(sequence,max_val=None):
    """Return vals until max_val reached"""
    if type(max_val) != int and type(max_val) != None:
        raise Exception("offset must be an integer or infinite")
    
    if max_val == None:
        max_val = float("inf")
    
    for val in sequence:
        yield val          
        if abs(val) > max_val:
            break

# Print the docstring with the sequence name then the first 20 numbers unless 
# a number greater than 1000 is found
def show_start(sequence):
    """Values of sequence until value passes 1000 or until 20 values printed"""
    
    part = partial(sequence,20)
    
    L = []
    
    for i in part:
        L.append(i)
        if i > 1000:
            break
        
    print(*L,sep=", ")
        
    print("\n")


# Copy of factorization function from Computation to prevent reference issues
def factorization(n,nontrivial=False):
    """All Unique Factors"""
    if type(n) != int:
        raise Exception("n must be an integer") 
    
    lim = ceil(sqrt(n))+1
    
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
    if n < k:
        raise Exception("n cannot be less than k")
    if k < 0:
        raise Exception("k must be nonnegative")
        
    # Calculate the numerator and denominator seperately in order to avoid loss
    # of precision for large numbers.
    N = 1
    D = 1
    for i in range(1,k+1):
        N *= (n+1-i)
        D *= i
    return N//D


def make_triangle(seq,n):
    """First n rows of the triangular arrangement of seq"""
    T = []
    ctr = 1
    for i in range(n):
        L = [next(seq) for c in range(ctr)]
        T.append(L)
        ctr += 1
    return T