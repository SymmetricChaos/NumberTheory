from Simple import naturals

# Not sure if this is faster but memoization means it is less computation
def evil():
    """
    Evil Numbers: Non-negative integers with an even number of 1s in their binary expansion
    OEIS A001969
    """
    
    L = {0:0}
    
    yield 0
    
    for n in naturals(1):
        s = 0
        m = n
        
        while m != 0:
            m,r = divmod(m,2)
            s += r
            if m in L:
                s = (s+L[m])%2
                break
        
        if s == 0:
            yield n
            L[n] = s


def odious():
    """
    Odious Numbers: Non-negative integers with an odd number of 1s in their binary expansion
    OEIS A000069
    """
    
    L = {1:1}
    
    yield 1
    
    for n in naturals(2):
        s = 0
        m = n
        
        while m != 0:
            m,r = divmod(m,2)
            s += r
            if m in L:
                s = (s+L[m])%2
                break
        
        if s == 1:
            yield n
            L[n] = s




if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Evil Numbers")
    simple_test(evil(),14,
                "0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27")
    
    print("\nOdious Numbers")
    simple_test(odious(),14,
                "1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26")