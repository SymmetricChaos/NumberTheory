from Sequences.Simple import naturals
from Sequences.NiceErrorChecking import require_integers, require_geq


def _collatz_step(n):
    q,r = divmod(n,2)
    if r == 0:
        return q
    return 3*n+1


def _reduced_collatz_step(n):
    q,r = divmod(n,2)
    if r == 0:
        return q
    return (3*n+1)//2


def collatz_sequence(n):
    """
    Collatz Sequence of n: Iteratively apply the Collatz function to n
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    yield n
    
    while n != 1:
        n = _collatz_step(n)
        yield n


def reduced_collatz_sequence(n):
    """
    Reduced Collatz Sequence of n: Iteratively apply the Collatz function to n but with an addition division by 2 for odd numbers
    """
    
    require_integers(["n"],[n])
    require_geq(["n"],[n],1)
    
    yield n
    
    while n != 1:
        n = _reduced_collatz_step(n)
        yield n


def collatz_map():
    """
    Map of the Collatz Function\n
    OEIS A006370
    """
    
    for n in naturals():
        yield _collatz_step(n)


def reduced_collatz_map():
    """
    Map of the Collatz Function\n
    OEIS A014682
    """
    
    for n in naturals():
        yield _reduced_collatz_step(n)


def collatz_all():
    """
    All Collatz Sequences: Concatenation of the non-repeating part of each Collatz sequence\n
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
    Collatz Sequence Lengths: Steps until the Collatz function equals 1 for each positive natural\n
    OEIS A006577, A008908
    """
    
    D = {1:0}
    
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
    Greatest Collatz Lenth: Positive integers that set a record for length of their Collatz sequence\n
    OEIS A006877
    """
    
    D = {1 : 0}
    rec = -1
    
    for n in naturals(1):
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
    High Point of each Collatz Sequence: Greatest value found in each Collatz sequence\n
    OEIS A025586
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
    High-Water Mark of the Collatz Sequences: Record values for the high points of Collatz sequences\n
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





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Collatz Map")
    simple_test(collatz_map(),16,
                "0, 4, 1, 10, 2, 16, 3, 22, 4, 28, 5, 34, 6, 40, 7, 46")
    
    print("\nReduced Collatz Map")
    simple_test(reduced_collatz_map(),16,
                "0, 2, 1, 5, 2, 8, 3, 11, 4, 14, 5, 17, 6, 20, 7, 23")
    
    print("\nCollatz Sequence of 11")
    simple_test(collatz_sequence(11),18,
                "11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1")
    
    print("\nReduced Collatz Sequence of 11")
    simple_test(reduced_collatz_sequence(11),18,
                "11, 17, 26, 13, 20, 10, 5, 8, 4, 2, 1")
    
    print("\nLength of the Collatz Sequences")
    simple_test(collatz_length(),16,
                "0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4")
    
    print("\nHighly Collatz Numbers")
    simple_test(collatz_longest(),14,
                "1, 2, 3, 6, 7, 9, 18, 25, 27, 54, 73, 97, 129, 171")
    
    print("\nAll Collatz Sequences")
    simple_test(collatz_all(),17,
                "1, 2, 1, 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 5, 16, 8")
    
    print("\nCollatz High Points")
    simple_test(collatz_highpoint(),14,
                "1, 2, 16, 4, 16, 16, 52, 8, 52, 16, 52, 16, 40, 52")
    
    print("\nCollatz High-Water Marks")
    simple_test(collatz_highwater(),10,
                "1, 2, 16, 52, 160, 9232, 13120, 39364, 41524, 250504")
    