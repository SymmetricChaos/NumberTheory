from Sequences.Simple import naturals
from Sequences.Combinatorics.Other import pascal
from Sequences.Combinatorics.PermutationUtils import permutation_cycle
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
    The alternating permutations of length k from a set of n elements, returns tuples in lexicographic order
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
            
    for P in permutations(n,k,replace=replace,reverse=reverse,reflect=reflect,index=index):
        if is_alternating(P):
            yield P


def all_permutations(index=0):
    """
    Every permutation on n elements for positive n, returns tuples in lexicographic order
    
    Args:
        index -- 0 or 1, least element
    
    OEIS A030298
    """
    
    for n in naturals(1):
        yield from permutations(n,n,index=index)


def all_derangements(index=0):
    """
    Every permutation on n elements for positive n, returns tuples in lexicographic order
    
    Args:
        index -- 0 or 1, least element
    
    OEIS A030298
    """
    
    for n in naturals(2):
        yield from derangements(n,index=index)


def adjacent_permutations(n,index=0):
    """
    Permutations on n that ordered so that each differs from the previous by an adjacent transposition
    Recursive version of Steinhaus–Johnson–Trotter algorithm
    """
    
    if n == 1:
        yield (0,)
    else:
        direct = -1
        for P in adjacent_permutations(n-1,index=index):
            if direct == 1:
                # Ascending step
                for i in range(n):
                    yield P[:i] + (n-1,) + P[i:]
            
            else:
                # Descneding step
                for i in range(n-1,-1,-1):
                    yield P[:i] + (n-1,) + P[i:]
            
            direct *= -1


def odd_permutations(n,index=0):
    """
    The odd permutations (created by an odd number of transpositions) on n elements
    Finite generator
    
    OEIS
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
    
    yield from sequence_slice(adjacent_permutations(n,index=index),offset=1,step=1)


def even_permutations(n,index=0):
    """
    The even permutations (created by an even number of transpositions) on n elements
    Finite generator
    
    OEIS
    """
    
    if index not in (0,1):
        raise Exception("index must be 0 or 1")
        
    yield from sequence_slice(adjacent_permutations(n,index=index),offset=0,step=1)


# Probably a better way to order these
def cyclic_permutations(n,index=0):
    """
    Permutations on n that contain exactly one nontrivial cycle, ordered by underlying cycle
    """
    base = tuple([i+index for i in range(n)])
    
    for i in range(2,n+1):
        for P in circular_permutations(n,i,index=index):
            yield permutation_cycle(P, base, index=index)


def cyclic_derangements(n,index=0):
    """
    Derangements on n that consist of exactly one cycle, ordered by underlying cycle
    """
    
    base = tuple([i+index for i in range(n)])
    
    for P in circular_permutations(n,n,index=index):
        yield permutation_cycle(P, base, index=index)





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
    OEIS
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


def alternating_permutation():
    """
    Number of alternating permutations on n
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
    
    print("\Alternating Permutation Numbers")
    simple_test(alternating_permutation(),12,
                "1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521, 353792")
    
    
    
    print("\n\n\nVarious Permutation Generators")
    print("\nAll Finite Permutations")
    simple_test(all_permutations(),6,
                "(0,), (0, 1), (1, 0), (0, 1, 2), (0, 2, 1), (1, 0, 2)")
    
    print("\nAll Finite Derangements")
    simple_test(all_derangements(),4,
                "(1, 0), (1, 2, 0), (2, 0, 1), (1, 0, 3, 2)")
    
    print("\nCyclic Derangements on 4, indexed from 1 for ease of reading")
    simple_test(cyclic_derangements(4,index=1),3,
                "(4, 1, 2, 3), (3, 1, 4, 2), (4, 3, 1, 2)")
    
    print("\nCyclic Permutations on 4, indexed from 1 for ease of reading")
    simple_test(cyclic_permutations(4,index=1),3,
                "(2, 1, 3, 4), (3, 2, 1, 4), (4, 2, 3, 1)")
    
    print("\nPermutations on 3 in Steinhaus–Johnson–Trotter Order")
    simple_test(adjacent_permutations(3,index=1),5,
                "(0, 1, 2), (0, 2, 1), (2, 0, 1), (2, 1, 0), (1, 2, 0)")
    
    print("\nOdd Permutations on 4 (in SJT Order)")
    simple_test(odd_permutations(4,index=1),4,
                "(0, 1, 3, 2), (3, 0, 1, 2), (0, 3, 2, 1), (0, 2, 1, 3)")
    
    print("\nEven Permutations on 4 (in SJT Order)")
    simple_test(even_permutations(4,index=1),4,
                "(0, 1, 2, 3), (0, 3, 1, 2), (3, 0, 2, 1), (0, 2, 3, 1)")
    
    
    
    print("\n\n\nCombinations on 5 of length 3")
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
    
    
    
    print("\n\n\nPermutations on 5 of length 3")
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
    
    
    
    print("\n\n\nDerangements of length 4, indexed from 1 for ease of reading")
    print("Lexicographc Order")
    simple_test(derangements(4,index=1),4,
                "(2, 1, 4, 3), (2, 3, 4, 1), (2, 4, 1, 3), (3, 1, 4, 2)")
    
    print("\nReversed")
    simple_test(derangements(4,reverse=True,index=1),4,
                "(4, 3, 2, 1), (4, 3, 1, 2), (4, 1, 2, 3), (3, 4, 2, 1)")
    
    print("\nReflected (some are not derangements when read left to right)")
    simple_test(derangements(4,reflect=True,index=1),4,
                "(3, 4, 1, 2), (1, 4, 3, 2), (3, 1, 4, 2), (2, 4, 1, 3)")
    
    print("\nReversed and Reflected")
    simple_test(derangements(4,reverse=True,reflect=True,index=1),4,
                "(1, 2, 3, 4), (2, 1, 3, 4), (3, 2, 1, 4), (1, 2, 4, 3)")
    
    
    
    print("\n\n\nDistinct circular permutation on 5 of length 3")
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
    
    
    
    print("\n\n\nAlternating permutation on 4 of length 3")
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
    