from Sequences.Simple import naturals, evens, powers
from Sequences.Manipulations import offset
from Sequences.MathUtils import digital_sum, digital_root, repeating_part, digital_prod, int_to_digits
from Sequences.NiceErrorChecking import require_integers, require_geq


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
            s ^= r
        
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
            s ^= r
        
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


def radix_k_weight(k,B=10):
    """
    Number of time the digit k appears in the base B expansion of each natural\n
    OEIS A000120, A023416, A081603
    """
    
    require_integers(["B","k"],[B,k])
    require_geq(["B"],[B],2)
    require_geq(["k"],[k],0)
    
    for n in naturals():
        s = 0
        
        while n != 0:
            n,r = divmod(n,B)
            
            if r == k:
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
    Additive persistence of each natural number in base B\n
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
    Multiplicative persistence of each natural number in base B\n
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


# This could also be done by generating combinations with repetition and 
# sticking them together which might be faster for large numbers but also would
# be harder to get into numeric order
def palindrome_digits(B=10):
    """
    Palindrome Numbers: Non-negative integers that are palindromes in base B\n
    OEIS A002113, A006995
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    yield (0,)
    
    for n in naturals(1):
        d = []
        l = []
        
        while n != 0:
            n,r = divmod(n,B)
            d.append(r)
            l.append(str(r))
        
        s = "".join(l)
        
        if s == s[::-1]:
            yield tuple(d)


def _plaindrome(n,B):
    prev = B
    d = []
    while n != 0:
        n,r = divmod(n,B)
        if r > prev:
            return []
        d.append(r)
        prev = r
    return reversed(d)


def plaindrome(B=10):
    """
    Plaindrome Numbers: Non-negative integers with their digits nondecreasing in base B\n
    OEIS
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    yield 0
    
    for n in naturals(1):
        if _plaindrome(n,B):
            yield n


def plaindrome_digits(B=10):
    """
    Plaindrome Numbers: Non-negative integers with their digits nondecreasing in base B\n
    OEIS
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    yield (0,)
    
    for n in naturals(1):
        p = _plaindrome(n,B)
        if p:
            yield tuple(p)


def fraction_period(B=10):
    """
    Repeating period of each unit fraction in base B\n
    OEIS A007732
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    for n in naturals(1):
        yield len(repeating_part(1,n,B))


