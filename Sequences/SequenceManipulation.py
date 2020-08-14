

def offset(sequence,offset=0):
    
    for i in range(offset):
        next(sequence)
    
    for i in sequence:
        yield i


# Return some number of values with some offset
def segment(sequence,num_vals=0,offset=0):
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


def show_start(sequence):
    """Values of sequence until value passes 1000 or until 20 values printed"""
    
    part = segment(sequence,20)
    L = []
    
    for i in part:
        L.append(i)
        
        if i > 1000:
            break
        
    print(*L,sep=", ")
        
    print("\n")


def make_triangle(sequence):
    """Standard triangular arrangement of seq"""
    
    ctr = 1
    
    while True:
        L = [next(sequence) for c in range(ctr)]
        ctr += 1
        yield L


def partial_sums(sequence,S=0):
    """Partial sums of the sequence"""
    
    if type(S) != int:
        raise TypeError("S must be an integer")
    
    for term in sequence:
        S += term
        yield S


def partial_products(sequence,S=1):
    """Partial products of the sequence"""
    
    if type(S) != int:
        raise TypeError("S must be an integer")
    
    for term in sequence:
        S *= term
        yield S