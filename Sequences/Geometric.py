from Sequences.Primes import pythagorean_primes
from Sequences.Simple import naturals
from math import gcd

def nonhypotenuse():
    """
    Nonhypotenuse Numbers: Positive integers that cannot be the hypotenuse of a Pythagorean triple\n
    OEIS A004144
    """
    
    for n in naturals(1):
        for p in pythagorean_primes():
            if n % p == 0:
                break
            
            if p > n//2:
                yield n
                break


def primitive_hypotenuse():
    """
    Primitive Hypotenuse Numbers: Positive integers that can be the hypotenuse of a primitive Pythagorean triple\n
    OEIS A008846
    """
    
    L = []
    
    for m in naturals(1):
        lim = m*m+1 # smallest number that can be produced in this round
        
        if m % 2 == 0:
            for n in range(1,m,2):
                if gcd(m,n) == 1:
                    p = m*m+n*n
                    
                    if p not in L:
                        L.append(p)
        
        else:
            for n in range(2,m,2):
                if gcd(m,n) == 1:
                    p = m*m+n*n
                    
                    if p not in L:
                        L.append(p)
        
        L.sort()
        
        for i in L:
            if i > lim:
                break
            
            yield L.pop(0)

def hypotenuse():
    """
    Hypotenuse Numbers: Positive integers which are the hypotenuse of some Pythagoean triple\n
    OEIS A009003
    """
    
    for n in naturals(1):
        for p in pythagorean_primes():
            if n % p == 0:
                yield n
                break
            
            if p > n:
                break





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Nonhypotenuse Numbers")
    simple_test(nonhypotenuse(),10,
                "1, 2, 3, 4, 6, 7, 8, 9, 11, 12")
    
    print("\nPrimitive Hypotenuse Numbers")
    simple_test(primitive_hypotenuse(),10,
                "5, 13, 17, 25, 29, 37, 41, 53, 61, 65")
    
    print("\nHypotenuse Numbers")
    simple_test(hypotenuse(),10,
                "5, 10, 13, 15, 17, 20, 25, 26, 29, 30")
    