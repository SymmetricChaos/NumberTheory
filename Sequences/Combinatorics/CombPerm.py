from Sequences.Simple import naturals
from Sequences.Combinatorics.Other import pascal_triangle
from Sequences.Combinatorics.PermutationUtils import permutation_cycle, perm_to_pattern
from Sequences.Manipulations import sequence_slice
from Sequences.MathUtils import sign_of

from math import comb

def permutations(n,k,replace=False,reverse=False,reflect=False,index=0):
    """
    The permutations of length k from a set of n elements, returns tuples in lexicographic order
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
                # Get the suffix by recursion
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


def combinations(n,k,replace=False,reverse=False,reflect=False,colex=False,index=0):
    """
    The combinations of length k from a set of n elements, returns tuples in lexicographic order
    Finite generator
    
    Args:
        n -- int, size of the set to choose from
        k -- int, number of elements chosen
        replace -- bool, results with or without replacement
        reverse -- bool, return results in reverse order
        reflect -- bool, return descending combination rather than ascending
        colex -- bool, return results in colexicographic order, aka prefix order
        index -- 0 or 1, value to start counting from
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    def lex_choose_recur(n,k,depth):
        if depth >= k:
            yield ()
        
        else:
            # To reverse the external order (ie return the 'first' tuple last) reverse the selection order
            S = range(index,n+index)
            if reverse:
                S = reversed(S)
            
            for s in S:
                # Get the suffix by recursion
                for suffix in lex_choose_recur(n,k,depth+1):
                    # We're looking for the lexicographically first representation for each permutation
                    # So if anything in the suffix is less than s it can't be valid
                    if len(suffix) > 0 and min(suffix) < s:
                        continue
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
    
    def colex_choose_recur(n,k,depth):
        if depth >= k:
            yield ()
        
        else:
            S = range(index,n+index)
            if reverse:
                S = reversed(S)
            
            for s in S:
                # Get the prefix by recursion
                for prefix in colex_choose_recur(n,k,depth+1):
                    # We're looking for the colexicographically first representation for each permutation
                    # So if anything in the prefix is greater than s it can't be valid
                    if len(prefix) > 0 and max(prefix) > s:
                        continue
                    if reflect:
                        T = (s,) + prefix
                    else:
                        T = prefix + (s,)
                    
                    if replace:
                        yield T
                    else:
                        if s not in prefix:
                            yield T
    
    if colex:
        yield from colex_choose_recur(n,k,0)
    else:
        yield from lex_choose_recur(n,k,0)


def derangements(n,reverse=False,reflect=False,index=0):
    """
    The derangements of n elements, permutations with no term at its own index, returns tuples in lexicographic order
    Finite generator
    
    Args:
        n -- int, size of the set to choose from
        reverse -- bool, return results in reverse order
        reflect -- bool, reflect each derangement
        index -- 0 or 1, value to start counting from
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    def derange_recur(n,depth):
        if depth >= n:
            yield ()
        
        else:
            # To reverse the external order (ie return the 'first' tuple last) reverse the selection order
            S = range(n)
            if reverse:
                S = reversed(S)
            
            for s in S:
                if s != depth:
                    s += index
                    
                    # Get the suffix by recursion
                    for suffix in derange_recur(n,depth+1):
                        # To reflect the internal order(ie write each tuple 'backward') reverse the joining order
                        if reflect:
                            T = suffix + (s,)
                        else:
                            T = (s,) + suffix
                        
                        if s not in suffix:
                            yield T
    
    yield from derange_recur(n,0)


def circular_permutations(n,k,replace=False,reverse=False,reflect=False,index=0):
    """
    The disctinct circular permutations of length k from a set of n elements, returns tuples in lexicographic order
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
    
    def partial_permute_recur(n,k,depth):
        if depth >= k:
            yield ()
        
        else:
            # To reverse the external order (ie return the 'first' tuple last) reverse the selection order
            S = range(1+index,1+n+index)
            if reverse:
                S = reversed(S)
            
            for s in S:
                # Get the suffix by recursion
                for suffix in partial_permute_recur(n,k,depth+1):
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
    
    for P in partial_permute_recur(n-1,k-1,0):
        if reflect:
            yield P + (index,)
        else:
            yield (index,) + P


