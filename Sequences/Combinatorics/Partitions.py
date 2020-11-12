from Sequences.Figurate import gen_pentagonal
from Sequences.Simple import naturals, powers, evens
from Sequences.Divisibility import primes

from math import prod
from sympy import prime

def partition_count():
    """
    Partition Numbers: Number of unique multisets of positive integers with sum n\n
    OEIS A000041
    """
    
    D = [1]
    
    for n in naturals(1):
        yield D[-1]
        
        P = gen_pentagonal()
        next(P)
        
        sign = -1
        k=0
        
        for ctr,i in enumerate(P):
            if n-i < 0:
                D.append(k)
                break
            
            if ctr % 2 == 0:
                sign *= -1
            
            k += sign*D[n-i]


def partitions(n):
    """
    Partitions of n in canonical (reverse lexicographic) order
    Finite generator
    OEIS
    """
    
    if n == 0:
        yield ()
    
    if n == 1:
        yield (1,)
    
    else:
        yield (n,)
        
        for x in range(1,n):
            for p in partitions(x):
                if p[0] <= n-x:
                    yield (n-x,) + p


def all_partitions():
    """
    Partitions of each integer in canonical (reverse lexicographic) order\n
    OEIS A080577
    """
    
    yield ()
    
    for n in naturals(1):
        yield from partitions(n)


def partition_ordering():
    """
    Permutation of the positive integers defined by partition tuples\n
    OEIS A129129
    """
    
    for Q in all_partitions():
        yield prod([prime(i) for i in Q])


def equal_partitions(n):
    """
    Partitions of n with all elements equal in reverse lexicographic order
    Finite generator
    OEIS
    """
    
    if n == 0:
        yield ()
    
    else:
        for x in range(n,0,-1):
            if n%x == 0:
                yield tuple([x]*(n//x))


def power_partitions(n,k):
    """
    Partitions of n into powers of k in reverse lexicographic order
    Finite generator
    """
    
    if n < 0:
        raise ValueError("n must be non-negative")
    if k < 1:
        raise ValueError("k must be positive")
    
    if n == k:
        yield (n,)
    
    if n == 0:
        yield ()
    
    if n == 1:
        yield (1,)
    
    else:
        for p in powers(k):
            if p >= n:
                break
        while p >= k:
            p = p//k
            for S in power_partitions(n-p,k):
                if S[0] <= p:
                    yield (p,) + S


def even_goldbach_partitions():
    """
    Even numbers written as the sum of two primes\n
    OEIS
    """
    
    P = primes()
    L = [next(P)]
    
    for e in evens():
        if e > L[0]:
            L.append(next(P))
        
        for s in L:
            if e-s in L and e-s <= s:
                yield (e-s,s)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Partition Numbers")
    simple_test(partition_count(),15,
                "1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135")
    
    print("\nPartitions of 4")
    simple_test(partitions(4),8,
                "(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)")
    
    print("\nSequence of All Partitions")
    simple_test(all_partitions(),8,
                "(), (1,), (2,), (1, 1), (3,), (2, 1), (1, 1, 1), (4,)")
    
    print("\nPartition Order")
    simple_test(partition_ordering(),16,
                "1, 2, 3, 4, 5, 6, 8, 7, 10, 9, 12, 16, 11, 14, 15, 20")
    
    print("\nEqual Partitions of 6")
    simple_test(equal_partitions(6),16,
                "(6,), (3, 3), (2, 2, 2), (1, 1, 1, 1, 1, 1)")
    
    print("\nBinary Partitions of 6")
    simple_test(power_partitions(6,2),16,
                "(4, 2), (4, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)")
    
    print("\nGoldbach Partitions of the Even Numbers")
    simple_test(even_goldbach_partitions(),7,
                "(2, 2), (3, 3), (3, 5), (5, 5), (3, 7), (5, 7), (7, 7)")
    