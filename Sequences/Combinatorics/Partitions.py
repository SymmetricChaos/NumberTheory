from Sequences.Figurate import gen_pentagonal
from Sequences.Simple import naturals, powers, evens
from Sequences.Divisibility import primes
from Sequences.Recurrence import tribonacci
from Sequences.Manipulations import offset
from Sequences.MathUtils import factors, nontrivial_factors

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
    
    elif n == 1:
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


def polite_partitions(n):
    """
    Partitions of n into sums of at least two consecutive naturals
    Finite generator
    """
    
    for x in range(1,n):
        s = (x,)
        
        while sum(s) < n:
            x += 1
            s += (x,)
            
            if sum(s) == n:
                yield s
                break


def politeness():
    """
    Number of polite partitions of each integer. The number of odd factors excluding 1.\n
    OEIS A069283
    """
    
    for n in naturals(1):
        yield len([p for p in factors(n) if p > 1 and p % 2 == 1])


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


def tribonnaci_partitions():
    """
    Unique representation of each natural as a sum of distrinct tribonacci numbers\n
    OEIS
    """
    
    trib = offset(tribonacci(),4)
    T = [1]
    
    yield (0,)
    
    for n in naturals(1):
        if T[-1] < n:
            T.append(next(trib))
        
        out = []
        
        for t in reversed(T):
            if n >= t:
                out.append(t)
                n -= t
            
            if n == 0:
                break
        
        yield tuple(out)


def composition_count():
    """
    Number of compositions (ordered partition) for each natural (2**(n-1) for n > 0)
    OEIS A011782
    """
    
    yield 1
    
    for p in powers(2):
        yield p


def compositions(n):
    """
    All of the compositions (ordered partitions) of n
    Finite generator
    """
    
    if n == 0:
        yield ()
    
    elif n == 1:
        yield (1,)
    
    else:
        yield (n,)
        
        for x in range(1,n):
            for p in partitions(x):
                yield (n-x,) + p
    
    # An interative version of this (using a list as a stack) show the relationship
    # with binary expansions
    # if n == 0:
    #     yield ()
    #
    # else:
    #     for i in range(0,2**(n-1)):
    #         P = [n]
    #        
    #         for pos,val in enumerate(int_to_bits(i,width=n-1),1):
    #             if val:
    #                 P[-1] -= n-pos
    #                 P.append(n-pos)
    #        
    #         yield tuple(P)


def all_compositions():
    """
    All of the compositions (ordered partitions) of each positive natural
    OEIS 
    """
    
    for n in naturals(0):
        yield from compositions(n)


# Potentially memoizeable
def multiplicative_partition():
    """
    Multiplicative Partition Numbers: Number of sets of integers, not including one, that have a product of n\n
    OEIS A001055
    """
    
    def mul_part_recur(n,m=2):
        F = [f for f in factors(n) if f >= m]
        
        if n == 1:
            yield ()
        
        else:
            for f in F:
                for a in mul_part_recur(n//f,f):
                    yield (f,) + a
    
    for n in naturals(1):
        yield len([i for i in mul_part_recur(n)])


def multiplicative_partitions(n):
    """
    Multiplicative Partitions: Sets of integers, not including one, that have a product of n\n
    Finite generator
    """
    
    def mul_part_recur(n,m=2):
        F = [f for f in factors(n) if f >= m]
        
        if n == 1:
            yield ()
        
        else:
            for f in F:
                for a in mul_part_recur(n//f,f):
                    yield (f,) + a
    
    yield from mul_part_recur(n)





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
    
    print("\nPolite Partitions of 100")
    simple_test(polite_partitions(100),2,
                "(9, 10, 11, 12, 13, 14, 15, 16), (18, 19, 20, 21, 22)")
    
    print("\nGoldbach Partitions of the Even Numbers")
    simple_test(even_goldbach_partitions(),7,
                "(2, 2), (3, 3), (3, 5), (5, 5), (3, 7), (5, 7), (7, 7)")
    
    print("\nUnique Representation of Each Natural as a Sum of Tribonacci Numbers")
    simple_test(tribonnaci_partitions(),8,
                "(0,), (1,), (2,), (2, 1), (4,), (4, 1), (4, 2), (7,)")
    
    print("\nNumber of Compositions for Each Natural")
    simple_test(composition_count(),13,
                "1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048")
    
    print("\nCompositions of 5")
    simple_test(compositions(5),12,
                "(5,), (4, 1), (3, 2), (3, 1, 1), (2, 3), (2, 2, 1), (2, 1, 1, 1), (1, 4), (1, 3, 1), (1, 2, 2), (1, 2, 1, 1), (1, 1, 1, 1, 1)")
    
    print("\nSequence of all Compositions")
    simple_test(all_compositions(),7,
                "(), (1,), (2,), (1, 1), (3,), (2, 1), (1, 2)")
    
    print("\nPoliteness of Each Natural")
    simple_test(politeness(),18,
                "0, 0, 1, 0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 3, 0, 1, 2")
    
    print("\nMultiplicative Partitions")
    simple_test(multiplicative_partition(),18,
                "1, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 4, 1, 2, 2, 5, 1, 4")
    
    print("\nMultiplicative Partitions of 12")
    simple_test(multiplicative_partitions(12),14,
                "(2, 2, 3), (2, 6), (3, 4), (12,)")
    