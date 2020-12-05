from Sequences.Simple import naturals
from Sequences.Combinatorics.Factorials import factorials




def relation():
    """
    Number of Binary Relations on n elements
    OEIS A002416
    """
    
    for n in naturals():
        yield 2**(n*n)


def reflexive_relation():
    """
    Number of Reflexive Relations on n elements
    OEIS A053763
    """
    
    for n in naturals():
        yield 2**(n*n-n)


def total_order():
    """
    Number of Total Orders on n elements (same as factorials)
    OEIS A000142
    """
    
    yield from factorials()


def equivalence_relation():
    """
    Number of Equivalence Relations on a set with n elements (same as Bell Numbers)
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




if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nBinary Relations")
    simple_test(relation(),7,
                "1, 2, 16, 512, 65536, 33554432, 68719476736")
    
    print("\nReflexive Relations")
    simple_test(reflexive_relation(),7,
                "1, 1, 4, 64, 4096, 1048576, 1073741824")
    
    print("\nTotal Orders")
    simple_test(total_order(),10,
                "1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880")
    
    print("\nEquivalence Relations")
    simple_test(equivalence_relation(),10,
                "1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147")
    