from Sequences.Simple import naturals, evens, powers
from Sequences.SequenceManipulation import offset
from MathUtils import digital_sum, digital_root

def evil():
    """
    Evil Numbers: Non-negative integers with an even number of 1s in their binary expansion
    OEIS A001969
    """
    
    for n in naturals():
        m = n
        s = 0
        
        while m != 0:
            m,r = divmod(m,2)
            s += r
        
        s = s%2
        
        if s == 0:
            yield n


def odious():
    """
    Odious Numbers: Non-negative integers with an odd number of 1s in their binary expansion
    OEIS A000069
    """
    
    for n in naturals():
        m = n
        s = 0
        
        while m != 0:
            m,r = divmod(m,2)
            s += r
        
        s = s%2
        
        if s == 1:
            yield n


def binary_weight():
    """
    Binary Weight: Count of 1s in the binary expansion of each non-negative integer
    OEIS A000120
    """
    
    for n in naturals():
        s = 0
        
        while n != 0:
            n,r = divmod(n,2)
            s += r
        
        yield s


def co_binary_weight():
    """
    Binary Weight: Count of 0s in the binary expansion of each non-negative integer
    OEIS A023416
    """
    
    yield 1
    
    for n in naturals(1):
        s = 0
        
        while n != 0:
            n,r = divmod(n,2)
            
            if r == 0:
                s += 1
        
        yield s


def ruler():
    """
    Ruler Sequence: Largest power of 2 dividing each positive integer, also height of gradation at each position of an infinite ruler
    OEIS A000120
    """
    
    for e in offset(evens(),1):
        yield 0
        
        for n,p in enumerate(powers(2)):
            if e % p != 0:
                yield n-1
                break


def binary_length():
    """
    Binary Length: Bits in the binary representation of each non-negative integer
    OEIS A070939
    """
    
    yield 1
    yield 1
    
    for n,p in enumerate(offset(powers(2),1),2):
        for i in range(p):
            yield n


def base_length(B):
    """
    Binary Length: Symbols in the representation of each non-negative integer in base B
    """
    
    for i in range(B):
        yield 1
    
    for n,p in enumerate(offset(powers(B),1),2):
        for i in range(p):
            yield n


def digital_sums(B):
    """
    Digital Sums: Sum of the digits of each non-negative integer in base B
    OEIS A007953
    """
    
    for n in naturals():
        yield digital_sum(n,B)


def digital_roots(B):
    """
    Digital Roots: Final value of the iteration of digital sums of each non-negative integer in base b
    OEIS A010888
    """
    
    for n in naturals():
        yield digital_root(n,B)





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Evil Numbers")
    simple_test(evil(),15,
                "0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29")
    
    print("\nOdious Numbers")
    simple_test(odious(),15,
                "1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28")
    
    print("\nBinary Weights")
    simple_test(binary_weight(),18,
                "0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2")
    
    print("\nComplementary Binary Weights")
    simple_test(co_binary_weight(),18,
                "1, 0, 1, 0, 2, 1, 1, 0, 3, 2, 2, 1, 2, 1, 1, 0, 4, 3")
    
    print("\nBinary Lengths")
    simple_test(binary_length(),18,
                "1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5")
    
    print("\nTernary Lengths")
    simple_test(base_length(3),18,
                "1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4")
    
    print("\nRuler Sequence")
    simple_test(ruler(),18,
                "0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 4, 0, 1")
    
    print("\nDigital Sums (Base 3)")
    simple_test(digital_sums(3),18,
                "0, 1, 2, 1, 2, 3, 2, 3, 4, 1, 2, 3, 2, 3, 4, 3, 4, 5")
    
    print("\nDigital Roots (Base 3)")
    simple_test(digital_roots(3),18,
                "0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1")
    