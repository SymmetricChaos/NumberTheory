from Sequences.Simple import naturals
from math import gcd


def _collatz_step(n):
    if n % 2 == 1:
        return 3*n+1
    return n//2


def collatz_sequence(n):
    """
    Collatz Sequence of n: Iteratively apply the Collatz function to n
    """
    
    yield n
    
    while n != 1:
        n = _collatz_step(n)
        yield n


def collatz_all():
    """
    All Collatz Sequences: Concatenation of the non-repeating part of each Collatz sequence
    OEIS A070165
    """
    
    for n in naturals(1):
        for c in collatz_sequence(n):
            yield c


# Unknown if any terms are undefined but searches by other suggest this code
# isn't fast enough to ever encounter such a case.
# This algorithm stores a lot of intermediate results for a few percent speed
# increase
def collatz_length():
    """
    Collatz Sequence Lengths: Steps until the Collatz function equals 1 for each positive natural
    OEIS A006577, A008908
    """
    
    D = {}
    
    for i in range(16):
        D[2**i] = i
    
    for n in naturals(1):
        if n in D:
            yield D[n]
        
        else:
            ctr = n
            length = 0
            seen = []
            
            while ctr not in D:
                ctr = _collatz_step(ctr)
                length += 1
                seen.append(ctr)
            
            length = D[ctr] + length
            D[n] = length
            yield D[n]
            
            for num in seen:
                length -= 1
                D[num] = length


def collatz_longest():
    """
    Greatest Collatz Lenth: Positive integers that set a record for length of their Collatz sequence
    OEIS A006877
    """
    
    D = {1 : 0, 2 : 1, 4 : 2}
    
    rec = -1
    
    for n in naturals(1):
        if n not in D:
            ctr = n
            length = 0
            
            while ctr not in D:
                ctr = _collatz_step(ctr)
                length += 1
            
            D[n] = D[ctr] + length
        
        if D[n] > rec:
            yield n
            rec = D[n]


def collatz_highpoint():
    """
    High Point of each Collatz Sequence: Greatest value found in each Collatz sequence
    OEIS 
    """
    
    D = {1 : 1}
    
    yield 1
    
    for n in naturals(2):
        cur_rec = 0
        val = n
        
        while val not in D:
            cur_rec = max(cur_rec,val)
            val = _collatz_step(val)
        
        
        cur_rec = max(cur_rec,val)
        D[n] = max(D[val],cur_rec)
        yield D[n]



def collatz_highwater():
    """
    High-Water Mark of the Collatz Sequences: Record values for the high points of Collatz sequences
    OEIS A006885
    """
    
    D = {1 : 1}
    rec = 0
    yield 1
    
    for n in naturals(2):
        cur_rec = 0
        val = n
        
        while val not in D:
            cur_rec = max(cur_rec,val)
            val = _collatz_step(val)
        
        
        cur_rec = max(cur_rec,val)
        D[n] = max(D[val],cur_rec)
        if cur_rec > rec:
            yield D[n]
            rec = cur_rec


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





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Recaman's Sequence")
    simple_test(recaman(),10,
                "0, 1, 3, 6, 2, 7, 13, 20, 12, 21")
    
    print("\nLength of the Collatz Sequences")
    simple_test(collatz_length(),10,
                "0, 1, 7, 2, 5, 8, 16, 3, 19, 6")
    
    print("\nHighly Collatz Numbers")
    simple_test(collatz_longest(),10,
                "1, 2, 3, 6, 7, 9, 18, 25, 27, 54")
    
    print("\nAll Collatz Sequences")
    simple_test(collatz_all(),10,
                "1, 2, 1, 3, 10, 5, 16, 8, 4, 2")
    
    print("\nCollatz Sequence of 163")
    simple_test(collatz_sequence(163),10,
                "163, 490, 245, 736, 368, 184, 92, 46, 23, 70")
    
    print("\nCollatz High Point")
    simple_test(collatz_highpoint(),10,
                "1, 2, 16, 4, 16, 16, 52, 8, 52, 16")
    
    print("\nCollatz High Water Marks")
    simple_test(collatz_highwater(),10,
                "1, 2, 16, 52, 160, 9232, 13120, 39364, 41524, 250504")
    
    print("\nIntegers that represent the Cantor pairing function a of fully reduced proper fraction")
    simple_test(cantor_pairs(),10,
                "8, 13, 18, 19, 26, 32, 33, 34, 41, 43")