def radix_digits(B=10):
    """
    The digits of each natural number in base B\n
    OEIS
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    yield (0,)
    
    for n in naturals(1):
        yield int_to_digits(n,B)


def repdigit(n,B=10):
    """
    Repdigit Numbers: Numbers that consist entire of the digtit n in base B\n
    OEIS A002275-A002279
    """
    
    require_integers(["n","B"],[n,B])
    require_geq(["B"],[B],2)
    require_geq(["n"],[n],1)
    
    if n >= B:
        raise ValueError("There is no digit {n} in base {B}")
    
    r = n
    
    while True:
        yield r
        r = (r*B)+n


def all_repdigit(B=10):
    """
    All the numbers in base B that use the same digit in every position\n
    OEIS A010785, A048328-A048340
    """
    
    require_integers(["B"],[B])
    require_geq(["B"],[B],2)
    
    nums = [repdigit(n,B) for n in range(1,B)]
    
    yield 0
    
    while True:
        for i in nums:
            yield next(i)


def cantor():
    """
    Cantor Numbers: Naturals that contain no 1s in their ternary expansion\n
    OEIS A005823
    """
    
    for n in naturals():
        D = int_to_digits(n,3)
        if 1 not in D:
            yield n


def stanley():
    """
    Stanley Numbers: Naturals that contain no 2s in their ternary expansion\n
    OEIS A005836
    """
    
    for n in naturals():
        D = int_to_digits(n,3)
        if 2 not in D:
            yield n


def digit_avoiding(d,B=10):
    """
    Naturals that do not contain the digit d in base B\n
    OEIS A005823, A005836
    """
    
    if d >= B:
        raise Exception("d must be less than B")
    
    for n in naturals():
        D = int_to_digits(n,B)
        if d not in D:
            yield n


def digit_including(d,B=10):
    """
    Naturals that do contain the digit d in base B\n
    OEIS
    """
    
    if d >= B:
        raise Exception("d must be less than B")
    
    for n in naturals():
        D = int_to_digits(n,B)
        if d in D:
            yield n


def digit_avoiding_words(d,B=10):
    """
    Naturals that do not contain the digit d in base B, returns tuples\n
    OEIS A005823, A005836
    """
    
    if d >= B:
        raise Exception("d must be less than B")
    
    for n in naturals():
        D = int_to_digits(n,B)
        if d not in D:
            yield D


def digit_including_words(d,B=10):
    """
    Naturals that do contain the digit d in base B, returns tuples\n
    OEIS
    """
    
    if d >= B:
        raise Exception("d must be less than B")
    
    for n in naturals():
        D = int_to_digits(n,B)
        if d in D:
            yield D


def _subseq(subseq, L):
    try:
        l = len(subseq)
    except TypeError:
        l = 1
        subseq = type(L)((subseq,))
    
    for i in range(len(L)):
        if L[i:i+l] == subseq:
            return True
    return False


def sequence_avoiding(S,B=10):
    """
    Naturals that do not include the sequence S as a subsequence of digits in base B
    """
    
    for s in S:
        if s >= B:
            raise Exception("all values in S must be less than D")
    
    l = len(S)
    
    for n in naturals():
        D = int_to_digits(n,B)
        d = len(D)
        if d < l:
            yield n
        
        elif not _subseq(S,D):
            yield n



def sequence_including(S,B=10):
    """
    Naturals that do include the sequence S as a subsequence of digits in base B
    """
    
    for s in S:
        if s >= B:
            raise Exception("all values in S must be less than D")
    
    l = len(S)
    
    for n in naturals():
        D = int_to_digits(n,B)
        d = len(D)
        if d < l:
            continue
        
        elif _subseq(S,D):
            yield n


def sequence_avoiding_words(S,B=10):
    """
    Naturals that do not include the sequence S as a subsequence of digits in base B, returns tuples
    """
    
    for s in S:
        if s >= B:
            raise Exception("all values in S must be less than D")
    
    l = len(S)
    
    for n in naturals():
        D = int_to_digits(n,B)
        d = len(D)
        if d < l:
            yield D
        
        elif not _subseq(S,D):
            yield D


def sequence_including_words(S,B=10):
    """
    Naturals that do include the sequence S as a subsequence of digits in base B, returns tuples
    """
    
    for s in S:
        if s >= B:
            raise Exception("all values in S must be less than D")
    
    l = len(S)
    
    for n in naturals():
        D = int_to_digits(n,B)
        d = len(D)
        if d < l:
            continue
        
        elif _subseq(S,D):
            yield D





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Evil Numbers (Even Number of 1s in Binary Expansion)")
    simple_test(evil(),15,
                "0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29")
    
    print("\nOdious Numbers (Odd Number of 1s in Binary Expansion)")
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
    
    print("\nAdditive Persistence (Base 3)")
    simple_test(additive_persistence(3),18,
                "0, 0, 0, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 3")
    
    print("\nMultiplicative Persistence (Base 3)")
    simple_test(multiplicative_persistence(3),18,
                "0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2")
    
    print("\nPalindromes (Base 2)")
    simple_test(palindrome(2),15,
                "0, 1, 3, 5, 7, 9, 15, 17, 21, 27, 31, 33, 45, 51, 63")
    
    print("\nPalindrome Digits (Base 2)")
    simple_test(palindrome_digits(2),6,
                "(0,), (1,), (1, 1), (1, 0, 1), (1, 1, 1), (1, 0, 0, 1)")
    
    print("\nPlaindromes (Base 3)")
    simple_test(plaindrome(3),16,
                "0, 1, 2, 4, 5, 8, 13, 14, 17, 26, 40, 41, 44, 53, 80, 121")
    
    print("\nPlaindrome Digits (Base 3)")
    simple_test(plaindrome_digits(3),7,
                "(0,), (1,), (2,), (1, 1), (1, 2), (2, 2), (1, 1, 1)")
    
    print("\nRepeating Unit Fraction Length (Base 10)")
    simple_test(fraction_period(10),18,
                "1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 2, 1, 6, 6, 1, 1, 16, 1")
    
    print("\nDigits of Each Natural (Base 3)")
    simple_test(radix_digits(3),7,
                "(0,), (1,), (2,), (1, 0), (1, 1), (1, 2), (2, 0)")
    
    print("\nNumber of 2s in the Base-3 Expansion of Each Natural")
    simple_test(radix_k_weight(2,3),18,
                "0, 0, 1, 0, 0, 1, 1, 1, 2, 0, 0, 1, 0, 0, 1, 1, 1, 2")
    
    print("\nThe Repunit Sequence in Base 10")
    simple_test(repdigit(1), 8,
                "1, 11, 111, 1111, 11111, 111111, 1111111, 11111111")
    
    print("\nThe Rep-2 Sequence in Base 3")
    simple_test(repdigit(2,3), 10,
                "2, 8, 26, 80, 242, 728, 2186, 6560, 19682, 59048")
    
    print("\nAll Base 3 Repdigits")
    simple_test(all_repdigit(3), 13,
                "0, 1, 2, 4, 8, 13, 26, 40, 80, 121, 242, 364, 728")
    
    print("\nCantor Numbers")
    simple_test(cantor(), 15,
                "0, 2, 6, 8, 18, 20, 24, 26, 54, 56, 60, 62, 72, 74, 78")
    
    print("\nStanley Numbers")
    simple_test(stanley(), 15,
                "0, 1, 3, 4, 9, 10, 12, 13, 27, 28, 30, 31, 36, 37, 39")
    
    print("\n3-Avoiding Numbers in Base 5")
    simple_test(digit_avoiding(3,5), 15,
                "0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 14, 20, 21, 22")
    
    print("\n3-Avoiding Words in Base 5")
    simple_test(digit_avoiding_words(3,5), 8,
                "(), (1,), (2,), (4,), (1, 0), (1, 1), (1, 2), (1, 4)")
    
    print("\n3-Including Numbers in Base 5")
    simple_test(digit_including(3,5), 14,
                "3, 8, 13, 15, 16, 17, 18, 19, 23, 28, 33, 38, 40, 41")
    
    print("\n3-Including Words in Base 5")
    simple_test(digit_including_words(3,5), 7,
                "(3,), (1, 3), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)")
    
    print("\n12-Avoiding Numbers in Base 4")
    simple_test(sequence_avoiding((1,2),4), 16,
                "0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16")
    
    print("\n12-Avoiding Words in Base 4")
    simple_test(sequence_avoiding_words((1,2),4), 8,
                "(), (1,), (2,), (3,), (1, 0), (1, 1), (1, 3), (2, 0)")
    
    print("\n12-Avoiding Numbers in Base 4")
    simple_test(sequence_including((1,2),4), 14,
                "6, 22, 24, 25, 26, 27, 38, 54, 70, 86, 88, 89, 90, 91")
    
    print("\n12-Avoiding Words in Base 4")
    simple_test(sequence_including_words((1,2),4), 5,
                "(1, 2), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2)")
    