from itertools import islice, cycle, count, zip_longest, chain, accumulate
import operator
from math import prod
from time import time


# Copied from itertools recipies
# Some renamed or slightly modified

# These first few are specifically quick to use interfaces for islice
def sequence_slice(sequence, offset, num_vals, step):
    """Yields sequence but skipping n terms each time, starts with first element"""
    
    islice(sequence, offset, num_vals,step+1)


def segment(sequence,offset=0,num_vals=None):
    """
    Return num_val values from a sequence after skipping offset of them
    If num_vals is left as None all terms after the offset are returned
    """
    
    return islice(sequence, offset, num_vals)


def offset(sequence,offset):
    """Skip the first n terms of a sequence"""
    
    return islice(sequence, offset, 0)


def skips(sequence,step):
    """Yields sequence but skipping n terms each time"""
    
    return islice(sequence, 0, None, step+1)


def chunk_by_n(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def prepend(value, iterator):
    "Prepend a single value in front of an iterator"
    
    return chain([value], iterator)


def sequence_apply(sequence,func):
    """Apply some function to each term of a sequence and yield the result"""
    
    return map(func,sequence)


def interleave(*sequences):
    """Interleave some sequences in a round-robin style, interleaving ends if any iterator ends"""
    
    nexts = cycle(iter(s).__next__ for s in sequences)
    
    try:
        for N in nexts:
            yield N()
    
    except StopIteration:
        pass


def partial_sums(sequence,S=None):
    """Partial sums of the sequence"""
    
    return accumulate(sequence,operator.add,initial=S)


def partial_products(sequence,S=None):
    """Partial products of the sequence"""
    
    return accumulate(sequence,operator.mul,initial=S)









# For testing purposes
def simple_test(sequence,N,check):
    """Check the first few terms of a sequence against a known good source like the OEIS"""
    
    L = [str(i) for i in segment(sequence,0,N)]
    S = ", ".join(L)
    
    if S == check:
        print(S)
    else:
        print("ERROR")
        print(f"Expected:\n{check}")
        print(f"Produced:\n{S}")


def speed_compare(sequences,n,reps=1):
    
    for number,S in enumerate(sequences,1):
        print(f"Sequence {number}")
        
        t0 = time()
        
        for r in range(reps):
            for t in segment(S,n):
                pass
        
        print(time()-t0)





## Other manipulations ##
def make_triangle(sequence):
    """
    Standard triangular arrangement of the sequence
    0
    1 2
    3 4 5
    6 7 8 9
    """
    
    for n in count():
        L = [next(sequence) for c in range(n)]
        yield L


def triangle_sums(sequence):
    """Sums of the rows of the standard triangular arrangement of the sequence"""
    
    for R in make_triangle(sequence):
        yield sum(R)


def triangle_products(sequence):
    """Products of the rows of the standard triangular arrangement of the sequence"""
    
    for R in make_triangle(sequence):
        yield prod(R)