def alternating_permutations(n,k,replace=False,reverse=False,reflect=False,index=0):
    """
    The alternating permutations of length k from a set of n elements, returns tuples in lexicographic order\n
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
    
    def is_alternating(P):
        direct = sign_of(P[0]-P[1])
        for i in range(1,len(P)-1):
            if sign_of(P[i]-P[i+1]) == direct:
                return False
        return True
            
    for P in permutations(n,k,reverse=reverse,reflect=reflect,index=index):
        if is_alternating(P):
            yield P


def subsequences(P,k,reverse=False,reflect=False,colex=False):
    """
    All the subsequences of length k contained in P\n
    Finite generator
    
    Args:
        P -- tuple, a permutation
        k -- int, length of subsequences to generate
        reverse -- bool, return results in reverse order
        reflect -- bool, return descending combination rather than ascending
        colex -- bool, return results in colexicographic order, aka prefix order
    """
    
    for p in combinations(len(P),k,reverse=reverse,reflect=reflect,colex=colex):
        yield tuple([P[i] for i in p])


def permutation_patterns(P,k,reverse=False,reflect=False,colex=False,index=0):
    """
    All the permutations patterns of length k contained in P\n
    Finite generator
    
    Args:
        P -- tuple, a permutation
        k -- int, length of patterns to generate
        reverse -- bool, return results in reverse order
        reflect -- bool, return descending combination rather than ascending
        colex -- bool, return results in colexicographic order, aka prefix order
        index -- 0 or 1, value to start counting from
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    for S in subsequences(P,k,reverse=reverse,reflect=reflect,colex=colex):
        yield perm_to_pattern(S,index=index)


def all_permutations(index=0):
    """
    Every permutation on n elements for positive n, returns tuples in lexicographic order
    
    Args:
        index -- 0 or 1, least element
    
    OEIS A030298
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    for n in naturals(1):
        yield from permutations(n,n,index=index)


def all_derangements(index=0):
    """
    Every deragement on n elements for positive n, returns tuples in lexicographic order
    
    Args:
        index -- 0 or 1, least element
    
    OEIS A030298
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    for n in naturals(2):
        yield from derangements(n,index=index)


def adjacent_permutations(n,index=0):
    """
    Permutations on n that ordered so that each differs from the previous by an adjacent transposition\n
    Recursive version of Steinhaus–Johnson–Trotter algorithm\n
    Finite generator
    
    Args:
        n -- positive integer, size of the set
        index -- 0 or 1, least element
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    if n == 1:
        yield (index,)
    
    else:
        direct = -1
        for P in adjacent_permutations(n-1,index=index):
            if direct == 1:
                # Ascending step
                for i in range(n):
                    yield P[:i] + (n+index-1,) + P[i:]
            
            else:
                # Descending step
                for i in range(n-1,-1,-1):
                    yield P[:i] + (n+index-1,) + P[i:]
            
            direct *= -1


def swap_permutations(n,index=0):
    """
    Permutations on n that ordered so that each differs from the previous by a single transposition\n
    Iterative version of Heap's algorithm\n
    Finite generator
    
    Args:
        n -- positive integer, size of the set
        index -- 0 or 1, least element
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    C = [0]*n
    L = [i+index for i in range(n)]
    
    yield tuple(L)
    
    i = 0
    while i < n:
        if C[i] < i:
            if i % 2 == 0:
                L[0], L[i] = L[i], L[0]
            
            else:
                L[C[i]], L[i] = L[i], L[C[i]]
            
            yield tuple(L)
            
            C[i] += 1
            i = 0
        
        else:
            C[i] = 0
            i += 1


# Probably a better way to order these
def odd_permutations(n,index=0,mode="H"):
    """
    The odd permutations on n elements\n
    Finite generator
    
    Args:
        n -- positive integer, size of the set
        index -- 0 or 1, least element
        mode -- "H" or "SJT" to choose algorithm used
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    if mode == "H":
        yield from sequence_slice(swap_permutations(n,index=index),offset=1,step=1)
    elif mode == "SJT":
        yield from sequence_slice(adjacent_permutations(n,index=index),offset=1,step=1)
    else:
        raise Exception("mode must be 'H' (for Heap's Algorithm) or 'SJT' (for the Steinhaus–Johnson–Trotter algorithm)")


def even_permutations(n,index=0,mode="H"):
    """
    The even permutations on n elements\n
    Finite generator
    
    Args:
        n -- positive integer, size of the set
        index -- 0 or 1, least element
        mode -- "H" or "SJT" to choose algorithm used
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
        
    if mode == "H":
        yield from sequence_slice(swap_permutations(n,index=index),offset=0,step=1)
    elif mode == "SJT":
        yield from sequence_slice(adjacent_permutations(n,index=index),offset=0,step=1)
    else:
        raise Exception("mode must be 'H' (for Heap's Algorithm) or 'SJT' (for the Steinhaus–Johnson–Trotter algorithm)")


