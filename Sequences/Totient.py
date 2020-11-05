from Sequences.Simple import naturals
from Sequences.Primes import primorial
from Sequences.MathUtils import jordan_totient, prime_power_factorization, multi_lcm

from collections import defaultdict


def totients():
    """
    Totients: Count of positive integers coprime to each positive integer\n
    OEIS A000010
    """
    
    D = defaultdict(list)
    
    yield 1
    
    for q in naturals(2):
        if q not in D:
            yield q-1
            D[q + q] = [q]
        
        else:
            n,d = 1,1
            
            for p in D[q]:
                D[p+q].append(p)
                
                n *= (p-1)
                d *= p
            
            yield q*n//d
            
            del D[q]


def cototients():
    """
    Cotients: Count of positive integers not coprime to each positive integer\n
    OEIS A051953
    """
    
    for n,t in enumerate(totients(),1):
        yield n-t


def totient_range():
    """
    Range of Euler's Totient Function in order
    """
    
    # Primorials are all sparsely totient, every following number has a greater totient
    
    P = primorial()
    ctr = next(P)
    
    old = set([])
    S = set([])
    
    for n,t in enumerate(totients(),1):
        S.add(t)
        
        if n == ctr:
            ctr = next(P)
            
            #When reaching a primorial filter out eveything greater than its totient
            confirmed = [s for s in S-old if s <= t]
            
            # Then eliminate previously used values from S
            S = S - old
            
            # Store thenew confirmed values as old, we don't need anything else
            # because low number won't appear again
            old = set(confirmed)
            
            yield from sorted(confirmed)


def nontotients():
    """
    Numbers that are not in the range of the totient function\n
    OEIS A007617
    """
    
    T = totient_range()
    a,b = next(T),next(T)
    
    while True:
        for i in range(a+1,b):
            yield 
        
        a,b = b,next(T)


def even_nontotients():
    """
    Even Numbers that are not in the range of the totient function\n
    OEIS A005277
    """
    
    for i in nontotients():
        if i % 2 == 0:
            yield i


# def noncototient():


# def sparsely_totient():


def charmichael():
    """
    Charmichael Function: LCM of the orders of the elements of the finite multiplictive group on n\n
    OEIS A002322
    """
    
    yield 1
    
    def charm(n):
        if n > 4 and n%2 == 0:
            return jordan_totient(n)//2
        return jordan_totient(n)
    
    for n in naturals(2):
        T = [charm(p) for p in prime_power_factorization(n)]
        
        yield multi_lcm(T)


def jordan_totients(k):
    """
    Jordan's k-Totient Function
    
    Args:
        k -- power that denominator is raised to
    
    OEIS A007434, A059376, A059377, A059378, A069091-A069095
    """
    
    for n in naturals(1):
        yield jordan_totient(n,k)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Totient Sequence")
    simple_test(totients(),17,
                "1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16")
    
    print("\nJordan 2-Totients")
    simple_test(jordan_totients(2),13,
                "1, 3, 8, 12, 24, 24, 48, 48, 72, 72, 120, 96, 168")
    
    print("\nCharmichael Function")
    simple_test(charmichael(),17,
                "1, 1, 2, 2, 4, 2, 6, 2, 6, 4, 10, 2, 12, 6, 4, 4, 16")
    
    print("\nCototient Numbers")
    simple_test(cototients(),18,
                "0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, 1, 8, 7, 8, 1, 12")
    
    print("\nRange of the Totient Function")
    simple_test(totient_range(),15,
                "1, 2, 4, 6, 8, 10, 12, 16, 18, 20, 22, 24, 28, 30, 32")
    
    print("\nNontotient Numbers")
    simple_test(nontotients(),15,
                "3, 5, 7, 9, 11, 13, 14, 15, 17, 19, 21, 23, 25, 26, 27")
    
    print("\nEven Nontotient Numbers")
    simple_test(even_nontotients(),13,
                "14, 26, 34, 38, 50, 62, 68, 74, 76, 86, 90, 94, 98")
    