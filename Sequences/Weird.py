from Sequences.Simple import naturals, arithmetic, sign_sequence
from Sequences.Combinatorics import pascal
from Sequences.Manipulations import sequence_apply

from math import gcd

def recaman():
    """
    Recaman's Sequence: Taking steps of size n for eaching positive integer always going backward unless the result would be less than zero or has alread appeared
    OEIS A005132
    """
    
    used = set([0])
    cur = 0
    
    for n in naturals(1):
        yield cur
        
        if cur - n < 0:
            cur += n
        elif cur - n in used:
            cur += n
        else:
            cur -= n
            
        used.add(cur)


def cantor_pairs():
    """
    Integers that represent the Cantor pairing function a of fully reduced proper fraction
    OEIS A337308
    """
    
    L = []
    
    for b in naturals(1):
        L = sorted(L)
        
        if len(L) > 1:
            while len(L) > 0 and L[0] < (1+b)*(1+b+1)//2+b:
                yield L.pop(0)
        
        for a in range(1,b):
            if gcd(a,b) == 1:
                L.append( (a+b)*(a+b+1)//2+b )


def gcd_numbers():
    """
    Triangle by rows of the GCD for each pair of positive integers
    OEIS A003989
    """
    
    for n in naturals(1):
        for x in range(1,n):
            yield gcd(n,x)


def _eculid_step(a,b):
    if a > b:
        return (a-b,b)
    return (a,b-a)


def gcd_steps():
    """
    Triangle by rows for each pair of positive integers with how long it takes Euclid's GCD algorithm to terminate
    OEIS A072030
    """
    
    for n in naturals(1):
        for x in range(1,n):
            m = n
            ctr = 0
            
            while m != x:
                m,x = _eculid_step(m,x)
                ctr += 1
            
            yield ctr


def nonadditive():
    """
    No term is the sum of any previous distinct pair
    OEIS A033627
    """
    
    yield 1
    yield 2
    
    for a in arithmetic(4,3):
        yield a


# def nongeometric():
#     """
#     Greedy sequence avoiding any three term geometric subsequence
#     OEIS A000452
#     """
#    
#     yield 1
#    
#     L = []
#    
#     third = set([])
#    
#     for n in naturals(2):
#         if n not in third:
#             yield n
#             DO STUFF


def hofstader():
    """
    Solution to a puzzle by Hofstader
    OEIS A005228
    """
    
    diff = 2
    n = 1
    L = set([1])
    
    while True:
        yield n
        
        n += diff
        diff += 1
        L.add(n)
        
        if diff in L:
            diff += 1


def co_hofstader():
    """
    Complementary solution to a puzzle by Hofstader
    OEIS A030124
    """
    
    diff = 2
    n = 1
    L = set([1])
    
    while True:
        yield diff
        
        n += diff
        diff += 1
        L.add(n)
        
        if diff in L:
            diff += 1


def hofstader_Q():
    """
    Hofstader's Q-Sequence: Q(n) = Q(n-Q(n-1)) + Q(n-Q(n-2)), , Q(0) = Q(1) = 1
    OEIS A005185
    """
    
    Q = [1,1]
    
    yield 1
    yield 1
    
    for n in naturals(2):
        Q.append(Q[n-Q[n-1]] + Q[n-Q[n-2]])
        
        yield Q[-1]


def even_odd():
    """
    Positive integers but with odds and evens exchanged
    OEIS A103889
    """
    
    for n,s in zip(naturals(1),sign_sequence(1)):
        yield n+s


def sierpinski():
    """
    Sierpinski's Triangle by Rows
    OEIS A047999
    """
    
    yield from sequence_apply(pascal(),lambda x: x%2)


def lucky():
    """
    Lucky Numbers: Prime-like integers resulting from a modified sieve of Eratosthenes\n
    OEIS A000959
    """
    
    yield 1
    yield 3
    
    # Terms of the sequence and where in the cycle each is
    terms = [3]
    ctrs = [2]
    
    # Update the cycles positions
    # If any cycle has reached zero we're not at a lucky number and no later 
    # cycles will be updated since the value has been sieved out before that
    # number is known
    def update():
        for n,t in enumerate(terms):
            ctrs[n] = (ctrs[n]+1)%t
            if ctrs[n] == 0:
                return False
        return True
    
    # Which lucky number we're currently looking for
    # This sets where the cycle for a newly found lucky number begins
    nth = 3
    
    # Go through the odds greater than 5 looking for lucky numbers
    for o in arithmetic(5,2):
        if update():
            yield o
            
            terms.append(o)
            ctrs.append(nth)
            nth += 1


def selfridge():
    """
    Selfridge's Sequence: Used for parameter selection in Lucas pseudoprime tests\n
    OEIS 
    """
    
    for s,n in zip(sign_sequence(1),arithmetic(5,2)):
        yield s*n





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Recaman's Sequence")
    simple_test(recaman(),15,
                "0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9")
    
    print("\nIntegers that represent the Cantor pairing function a of fully reduced proper fraction")
    simple_test(cantor_pairs(),14,
                "8, 13, 18, 19, 26, 32, 33, 34, 41, 43, 50, 52, 53, 62")
    
    print("\nGCD Numbers")
    simple_test(gcd_numbers(),18,
                "1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1")
    
    print("\nEuclid's GCD Steps")
    simple_test(gcd_steps(),18,
                "1, 2, 2, 3, 1, 3, 4, 3, 3, 4, 5, 2, 1, 2, 5, 6, 4, 4")
    
    print("\nNonadditive")
    simple_test(nonadditive(),15,
                "1, 2, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40")
    
    print("\nHofstader")
    simple_test(hofstader(),14,
                "1, 3, 7, 12, 18, 26, 35, 45, 56, 69, 83, 98, 114, 131")
    
    print("\nCo-Hofstader")
    simple_test(co_hofstader(),15,
                "2, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20")
    
    print("\nFirst Derangement of the Natural Numbers")
    simple_test(even_odd(),16,
                "2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15")
    
    print("\nSierpinski Triangle by Rows")
    simple_test(sierpinski(),18,
                "1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0")
    
    print("\nHofstader's Q-Sequence")
    simple_test(hofstader_Q(),17,
                "1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8, 8, 8, 10, 9, 10")
    
    print("\nLucky Numbers")
    simple_test(lucky(),15,
                "1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63")
    
    print("\nSelfridge's Sequence")
    simple_test(selfridge(),13,
                "5, -7, 9, -11, 13, -15, 17, -19, 21, -23, 25, -27, 29")
    