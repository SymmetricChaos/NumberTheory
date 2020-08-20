from Simple import naturals
from collections import deque

# Unsure is this kind of memoization is clever or silly
def evil():
    """
    Evil Numbers: Non-negative integers with an even number of 1s in their binary expansion
    OEIS A001969
    """
    
    L = deque([0])
    
    yield 0
    
    for n in naturals(1):
        
        m,r = divmod(n,2)
        
        if r == 0:
            L.popleft()
        
        s = (L[0]+r)%2
        L.append(s)
        
        if s == 0:
            yield n


def odious():
    """
    Odious Numbers: Non-negative integers with an odd number of 1s in their binary expansion
    OEIS A000069
    """
    
    L = deque([0])
    
    for n in naturals(1):
        
        m,r = divmod(n,2)
        
        if r == 0:
            L.popleft()
        
        s = (L[0]+r)%2
        L.append(s)
        
        if s == 1:
            yield n




if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Evil Numbers")
    simple_test(evil(),14,
                "0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27")
    
    print("\nOdious Numbers")
    simple_test(odious(),14,
                "1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26")