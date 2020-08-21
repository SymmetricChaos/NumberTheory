from Simple import naturals


def evil():
    """
    Evil Numbers: Non-negative integers with an even number of 1s in their binary expansion
    OEIS A001969
    """
    
    for n in naturals():
        m = n
        s = 0
        
        while m != 0:
            m,r = divmod(m,2)
            s += r
        
        s = s%2
        
        if s == 0:
            yield n

# Too proud of this clever memoization to delete it but its hard to read, uses
# a lot of memory, and (based on some crude testing) it is at best faster by a 
# fraction of a second if millions of values are needed.
#from collections import deque
# def evil_alt():
#     """
#     Evil Numbers: Non-negative integers with an even number of 1s in their binary expansion
#     OEIS A001969
#     """
#    
#     L = deque([0])
#    
#     yield 0
#    
#     for n in naturals(1):
#        
#         m,r = divmod(n,2)
#        
#         if r == 0:
#             L.popleft()
#        
#         s = (L[0]+r)%2
#         L.append(s)
#        
#         if s == 0:
#             yield n


def odious():
    """
    Odious Numbers: Non-negative integers with an odd number of 1s in their binary expansion
    OEIS A000069
    """
    
    for n in naturals():
        m = n
        s = 0
        
        while m != 0:
            m,r = divmod(m,2)
            s += r
        
        s = s%2
        
        if s == 1:
            yield n


def binary_weight():
    """
    Binary Weight: Count of 1s in the binary expansion of each non-negative integer
    OEIS A000120
    """
    
    for n in naturals():
        s=0
        
        while n != 0:
            n,r = divmod(n,2)
            s += r
        
        yield s


if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Evil Numbers")
    simple_test(evil(),14,
                "0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27")
    
    print("\nOdious Numbers")
    simple_test(odious(),14,
                "1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26")
    
    print("\nBinary Weights")
    simple_test(binary_weight(),14,
                "0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3")