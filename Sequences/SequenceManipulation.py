from itertools import islice, cycle
from math import prod
from time import time


def offset(sequence,n=0):
    """Skip the first n terms of a sequence"""
    
    for i in range(n):
        next(sequence)
    
    for i in sequence:
        yield i


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
    """
    Standard triangular arrangement of the sequence
    0
    1 2
    3 4 5
    6 7 8 9
    """
    
    ctr = 1
    
    while True:
        L = [next(sequence) for c in range(ctr)]
        ctr += 1
        yield L


def triangle_sums(sequence):
    """Sums of the rows of the standard triangular arrangement of the sequence"""
    
    ctr = 1
    
    while True:
        L = [next(sequence) for c in range(ctr)]
        ctr += 1
        yield sum(L)


def triangle_products(sequence):
    """Products of the rows of the standard triangular arrangement of the sequence"""
    
    ctr = 1
    
    while True:
        L = [next(sequence) for c in range(ctr)]
        ctr += 1
        yield prod(L)


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


def skips(sequence,n):
    """Yields sequence but skipping n terms each time, starts with first element"""
    
    while True:
        yield next(sequence)
        
        for i in range(n):
            next(sequence)


def sequence_apply(sequence,func):
    """Apply some function to each term of a sequence and yield the result"""
    
    for s in sequence:
        yield func(s)


def interleave(*sequences):
    """Interleave some sequences in a round-robin style, interleaving ends if any iterator ends"""
    
    nexts = cycle(iter(s).__next__ for s in sequences)
    
    try:
        for N in nexts:
            yield N()
    
    except StopIteration:
        pass







# For testing purposes
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


def speed_compare(sequences,n,reps=1):
    
    for number,S in enumerate(sequences,1):
        print(f"Sequence {number}")
        
        t0 = time()
        
        for r in range(reps):
            for t in segment(S,n):
                pass
        
        print(time()-t0)