# Probably a better way to order these
def cyclic_permutations(n,index=0):
    """
    Permutations on n that contain exactly one nontrivial cycle, ordered by underlying cycle\n
    Finite generator
    
    Args:
        n -- positive integer, size of the set
        index -- 0 or 1, least element
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    base = tuple([i+index for i in range(n)])
    
    for i in range(2,n+1):
        for P in circular_permutations(n,i,index=index):
            yield permutation_cycle(P, base, index=index)


def cyclic_derangements(n,index=0):
    """
    Derangements on n that consist of exactly one cycle, ordered by underlying cycle\n
    Finite Generator
    
    Args:
        n -- positive integer, size of the set
        index -- 0 or 1, least element
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    base = tuple([i+index for i in range(n)])
    
    for P in circular_permutations(n,n,index=index):
        yield permutation_cycle(P, base, index=index)


def distinct_permutations(T):
    """
    Given a tuple with possibly repeated elements return the distinct permutations
    """
    
    def should_swap(L, start, cur):
        for i in range(start, cur):
            if L[i] == L[cur]:
                return False
        return True
    
    def distinct_recur(L,pos):
        if pos == len(L)-1:
            yield tuple(L)
        else:
            for i in range(pos, len(L)):
                if should_swap(L, pos, i):
                    L[pos], L[i] = L[i], L[pos]
                    yield from distinct_recur(L, pos + 1)
                    L[pos], L[i] = L[i], L[pos]
    
    yield from distinct_recur(list(T),0)


# def stirling_1():
#     """
#     Stirling Numbers of the First Kind\n
#     OEIS
#     """
    
#     yield 1
    
#     R = [0,1,0]
    
#     for n in naturals(1):
#         new = [0]
#         for k in range(1,n+1):
#             t = -n*R[k-1]+R[k]
#             yield t
#             new.append(t)
#         R = new + [0]


# def stirling_2():
#     """
#     Stirling Numbers of the First Kind\n
#     OEIS
#     """
    
#     yield 1
    
#     R = [0,1,0]
    
#     for n in naturals(1):
#         new = [0]
#         for k in range(1,n+1):
#             t = -n*R[k-1]+R[k]
#             yield t
#             new.append(t)
#         R = new + [0]


# Definitely a more efficent way to do this
def permutation_fixed_points(n,k,replace=False,reverse=False,reflect=False,index=0):
    """
    Permutations on n with exactly k fixed points in lexicographic order
    
    Args:
        n -- int, size of the set to choose from
        k -- int, number of fixed points
        replace -- bool, results with or without replacement
        reverse -- bool, return results in reverse order
        reflect -- bool, reflect each permutation
        index -- 0 or 1, value to start counting permutations from
    
    OEIS A001250
    """
    
    if k > n:
        raise Exception(f"k must be less than or equal to n, cannot have {k} fixed points in a set of {n}")
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    def has_x_fixed(P,x):
        ctr = 0
        for val,pos in enumerate(P,index):
            if val == pos:
                ctr += 1
            if ctr > x:
                return False
        if ctr == x:
            return True
        else:
            return False
    
    for P in permutations(n,n,replace=False,reverse=False,reflect=False,index=0):
        if has_x_fixed(P,k):
            yield P





### COUNTING SEQUENCES ###

def derangement():
    """
    Derangement Numbers: Number of permutations of length n with no element in its original position\n
    OEIS A000166
    """
    
    a,b = 1,0
    
    for n in naturals(1):
        yield a
        
        a, b = b, n * (a+b)


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


def odd_permutation():
    """
    Odd Permutation Numbers: Number of odd permutations of n elements (same as the even permutations for n > 1)\n
    OEIS A001710 (except for first two terms)
    """
    
    yield 0
    yield 0
    yield 1
    
    out = 3
    
    for n in naturals(4):
        yield out
        out = out * n


def recontres():
    """
    Recontres Numbers: Triangle by rows counting numbers of permutations of n elements with k fixed points\n
    OEIS A008290
    """
    
    P = pascal_triangle(flatten=True)
    dr = derangement()
    D = []
    
    for n in naturals():
        D.append(next(dr))
        yield D[-1]
        
        # Skip the next value of P
        next(P)
        
        for k in range(1,n+1):
            yield D[n-k]*next(P)


