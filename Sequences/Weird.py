from Sequences.Simple import naturals, arithmetic
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





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
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
    