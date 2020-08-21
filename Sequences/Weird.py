from Sequences.Simple import naturals

def _collatz_step(n):
    if n % 2 == 1:
        return 3*n+1
    return n//2


def collatz_sequence(n):
    """
    Collatz Sequence for N
    """
    
    while True:
        yield n
        
        n = _collatz_step(n)


# Unknown if any terms are undefined but searches by other suggest this code
# isn't fast enough to ever encounter such a case.
def collatz():
    """
    Collatz Numbers: Steps until the Collatz map equals 1 for each positive natural
    
    """
    
    D = {1 : 0, 2 : 1, 4 : 2}
    
    
    for n in naturals(1):
        if n in D:
            yield D[n]
        
        else:
            ctr = n
            length = 0
            
            while ctr not in D:
                ctr = _collatz_step(ctr)
                length += 1
            
            D[n] = D[ctr] + length
            yield D[n]


def recaman():
    """
    Recaman's Sequence: Taking steps of size n for eaching positive integer always going backward unless the result would be less than zero or has alread appeared
    A005132
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


if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Recaman's Sequence")
    simple_test(recaman(),10,
                "0, 1, 3, 6, 2, 7, 13, 20, 12, 21")
    
    print("\nCollatz Numbers")
    simple_test(collatz(),10,
                "0, 1, 7, 2, 5, 8, 16, 3, 19, 6")
    
    print("\nCollatz Sequence of 163")
    simple_test(collatz_sequence(163),10,
                "163, 490, 245, 736, 368, 184, 92, 46, 23, 70")