def alternating_permutation():
    """
    Number of alternating permutations on n\n
    OEIS A001250
    """
    
    yield 1
    yield 1
    
    A = [1,1]
    
    for n in naturals(1):
        a = 0
        for k in range(n+1):
            a += comb(n,k)*A[k]*A[n-k]
        
        yield a
        A.append(a//2)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Combinatoric Counting Sequences")
    print("\nDerangement Numbers")
    simple_test(derangement(),11,
                "1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961")
    
    print("\nEven Permutation Numbers")
    simple_test(even_permutation(),11,
                "1, 1, 1, 3, 12, 60, 360, 2520, 20160, 181440, 1814400")
    
    print("\nOdd Permutation Numbers")
    simple_test(odd_permutation(),11,
                "0, 0, 1, 3, 12, 60, 360, 2520, 20160, 181440, 1814400")
    
    print("\nRecontres Numbers")
    simple_test(recontres(),17,
                "1, 0, 1, 1, 0, 1, 2, 3, 0, 1, 9, 8, 6, 0, 1, 44, 45")
    
    print("\nAlternating Permutation Numbers")
    simple_test(alternating_permutation(),11,
                "1, 1, 2, 4, 10, 32, 122, 544, 2770, 15872, 101042")
    
    # print("\nStirling Numbers of the First Kind")
    # simple_test(stirling_1(),11,
    #             "1, 1, 2, 4, 10, 32, 122, 544, 2770, 15872, 101042")
    
    print("\n\n\nVarious Permutation Generators")
    print("\nAll Finite Permutations")
    simple_test(all_permutations(),6,
                "(0,), (0, 1), (1, 0), (0, 1, 2), (0, 2, 1), (1, 0, 2)")
    
    print("\nAll Finite Derangements")
    simple_test(all_derangements(),4,
                "(1, 0), (1, 2, 0), (2, 0, 1), (1, 0, 3, 2)")
    
    print("\nCyclic Derangements of Four Elements (indexed from 1)")
    simple_test(cyclic_derangements(4,index=1),3,
                "(4, 1, 2, 3), (3, 1, 4, 2), (4, 3, 1, 2)")
    
    print("\nCyclic Permutations of Four Elements (indexed from 1)")
    simple_test(cyclic_permutations(4,index=1),3,
                "(2, 1, 3, 4), (3, 2, 1, 4), (4, 2, 3, 1)")
    
    print("\nPermutations of Three Elements in Steinhaus–Johnson–Trotter Order")
    simple_test(adjacent_permutations(3,index=0),5,
                "(0, 1, 2), (0, 2, 1), (2, 0, 1), (2, 1, 0), (1, 2, 0)")
    
    print("\nPermutations of Three Element in Heap's Order")
    simple_test(swap_permutations(3,index=0),5,
                "(0, 1, 2), (1, 0, 2), (2, 0, 1), (0, 2, 1), (1, 2, 0)")
    
    print("\nEven Permutations of Four Elements (in Heap's Order)")
    simple_test(even_permutations(4,index=0),4,
                "(0, 1, 2, 3), (2, 0, 1, 3), (1, 2, 0, 3), (3, 1, 0, 2)")
    
    print("\nOdd Permutations of Four Elements(in Heap's Order)")
    simple_test(odd_permutations(4,index=0),4,
                "(1, 0, 2, 3), (0, 2, 1, 3), (2, 1, 0, 3), (1, 3, 0, 2)")
    
    print("\nSubsequences of Length 3 from (1,5,7,2,6,3,4)")
    simple_test(subsequences((1,5,7,2,6),3),5,
                "(1, 5, 7), (1, 5, 2), (1, 5, 6), (1, 7, 2), (1, 7, 6)")
    
    print("\nPatterns of Length 3 from (1,5,7,2,6,3,4)")
    simple_test(permutation_patterns((1,5,7,2,6),3),5,
                "(0, 1, 2), (0, 2, 1), (0, 1, 2), (0, 2, 1), (0, 2, 1)")
    
    print("\nPermutations of Four Elements with 2 Fixed Points")
    simple_test(permutation_fixed_points(4,2),3,
                "(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1)")
    
    print("\nDistinct Permutations of (0,1,1,2)")
    simple_test(distinct_permutations((0,1,1,2)),4,
                "(0, 1, 1, 2), (0, 1, 2, 1), (0, 2, 1, 1), (1, 0, 1, 2)")
    
    
    
    print("\n\n\nCombinations of Length 3 From a Set with 5 Elements")
    print("Lexicographc Order")
    simple_test(combinations(5,3),5,
                "(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4)")
    
    print("\nReversed")
    simple_test(combinations(5,3,reverse=True),5,
                "(2, 3, 4), (1, 3, 4), (1, 2, 4), (1, 2, 3), (0, 3, 4)")
    
    print("\nColexicographc Order")
    simple_test(combinations(5,3,colex=True),5,
                "(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 4)")
    
    print("\nReversed")
    simple_test(combinations(5,3,reverse=True,colex=True),5,
                "(2, 3, 4), (1, 3, 4), (0, 3, 4), (1, 2, 4), (0, 2, 4)")
    
    
    
    print("\n\n\nPermutations of Length 3 From a Set with 5 Elements")
    print("Lexicographic Order")
    simple_test(permutations(5,3),5,
                "(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 1), (0, 2, 3)")
    
    print("\nReversed")
    simple_test(permutations(5,3,reverse=True),5,
                "(4, 3, 2), (4, 3, 1), (4, 3, 0), (4, 2, 3), (4, 2, 1)")
    
    print("\nReflected")
    simple_test(permutations(5,3,reflect=True),5,
                "(2, 1, 0), (3, 1, 0), (4, 1, 0), (1, 2, 0), (3, 2, 0)")
    
    print("\nReversed and Reflected")
    simple_test(permutations(5,3,reflect=True,reverse=True),5,
                "(2, 3, 4), (1, 3, 4), (0, 3, 4), (3, 2, 4), (1, 2, 4)")
    
    
    
    print("\n\n\nDerangements of a Set With 4 Elements (indexed from 1)")
    print("Lexicographc Order")
    simple_test(derangements(4,index=1),4,
                "(2, 1, 4, 3), (2, 3, 4, 1), (2, 4, 1, 3), (3, 1, 4, 2)")
    
    print("\nReversed")
    simple_test(derangements(4,reverse=True,index=1),4,
                "(4, 3, 2, 1), (4, 3, 1, 2), (4, 1, 2, 3), (3, 4, 2, 1)")
    
    print("\nReflected")
    simple_test(derangements(4,reflect=True,index=1),4,
                "(3, 4, 1, 2), (1, 4, 3, 2), (3, 1, 4, 2), (2, 4, 1, 3)")
    
    print("\nReversed and Reflected")
    simple_test(derangements(4,reverse=True,reflect=True,index=1),4,
                "(1, 2, 3, 4), (2, 1, 3, 4), (3, 2, 1, 4), (1, 2, 4, 3)")
    
    
    
    print("\n\n\nDistinct Circular Permutation of Length 3 from a Set With 5 Elements")
    print("Lexicographc Order")
    simple_test(circular_permutations(5,3),5,
                "(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 1), (0, 2, 3)")
    
    print("\nReversed")
    simple_test(circular_permutations(5,3,reverse=True),5,
                "(0, 4, 3), (0, 4, 2), (0, 4, 1), (0, 3, 4), (0, 3, 2)")
    
    print("\nReflected")
    simple_test(circular_permutations(5,3,reflect=True),5,
                "(2, 1, 0), (3, 1, 0), (4, 1, 0), (1, 2, 0), (3, 2, 0)")
    
    print("\nReversed and Reflected")
    simple_test(circular_permutations(5,3,reverse=True,reflect=True),5,
                "(3, 4, 0), (2, 4, 0), (1, 4, 0), (4, 3, 0), (2, 3, 0)")
    
    
    
    print("\n\n\nAlternating Permutation of Length 3 from a Set with 4 Elements")
    print("Lexicographc Order")
    simple_test(alternating_permutations(4,3),5,
                "(0, 2, 1), (0, 3, 1), (0, 3, 2), (1, 0, 2), (1, 0, 3)")
    
    print("\nReversed")
    simple_test(alternating_permutations(4,3,reverse=True),5,
                "(3, 1, 2), (3, 0, 2), (3, 0, 1), (2, 3, 1), (2, 3, 0)")
    
    print("\nReflected")
    simple_test(alternating_permutations(4,3,reflect=True),5,
                "(1, 2, 0), (1, 3, 0), (2, 3, 0), (2, 0, 1), (3, 0, 1)")
    
    print("\nReversed and Reflected")
    simple_test(alternating_permutations(4,3,reverse=True,reflect=True),5,
                "(2, 1, 3), (2, 0, 3), (1, 0, 3), (1, 3, 2), (0, 3, 2)")