from itertools import islice

def offset(sequence,n=0):
    """Skip the first n terms of a sequence"""
    
    for i in range(n):
        next(sequence)
    
    for i in sequence:
        yield i


# Return some number of values with some offset
def segment(sequence,num_vals=0,offset=0):
    """
    Return num_val values from a sequence after skipping offset of them
    If num_vals is left as zero the entire sequence is returned
    """
    
    for i in islice(sequence, offset, num_vals):
        yield i


def show_start(sequence):
    """Values of sequence until value passes 1000 or until 15 values printed"""
    
    part = segment(sequence,15)
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


def partial_operations(sequence,S,operation):
    """Partial values of a sequence using some binary operation"""
    
    if type(S) != int:
        raise TypeError("S must be an integer")
    if not callable(operation):
        raise TypeError("operation must be an function representing a binary operation")
    
    for term in sequence:
        S = operation(S,term)
        yield S


def simple_test(sequence,N,check):
    """Check the first few terms of a sequence against a known good source like the OEIS"""
    
    L = [str(i) for i in segment(sequence,N)]
    S = ", ".join(L)
    
    if S == check:
        print(S)
    else:
        print("ERROR")
        print(f"Expected: {check}")
        print(f"Produced: {S}")


def skips(sequence,n):
    """Yields sequence but skipping n terms each time, starts with first element"""
    
    while True:
        yield next(sequence)
        
        for i in range(n):
            next(sequence)