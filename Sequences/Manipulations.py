from itertools import islice, cycle, count, zip_longest, chain, accumulate, repeat, compress
from math import comb, prod
import operator
from time import time

from Sequences.MathUtils import prime_power_factorization, prime_factorization, factors

# Many of these are copied from the itertools recipies


## Transform a sequence into another sequence ##
def sequence_slice(sequence, offset, num_vals, step):
    """Yields sequence starting with offset until num_vals are returned skipping step each time"""
    
    return islice(sequence, offset, num_vals,step+1)


def segment(sequence,offset=0,num_vals=None):
    """
    Return num_val values from a sequence after skipping offset of them
    If num_vals is left as None all terms after the offset are returned
    """
    
    return islice(sequence, offset, num_vals)


def offset(sequence,offset):
    """Skip the first n terms of a sequence"""
    
    return islice(sequence, offset, None)


def skips(sequence,step):
    """Yields sequence but skipping n terms each time"""
    
    return islice(sequence, 0, None, step+1)


def binomial_transform(sequence,invert=False):
    """
    Binomial transform (or its inverse) of a sequence
    """
    
    S = []
    
    if invert:
        for n in count():
            S.append(next(sequence))
            out = 0
            
            if n % 2 == 1:
                sign = cycle([-1,1])
            else:
                sign = cycle([1,-1])
            
            for k,s in enumerate(S):
                if s == 0:
                    continue
                
                out += next(sign)*comb(n,k)*s
            
            yield out
    
    else:
        for n in count():
            S.append(next(sequence))
            out = 0
            
            for k,s in enumerate(S):
                out += comb(n,k)*s
            
            yield out


def convolution(sequence1,sequence2):
    """
    Convolution of two sequences
    """
    
    S1 = []
    S2 = []
    
    while True:
        S1.append(next(sequence1))
        S2.append(next(sequence2))
        
        out = 0
        for a,b in zip(S1,reversed(S2)):
            out += a*b
        
        yield out


