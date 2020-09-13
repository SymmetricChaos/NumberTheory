from Sequences.Simple import naturals, evens, powers
from Sequences.Manipulations import offset
from MathUtils import digital_sum, digital_root, repeating_part, digital_prod
from NiceErrorChecking import require_integers, require_geq

def evil():
    """
    Evil Numbers: Non-negative integers with an even number of 1s in their binary expansion\n
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
    Odious Numbers: Non-negative integers with an odd number of 1s in their binary expansion\n
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
    Binary Weight: Count of 1s in the binary expansion of each non-negative integer\n
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
    Binary Weight: Count of 0s in the binary expansion of each non-negative integer\n
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
    Ruler Sequence: Largest power of 2 dividing each positive integer, also height of gradation at each position of an infinite ruler\n
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
    Binary Length: Bits in the binary representation of each non-negative integer\n
    OEIS A070939
    """
    
    yield 1
    yield 1
    
    for n,p in enumerate(offset(powers(2),1),2):
        for i in range(p):
            yield n


def base_length(B=10):
    """
    Binary Length: Symbols in the representation of each non-negative integer in base B\n
    OEIS A070939
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for i in range(B):
        yield 1
    
    for n,p in enumerate(offset(powers(B),1),2):
        for i in range(p):
            yield n


def digital_sums(B=10):
    """
    Digital Sums: Sum of the digits of each non-negative integer in base B\n
    OEIS A007953
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for n in naturals():
        yield digital_sum(n,B)


def digital_roots(B=10):
    """
    Digital Roots: Final value of the iteration of digital sums of each non-negative integer in base b\n
    OEIS A010888
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for n in naturals():
        yield digital_root(n,B)


def digital_prods(B=10):
    """
    Digital Sums: Sum of the digits of each non-negative integer in base B\n
    OEIS A007953
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for n in naturals():
        yield digital_prod(n,B)


def additive_persistence(B=10):
    """
    Additive persistence of each natural number in base B
    OEIS A031286
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for n in naturals():
        ctr = 0
        while digital_sum(n,B) != n:
            ctr += 1
            n = digital_sum(n,B)
        yield ctr


def multiplicative_persistence(B=10):
    """
    Multiplicative persistence of each natural number in base B
    OEIS A031346
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for n in naturals():
        ctr = 0
        while n >= B:
            ctr += 1
            n = digital_prod(n,B)
        yield ctr


def palindrome(B=10):
    """
    Palindrome Numbers: Non-negative integers that are palindromes in base B\n
    OEIS A002113, A006995
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    if B == 10:
        for n in naturals():
            if str(n) == str(n)[::-1]:
                yield n
    
    else:
        for n in naturals():
            m = n
            d = []
            
            while n != 0:
                n,r = divmod(n,B)
                d.append(str(r))
            
            s = "".join(d)
            
            if s == s[::-1]:
                yield m


def fraction_period(B=10):
    """
    Repeating period of each unit fraction in base B\n
    OEIS A007732
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for n in naturals(1):
        yield len(repeating_part(1,n,B))





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
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
    
    print("\nDigital Products (Base 3)")
    simple_test(digital_prods(3),18,
                "0, 1, 2, 0, 1, 2, 0, 2, 4, 0, 0, 0, 0, 1, 2, 0, 2, 4")
    
    print("\nPalindromes (Base 2)")
    simple_test(palindrome(2),15,
                "0, 1, 3, 5, 7, 9, 15, 17, 21, 27, 31, 33, 45, 51, 63")
    
    print("\nRepeating Unit Fraction Length (Base 10)")
    simple_test(fraction_period(10),17,
                "1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 2, 1, 6, 6, 1, 1, 16")
    
    print("\nAdditive Persistence (Base 3)")
    simple_test(additive_persistence(3),18,
                "0, 0, 0, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 3")
    
    print("\nMultiplicative Persistence (Base 3)")
    simple_test(multiplicative_persistence(3),18,
                "0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2")
    