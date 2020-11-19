from itertools import cycle, count
from math import comb

def permutation_cauchy(line,T,index=0):
    """
    Produce a permutation of T using Cauchy notation
    """
    
    new = []
    
    for pos in line:
        new.append(T[pos-index])
    
    return tuple(new)


def permutation_cycle(cyc,T,index=0):
    """
    Produce a permutation of T using cycle notation
    """
    
    cyc = cyc + (cyc[0],)
    new = list(T[:])
    
    for pos in range(len(cyc)-1):
        new[cyc[pos+1]-index] = cyc[pos]
    
    return tuple(new)


def comb_to_int(C):
    """
    Given a combination in descending order return to associated integer
    """
    
    for i in range(len(C)-1):
        if C[i] <= C[i+1]:
            raise Exception("Elements of C must be given in strictly decreasing order")
    
    L = [comb(c,i) for c,i in zip(C,range(len(C),0,-1))]
    
    return sum(L)


def int_to_comb(n,k):
    """
    Given an integer return the associated combination
    """
    
    if k == 0:
        return ()
    
    for c in count(1):
        if comb(c,k) > n:
            return (c-1,) + int_to_comb(n-comb(c-1,k),k-1)


def comb_to_vector(C,n=None,index=0):
    """
    Convert a combination (in any order) to an index vector in ascending order
    
    Args:
        C -- iterable containing the combination
        n -- number of elements to include in the vector
        index -- 0 or 1, number to start counting from
    """
    
    if index not in (0,1):
        raise ValueError("The index must be 0 or 1")
    
    if index == 0:
        if n == None:
            n = max(C)+1
        V = [0]*n
        for c in C:
            if c < index:
                raise ValueError("No element can be less than the index value 0")
            V[c-1] = 1
    
    if index == 1:
        if n == None:
            n = max(C)
        V = [0]*n
        for c in C:
            if c < index:
                raise ValueError("No element can be less than the index value 1")
            V[c] = 1
    
    return V