from Sequences.MathUtils import nontrivial_factors, all_subsets, int_to_comb
from Sequences.Simple import naturals
from Sequences.Manipulations import make_triangle, sequence_apply

from math import comb


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




if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    
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
    