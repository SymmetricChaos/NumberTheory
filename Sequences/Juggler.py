from Sequences.Simple import naturals
from math import isqrt

def _juggler_step(n):
    if n % 2 == 0:
        return isqrt(n)
    else:
        return isqrt(n*n*n)


def juggler(n):
    """
    Juggler Sequence starting with n\n
    OEIS 
    """
    
    while True:
        yield n
        
        n = _juggler_step(n)


def juggler_map():
    """
    Juggler Map of the Naturals\n
    OEIS 
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
                "0, 0, 1, 6, 2, 5, 2, 4, 2, 7, 7, 4, 7, 4, 7, 6, 3, 4")