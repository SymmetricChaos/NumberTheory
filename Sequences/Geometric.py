from Sequences.Divisibility import pythagorean_primes
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
    
    for m in naturals(2):
        lim = m*m+1 # smallest number that can be produced in this round
        
        for n in range(1+m%2,m,2):
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


def primitive_pythagorean_triples():
    """
    All primitive pythagorean triples with hypotenuse in non-decreasing order and otherwise lexicographic order
    """
    
    triples = []
    
    for m in naturals(2):
        lim = m*m+1
        
        for n in range(1+m%2,m,2):
            if gcd(m,n) == 1:
                a = m*m-n*n
                b = 2*m*n
                c = m*m+n*n
                
                triples.append( (min(a,b),max(a,b),c) )
        
        # This sorting assures that the hypotenuse is increasing and that
        # the if the hypotenuse is the same for two tuples the one with the
        # smaller initital term will go first
        triples.sort(key=lambda x: (x[2], x[0]))
            
        for i in triples:
            if i[2] > lim:
                break
            
            yield triples.pop(0)


def primitive_pythagorean_perimeters():
    """
    Perimeters of primitive pythagorean triples in asending order
    OEIS A024364
    """
    
    for i in primitive_pythagorean_triples():
        yield sum(i)


def pythagorean_triples():
    """
    All pythagorean triples with hypotenuse in non-decreasing order and otherwise lexicographic order
    """
    
    old_triples = {}
    triples = []
    
    for m in naturals(2):
        lim = m*m+1
        
        for n in range(1+m%2,m,2):
            if gcd(m,n) == 1:
                a = m*m-n*n
                b = 2*m*n
                c = m*m+n*n
                T = (min(a,b),max(a,b),c)
                
                triples.append(T)
                old_triples[T] = T
        
        for key,val in old_triples.items():
            if key[2]+val[2] < lim:
                new = (key[0]+val[0],key[1]+val[1],key[2]+val[2])
                old_triples[key] = new
                
                triples.append(new)
        
        # This sorting assures that the hypotenuse is increasing and that
        # the if the hypotenuse is the same for two tuples the one with the
        # smaller initital term will go first
        triples.sort(key=lambda x: (x[2], x[0]))
            
        for i in triples:
            if i[2] > lim:
                break
            
            T = triples.pop(0)
            yield T


# def pythagorean_perimeters():
#     """
#     Perimeters of pythagorean triples in asending order
#     OEIS 
#     """
    
#     for i in pythagorean_triples():
#         yield sum(i)


#def congruent():
#    """
#    Positive integers that can be the area of a right triangle with rational sides
#    """


def mosner():
    """
    Mosner Numbers: Maximum number of regions created by cutting a circle with n lines\n
    OEIS A000127
    """
    
    cur = 1
    
    for n in naturals(1):
        cur += sum([2-n+n*i-i*i for i in range(1,n)])
        yield cur





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Nonhypotenuse Numbers")
    simple_test(nonhypotenuse(),16,
                "1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 17, 18, 19, 21")
    
    print("\nHypotenuse Numbers")
    simple_test(hypotenuse(),14,
                "5, 10, 13, 15, 17, 20, 25, 26, 29, 30, 34, 35, 37, 39")
    
    print("\nPythagorean Triples")
    simple_test(pythagorean_triples(),4,
                "(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)")
    
    # print("\nPythagorean Perimeters")
    # simple_test(pythagorean_perimeters(),13,
    #             "12, 30, 40, 56, 70, 84, 90, 126, 132, 144, 154, 176")
    
    print("\nPrimitive Hypotenuse Numbers")
    simple_test(primitive_hypotenuse(),14,
                "5, 13, 17, 25, 29, 37, 41, 53, 61, 65, 73, 85, 89, 97")
    
    print("\nPrimitive Pythagorean Triples")
    simple_test(primitive_pythagorean_triples(),4,
                "(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)")
    
    print("\nPrimitive Pythagorean Perimeters")
    simple_test(primitive_pythagorean_perimeters(),12,
                "12, 30, 40, 56, 70, 84, 90, 126, 132, 144, 154, 176")
    
    print("\nMosner")
    simple_test(mosner(),13,
                "1, 2, 4, 8, 16, 31, 57, 99, 163, 256, 386, 562, 794")
    