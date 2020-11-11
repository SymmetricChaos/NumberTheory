from Sequences.MathUtils import nontrivial_factors, all_subsets, int_to_comb
from Sequences.Figurate import gen_pentagonal
from Sequences.Simple import naturals, powers, evens
from Sequences.Divisibility import primes
from Sequences.Manipulations import make_triangle, sequence_apply

from math import comb, prod
from sympy import prime

def derangement():
    """
    Derangement Numbers: Permutations with no element in its original position\n
    OEIS A000166
    """
    
    yield 1
    yield 0
    
    S = [1,0]
    
    for n in naturals(1):
        d = n * (S[0]+S[1])
        S[0], S[1] = S[1], d
        
        yield d


def even_permutation():
    """
    Even Permutation Numbers: Number of even permutations of n elements\n
    OEIS A001710
    """
    
    yield 1
    yield 1
    yield 1
    
    out = 3
    
    for n in naturals(4):
        yield out
        out = out * n


def catalan():
    """
    Catalan Numbers: Number of non-crossing partitions of a set with n elements\n
    OEIS A000108
    """
    C = 1
    
    for n in naturals():
        yield C
        C = C*(4*n+2)//(n+2)


# Building the triangle using only addition and index look ups is about 100 
# times faster than calculating the binomial coefficients directly on my
# machine
# There is probably a way to do this is place
def pascal():
    """
    Pascal's Triangle: Number triangle with binomial coefficients\n
    OEIS A007318
    """
    
    L = [1,0]
    
    while True:
        T = [0]
        
        for i in range(len(L)-1):
            x = L[i]+L[i+1]
            T.append(x)
            yield x
        
        T.append(0)
        L = T


def pascal_triangle():
    """
    Pascal's Triangle by Rows\n
    OEIS A007318
    """
    
    yield from make_triangle(pascal())


# Find a more efficient way to do this
def central_binomial():
    """
    Central Binomial Coefficients: Middle term of the odd rows of Pascal's Triangle
    OEIS A000984
    """
    
    for n in naturals():
        yield comb(2*n,n)


def gould():
    """
    Gould's Sequence: Number of odd values on the nth row of Pascal's Triangle\n
    OEIS A001316
    """
    
    P = pascal()
    
    for n in naturals(1):
        val = 0
        
        for i in range(n):
            if next(P) % 2 == 1:
                val += 1
        
        yield val


# As with Pascal's triangle I found this memoized version to be vastly faster
# than directly calculating the values, which involved both binomial
# coefficients and exponentiation
def eulerian():
    """
    Eulerian Triangle: Triangle with number of permutations of a set with n elements where there are m increases\n
    OEIS A008292
    """
    
    L = [1,0]
    
    for a in naturals(1):
        T = []
        
        for b in range(a):
            x = (a-b)*L[b-1] + (b+1)*L[b]
            T.append(x)
            yield x
        
        T.append(0)
        L = T


def recontres():
    """
    Recontres Numbers: Triangle by rows counting numbers of permutations of n elements with k fixed points
    OEIS A008290
    """
    
    P = pascal()
    dr = derangement()
    D = []
    
    for n in naturals():
        D.append(next(dr))
        yield D[-1]
        
        # Skip the next value of P
        next(P)
        
        for k in range(1,n+1):
            yield D[n-k]*next(P)


def bell():
    """
    Bell Numbers: Number of equivalence classes on a set with n elements\n
    OEIS A000110
    """
    
    R0 = [1]
    R1 = [1,2]
    
    while True:
        yield R0[0]
        R2 = [R1[-1]]
        
        for i in R1:
            R2.append(i+R2[-1])
        
        R0, R1 = R1, R2


def lazy_caterer():
    """
    Lazy Caterer Numbers: Maximum number of pieces produced when cutting a circle with exactly n lines\n
    OEIS A000124
    """
    
    for n in naturals():
        yield (n*(n+1))//2+1


# Generalized cake numbers?
def cake():
    """
    Cake Numbers: Maximum number of pieces produced when cutting a sphere with exactly n planes\n
    OEIS A000125
    """
    
    for n in naturals():
        yield (n*n*n+5*n+6)//6