def dirichlet_convolution(sequence1,sequence2):
    """
    Dirichlet convolution of two sequences
    Domain for both most be positive integers
    """
    
    S1 = []
    S2 = []
    
    for n in count(1,1):
        S1.append(next(sequence1))
        S2.append(next(sequence2))
        
        D = factors(n)
        out = 0
        
        for d in D:
            out += S1[d-1]*S2[n//d-1]
        
        yield out


# def dirichlet_inversion(sequence):


# def mobius_inversion(sequence):


def triangle_sums(sequence):
    """
    Sums of the rows of the standard triangular arrangement of the sequence
    """
    
    for R in make_triangle(sequence):
        yield sum(R)


def triangle_products(sequence):
    """
    Products of the rows of the standard triangular arrangement of the sequence
    """
    
    for R in make_triangle(sequence):
        yield prod(R)


def pairwise_sum(sequence1,sequence2):
    """
    Sum two sequences pairwise
    """
    
    for a,b in zip(sequence1,sequence2):
        yield a+b


def pairwise_prod(sequence1,sequence2):
    """
    Multiply together two sequences pairwise 
    """
    
    for a,b in zip(sequence1,sequence2):
        yield a*b


def pairwise_apply(sequence1,sequence2,func,*args,**kwargs):
    """
    Combine two sequences pairwise using some function
    """
    
    for a,b in zip(sequence1,sequence2):
        yield func(a,b,args,kwargs)


def chunk_by_n(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks
    """
    
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def prepend(value, iterator):
    """
    Prepend a single value in front of an iterator
    """
    
    return chain([value], iterator)


def sequence_apply(sequence,func):
    """
    Apply some function to each term of a sequence and yield the result
    """
    
    return map(func,sequence)


def lower_bits(sequence,n):
    """Return only the n lowest bits of each term in the sequence"""
    return map(lambda x: x%(2**n), sequence)


def upper_bits(sequence,n):
    """Return only the n highest bits of each term in the sequence"""
    return map(lambda x: (x >> n) % (2**n), sequence)


def interleave(*sequences):
    """Interleave some sequences in a round-robin style, interleaving ends if any iterator ends"""
    
    nexts = cycle(iter(s).__next__ for s in sequences)
    
    try:
        for N in nexts:
            yield N()
    
    except StopIteration:
        pass


def partial_sums(sequence,S=None):
    """
    Partial sums of the sequence
    """
    
    return accumulate(sequence,operator.add,initial=S)


def partial_prods(sequence,S=None):
    """
    Partial products of the sequence
    """
    
    return accumulate(sequence,operator.mul,initial=S)


def differences(sequence):
    """
    Differences of the given sequence
    """
    
    a, b = next(sequence), next(sequence)
    
    while True:
        yield b-a
        
        a,b = b,next(sequence)


def hypersequence(sequence):
    """
    Returns the a(n)th term of the sequence a(n)
    For example if a(n) = 1, 3, 5, 7, 9, 11, 13...
        hypersequence(a(n)) = 1, 5, 9, 13, 17...
    """
    
    L = []
    pr = 0
    
    for n,v in enumerate(sequence,1):
        if pr >= v:
            raise ValueError("Can only create a hypersequence of a sequence that is entirely positive and strictly increasing")
        
        L.append(v)
        
        if n in L:
            yield v
            del L[0]
        
        pr = v


def run_length_encoding(sequence,reverse=False):
    """
    Encodes sequence the length of the runs followed by the number that is repeated
    Alternatively returns the number and then the length of the run
    """
    
    ctr = 0
    cur = next(sequence)
    
    if reverse:
        for i in sequence:
            ctr += 1
            
            if i != cur:
                yield cur
                yield ctr
                
                ctr = 0
                cur = i
        
        yield cur
        yield ctr+1
    
    else:
        for i in sequence:
            ctr += 1
            
            if i != cur:
                yield ctr
                yield cur
                
                ctr = 0
                cur = i
        
        yield ctr+1
        yield cur


def inv_run_length_encoding(sequence,reverse=False):
    """
    Convert a Run Length Encoding to the original sequence
    """
    
    if reverse:
        for a,b in chunk_by_n(sequence,2):
            for i in range(b):
                yield a
    
    else:
        for a,b in chunk_by_n(sequence,2):
            for i in range(a):
                yield b


def run_lengths(sequence):
    """
    Returns the length of the runs in the sequence
    """
    
    ctr = 0
    cur = next(sequence)
    
    for i in sequence:
        ctr += 1
        
        if i != cur:
            yield ctr
            
            ctr = 0
            cur = i
    
    yield ctr+1


def n_rep_a(sequence,rep_sequence):
    """
    Take elements pairwise and repeat the left value as many times as specified by the right argument
    """
    
    for n,a in zip(sequence,rep_sequence):
        yield from repeat(n,a)


def records(sequence):
    
    r = next(sequence)
    yield r
    
    for s in sequence:
        if s > r:
            yield s
            r = s


def permute(sequence,permutation):
    """
    Reorder the sequence according to the permutation.
    The permutation must be a permutation of the non-negative integers or behavior is undefined.
    """
    
    L = []
    
    for pos in permutation:
        while pos > (len(L)-1):
            L.append(next(sequence))
        
        yield L[pos]


def memoize_multiplicative(function):
    """
    Given a multiplicative function over the naturals calculate the values for
    all naturals by evaluating explicitly at prime powers and using the 
    multiplicative property for all others
    WARNING: Currently only useful if the function is extremely expensive to compute
    """
    
    # For any multiplicative function f(1) = 1
    yield 1
    
    D = {}
    
    for n in count(2,1):
        p = prime_power_factorization(n)
        
        if len(p) == 1:
            D[n] = function(n)
        
        yield prod([D[i] for i in p])


def memoize_total_multiplicative(function):
    """
    Given a total multiplicative function over the naturals calculate the 
    values for all naturals by evaluating explicitly at primes and using the 
    multiplicative property for all others
    WARNING: Currently only useful if the function is extremely expensive to compute
    """
    
    # For any multiplicative function f(1) = 1
    yield 1
    
    D = {}
    
    for n in count(2,1):
        p = prime_factorization(n)
        
        if len(p) == 1:
            D[n] = function(n)
        
        yield prod([D[i] for i in p])


def memoize_additive(function):
    """
    Given an additive function over the naturals calculate the values for
    all naturals by evaluating explicitly at prime powers and using the 
    additive property for all others
    WARNING: Currently only useful if the function is extremely expensive to compute
    """
    
    D = {1: function(1)}
    
    for n in count(2,1):
        p = prime_power_factorization(n)
        
        if len(p) == 1:
            D[n] = function(n)
        
        yield sum([D[i] for i in p])+D[1]


def memoize_total_additive(function):
    """
    Given atotal additive function over the naturals calculate the values for
    all naturals by evaluating explicitly at primes and using the additive
    property for all others
    WARNING: Currently only useful if the function is extremely expensive to compute
    """
    
    # For any total additive function f(1) = 0
    yield 0
    
    D = {}
    
    for n in count(2,1):
        p = prime_factorization(n)
        
        if len(p) == 1:
            D[n] = function(n)
        
        yield sum([D[i] for i in p])


# To avoid potential circular reference from Sequences.Primes in following functions
def _primes_copy():
    yield 2
    yield 3
    yield 5
    
    D = { 9: 3, 25: 5 }
    MASK = cycle((1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0))
    MODULOS = frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )
    
    for q in compress(count(7,2),MASK):
        p = D.pop(q, None)
        
        if p is None:
            D[q*q] = q
            yield q
        
        else:
            x = q + 2*p
            
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            
            D[x] = p


def prime_subsequence(sequence):
    """
    Given a monotonically increasing sequence return all the prime elements
    WARNING: Doesn't check for monotonically increasing property
    """
    prime = _primes_copy()
    
    a = next(prime)
    b = next(sequence)
    
    while True:
        if a == b:
            yield a
            
            a = next(prime)
            b = next(sequence)
        
        else:
            if a > b:
                b = next(prime)
            
            if b > a:
                a = next(sequence)





#############
## TESTING ##
#############
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


def speed_compare(sequences,names=[],*,n=1,reps=1):
    
    if names == []:
        names = [f"Sequence {i}" for i in range(1,len(sequences)+1)]
    
    for S,name in zip(sequences,names):
        print(name)
        
        t0 = time()
        
        for r in range(reps):
            for t in islice(S, n):
                pass
        
        print(time()-t0)


def head(sequence,n):
    """
    First n terms of the sequence as a list, not a generator
    """
    
    return [i for i in segment(sequence,0,n)]





##################
## Arrangements ##
##################
def make_triangle(sequence):
    """
    Standard triangular arrangement of the sequence
    0
    1 2
    3 4 5
    6 7 8 9
    """
    
    for n in count(1):
        L = [next(sequence) for c in range(n)]
        yield L


def irregular_array(sequence,row_sequence):
    """
    Display the sequence using some pattern of row lengths
    """
    
    for n in row_sequence:
        L = [next(sequence) for c in range(n)]
        yield L
