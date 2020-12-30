from Sequences.Simple import naturals, odds
from math import isqrt

def _juggler_step(n):
    if n % 2 == 0:
        return isqrt(n)
    else:
        return isqrt(n*n*n)


def juggler(n):
    """
    Juggler Sequence starting with n
    """
    
    if n == 0:
        yield 0
    
    if n == 1:
        yield 1
    
    while n != 1:
        yield n
        
        n = _juggler_step(n)


def juggler_all(n):
    """
    Concatenation of all Juggler Sequences
    """
    
    for n in naturals():
        yield from juggler(n)


def juggler_map():
    """
    Juggler Map of the Naturals\n
    OEIS A094683
    """
    
    for n in naturals():
        yield _juggler_step(n)


# As with the Collatz sequences it is unknown if all terms are defined
def juggler_length():
    """
    Juggler Sequence Lengths: Steps until the Juggler Sequence starting at each positive natural reaches 1\n
    OEIS A007320
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
                ctr = _juggler_step(ctr)
                length += 1
                seen.append(ctr)
            
            length = D[ctr] + length
            D[n] = length
            
            yield D[n]
            
            for num in seen:
                length -= 1
                D[num] = length


def juggler_longest():
    """
    Greatest Juggler Length: Positive integers that set a record for length of their Juggler sequence\n
    OEIS A094679
    """
    
    D = {1:0}
    rec = -1
    
    for n in naturals(1):
        ctr = n
        length = 0
        
        while ctr not in D:
            ctr = _juggler_step(ctr)
            length += 1
        
        D[n] = D[ctr] + length
        
        if D[n] > rec:
            yield n
            rec = D[n]


def juggler_highpoint():
    """
    High Point of each Juggler Sequence: Greatest value found in each Juggler sequence\n
    OEIS A025586
    """
    
    D = {1:1}
    
    yield 0
    
    for n in naturals(1):
        cur_rec = 0
        val = n
        
        while val not in D:
            cur_rec = max(cur_rec,val)
            val = _juggler_step(val)
        
        cur_rec = max(cur_rec,val)
        D[n] = max(D[val],cur_rec)
        
        yield D[n]


def juggler_highwater():
    """
    High-Water Mark of the Juggler Sequences: Record values for the high points of Juggler sequences\n
    OEIS A143745
    """
    
    D = {1 : 1}
    rec = 0
    
    yield 1
    
    for n in naturals(2):
        cur_rec = 0
        val = n
        
        while val not in D:
            cur_rec = max(cur_rec,val)
            val = _juggler_step(val)
        
        cur_rec = max(cur_rec,val)
        D[n] = max(D[val],cur_rec)
        
        if cur_rec > rec:
            yield D[n]
            rec = cur_rec


def juggler_dropping_time():
    """
    Dropping Time of the Odd Juggler Sequences: Steps until the Juggler Sequence starting at each odd number is less than the starting value\n
    OEIS A094778
    """
    
    
    for n in odds():
        val = n
        ctr = 0
        
        while val >= n and val != 1:
            ctr += 1
            val = _juggler_step(val)
        
        yield ctr





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nJuggler Sequence Starting with 2051")
    simple_test(juggler(2051),5,
                "2051, 92885, 28308599, 150618238728, 388095")
    
    print("\nJuggler Map")
    simple_test(juggler_map(),16,
                "0, 1, 1, 5, 2, 11, 2, 18, 2, 27, 3, 36, 3, 46, 3, 58")
    
    print("\nJuggler Sequence Lengths")
    simple_test(juggler_length(),18,
                "0, 1, 6, 2, 5, 2, 4, 2, 7, 7, 4, 7, 4, 7, 6, 3, 4, 3")
    
    print("\nGreatest Juggler Lengths")
    simple_test(juggler_longest(),12,
                "1, 2, 3, 9, 19, 25, 37, 77, 163, 193, 1119, 1155")
    
    print("\nJuggler High Points")
    simple_test(juggler_highpoint(),15,
                "0, 1, 2, 36, 4, 36, 6, 18, 8, 140, 36, 36, 36, 46, 36")
    
    print("\nJuggler Highwater Marks")
    simple_test(juggler_highwater(),6,
                "1, 2, 36, 140, 52214, 24906114455136")
    
    print("\nJuggler Dropping Times")
    simple_test(juggler_dropping_time(),18,
                "0, 5, 4, 2, 5, 2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 4, 4")
    