# Potentially memoizeable
def multiplicative_partition():
    """
    Multiplicative Partition Numbers: Sets of integers, not including one, that have a product of n\n
    OEIS A001055
    """
    
    def all_factorizations_inner(n,m=1):
        F = [f for f in nontrivial_factors(n) if f >= m]
        
        if len(F) == 0:
            yield [n]
        
        else:
            for f in F:
                for a in all_factorizations_inner(n//f,f):
                    yield [f] + a
    
    def num_factorizations(n):
        S = set([(n,)])
        
        for i in all_factorizations_inner(n):
            S.add(tuple(sorted(i)))
        
        return len(S)
    
    for n in naturals(1):
        yield num_factorizations(n)


def lex_permute(n,k,replace=False,reverse=False,reflect=False,index=0):
    """
    The ways to choose permutations of length k from a set of n elements, returns tuples in lexicographic order
    Finite generator
    
    Args:
        n -- int, size of the set to choose from
        k -- int, number of elements chosen
        replace -- bool, results with or without replacement
        reverse -- bool, return results in reverse order
        reflect -- bool, reflect each permutation
        index -- 0 or 1, value to start counting permutations from
    """
    
    if k > n:
        raise Exception(f"k must be less than or equal to n, cannot choose {k} elements from a set of {n}")
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    def permute_recur(n,k,depth):
        if depth >= k:
            yield ()
        
        else:
            # To reverse the external order (ie return the 'first' tuple last) reverse the selection order
            S = range(index,n+index)
            if reverse:
                S = reversed(S)
            
            for s in S:
                # Get the syffux by recursion
                for suffix in permute_recur(n,k,depth+1):
                    # To reflect the internal order(ie write each tuple 'backward') reverse the joining order
                    if reflect:
                        T = suffix + (s,)
                    else:
                        T = (s,) + suffix
                    
                    # If we allow replacement don't check for repetition
                    if replace:
                        yield T
                    else:
                        if s not in suffix:
                            yield T
    
    yield from permute_recur(n,k,0)


def lex_choose(n,k,replace=False,reverse=False,descending=False,index=0):
    """
    The ways to choose combinations of length k from a set of n element, returns tuples in lexicographic order  (aka suffix order)
    Finite generator
    
    Args:
        n -- int, size of the set to choose from
        k -- int, number of elements chosen
        replace -- bool, results with or without replacement
        reverse -- bool, return results in reverse order
        index -- 0 or 1, value to start counting permutations from
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    def choose_recur(n,k,depth):
        if depth >= k:
            yield ()
        
        else:
            # To reverse the external order (ie return the 'first' tuple last) reverse the selection order
            S = range(index,n+index)
            if reverse:
                S = reversed(S)
            
            for s in S:
                # Get the suffix by recursion
                for suffix in choose_recur(n,k,depth+1):
                    # We're looking for the lexicographically first representation for each permutation
                    # So if anything in the suffix is less than s it can't be valid
                    if len(suffix) > 0 and min(suffix) < s:
                        continue
                    if descending:
                        T = suffix + (s,)
                    
                    T = (s,) + suffix
                    # If we allow replacement don't check for repetition
                    if replace:
                        yield T
                    else:
                        if s not in suffix:
                            yield T
    
    yield from choose_recur(n,k,0)


def colex_permute(n,k,replace=False,reverse=False,reflect=False,index=0):
    """
    The ways to choose permutations of length k from a set of n element, returns tuples in colexicographic order, equivalent to lex_order() with reversed = True
    Finite generator
    
    Args:
        n -- int, size of the set to choose from
        k -- int, number of elements chosen
        replace -- bool, results with or without replacement
        reverse -- bool, return results in reverse order
        reflect -- bool, reflect each permutation
        index -- 0 or 1, value to start counting permutations from
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    def choose_recur(n,k,depth):
        if depth >= k:
            yield ()
        
        else:
            S = range(index,n+index)
            if reverse:
                S = reversed(S)
            
            for s in S:
                # Get the prefix by recursion
                for prefix in choose_recur(n,k,depth+1):
                    if reflect:
                        T = (s,) + prefix
                    else:
                        T = prefix + (s,)
                    
                    if replace:
                        yield T
                    else:
                        if s not in prefix:
                            yield T
    
    yield from choose_recur(n,k,0)


def colex_choose(n,k,replace=False,reverse=False,descending=False,index=0):
    """
    The ways to choose combinations of length k from a set of n element, returns tuples in colexicographic order (aka prefix order)
    Finite generator
    
    Args:
        n -- int, size of the set to choose from
        k -- int, number of elements chosen
        replace -- bool, results with or without replacement
        reverse -- bool, return results in reverse order
        index -- 0 or 1, value to start counting permutations from
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    def choose_recur(n,k,depth):
        if depth >= k:
            yield ()
        
        else:
            S = range(index,n+index)
            if reverse:
                S = reversed(S)
            
            for s in S:
                # Get the prefix by recursion
                for prefix in choose_recur(n,k,depth+1):
                    # We're looking for the colexicographically first representation for each permutation
                    # So if anything in the prefix is greater than s it can't be valid
                    if len(prefix) > 0 and max(prefix) > s:
                        continue
                    if descending:
                        T = (s,) + prefix
                        
                    T = prefix + (s,)
                    if replace:
                        yield T
                    else:
                        if s not in prefix:
                            yield T
    
    yield from choose_recur(n,k,0)


def finite_permutations(index=0):
    """
    Every permutation on n elements for positive n, returns tuples in lexicographic order
    
    Args:
        index -- 0 or 1, least element
    
    OEIS A030298
    """
    
    for n in naturals(1):
        yield from lex_permute(n,n,index=index)


def natural_subsets(index=0):
    """
    All subsets of the natural numbers in colexicographic order (aka prefix order)
    
    Args:
        index -- 0 or 1, least element
    
    OEIS
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    yield ()
    yield from all_subsets(naturals(index))


def combinadic(k):
    """
    k-Combinadic Numbers: Natural numbers represented as descending combinations of k elements\n
    OEIS
    """
    
    for n in naturals():
        yield int_to_comb(n,k)


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


def sierpinski_triangle():
    """
    Sierpinski's Triangle by Rows
    OEIS A047999
    """
    
    yield from make_triangle(sequence_apply(pascal(),lambda x: x%2))





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Derangement Numbers")
    simple_test(derangement(),11,
                "1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961")
    
    print("\nCatalan Numbers")
    simple_test(catalan(),11,
                "1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796")
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal(),18,
                "1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10")
    
    print("\nCentral Binomial Coefficients")
    simple_test(central_binomial(),11,
                "1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756")
    
    print("\nGould's Sequence")
    simple_test(gould(),18,
                "1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, 4")
    
    print("\nEulerian Triangle by Rows")
    simple_test(eulerian(),16,
                "1, 1, 1, 1, 4, 1, 1, 11, 11, 1, 1, 26, 66, 26, 1, 1")
    
    print("\nBell Numbers")
    simple_test(bell(),11,
                "1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975")
    
    print("\nLazy Caterer's Numbers")
    simple_test(lazy_caterer(),14,
                "1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92")
    
    print("\nCake Numbers")
    simple_test(cake(),13,
                "1, 2, 4, 8, 15, 26, 42, 64, 93, 130, 176, 232, 299")
    
    print("\nMultiplicative Partitions")
    simple_test(multiplicative_partition(),18,
                "1, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 4, 1, 2, 2, 5, 1, 4")
    
    print("\nEven Permutations")
    simple_test(even_permutation(),11,
                "1, 1, 1, 3, 12, 60, 360, 2520, 20160, 181440, 1814400")
    
    print("\nRecontres Numbers")
    simple_test(recontres(),17,
                "1, 0, 1, 1, 0, 1, 2, 3, 0, 1, 9, 8, 6, 0, 1, 44, 45")
    
    
    print("\n\nThe following are combinations (without repetition) of length 3 from the set {0,1,2,3,4}")
    print("Lexicographc Order")
    simple_test(lex_choose(5,3),5,
                "(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4)")
    
    print("\nReversed")
    simple_test(lex_choose(5,3,reverse=True),5,
                "(2, 3, 4), (1, 3, 4), (1, 2, 4), (1, 2, 3), (0, 3, 4)")
    
    print("\nColexicographc Order")
    simple_test(colex_choose(5,3),5,
                "(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 4)")
    
    print("\nReversed")
    simple_test(colex_choose(5,3,reverse=True),5,
                "(2, 3, 4), (1, 3, 4), (0, 3, 4), (1, 2, 4), (0, 2, 4)")
    
    
    print("\n\nThe following are permutations (without repetition) of length 3 from the set {0,1,2,3,4}")
    print("Lexicographic Order")
    simple_test(lex_permute(5,3),5,
                "(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 1), (0, 2, 3)")
    
    print("\nReversed (equivalent to using the colex_permute() function)")
    simple_test(lex_permute(5,3,reverse=True),5,
                "(4, 3, 2), (4, 3, 1), (4, 3, 0), (4, 2, 3), (4, 2, 1)")
    
    print("\nReflected")
    simple_test(lex_permute(5,3,reflect=True),5,
                "(2, 1, 0), (3, 1, 0), (4, 1, 0), (1, 2, 0), (3, 2, 0)")
    
    print("\nReversed and Reflected")
    simple_test(lex_permute(5,3,reflect=True,reverse=True),5,
                "(2, 3, 4), (1, 3, 4), (0, 3, 4), (3, 2, 4), (1, 2, 4)")
    
    
    print("\n\nAll Finite Permutations")
    simple_test(finite_permutations(),6,
                "(0,), (0, 1), (1, 0), (0, 1, 2), (0, 2, 1), (1, 0, 2)")
    
    print("\nAll Subsets of Natural Numbers")
    simple_test(natural_subsets(),7,
                "(), (0,), (1,), (0, 1), (2,), (0, 2), (1, 2)")
    
    print("\n2-Combinadic Numbers")
    simple_test(combinadic(2),7,
                "(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0)")
    
    print("\nPartition Numbers")
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
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal_triangle(),5,
                "(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1), (1, 4, 6, 4, 1)")
    
    print("\nSierpinski Triangle by Rows")
    simple_test(sierpinski_triangle(),5,
                "(1,), (1, 1), (1, 0, 1), (1, 1, 1, 1), (1, 0, 0, 0, 1)")
    