from Sequences.MathUtils import nontrivial_factors
from Sequences.Polygonal import gen_pentagonal
from Sequences.Simple import naturals
from math import comb


def derangement():
    """
    Derangement Numbers: Permutations with no element in its original position\n
    OEIS A000166
    """
    
    yield 1
    yield 0
    
    S = [1,0]
    
    for n in naturals(1):
        d = n * (S[0]+S[1])
        S[0], S[1] = S[1], d
        yield d


def even_permutation():
    """
    Even Permutation Numbers: Number of even permutations of n elements\n
    OEIS A001710
    """
    
    yield 1
    yield 1
    yield 1
    
    out = 3
    
    for n in naturals(4):
        yield out
        out = out * n


def catalan():
    """
    Catalan Numbers: Number of non-crossing partitions of a set with n elements\n
    OEIS A000108
    """
    C = 1
    
    yield 1
    
    for n in naturals(1):
        yield C
        C = C*(4*n+2)//(n+2)


# Building the triangle using only addition and index look ups is about 100 
# times faster than calculating the binomial coefficients directly on my
# machine
# There is probably a way to do this is place
def pascal():
    """
    Pascal's Triangle: Number triangle with binomial coefficients\n
    OEIS A007318
    """
    
    L = [1,0]
    
    while True:
        T = [0]
        for i in range(len(L)-1):
            x = L[i]+L[i+1]
            T.append(x)
            yield x
        T.append(0)
        L = T


# Find a more efficient way to do this
def central_binomial():
    """
    Central Binomial Coefficients: 
    OEIS A000984
    """
    
    for n in naturals():
        yield comb(2*n,n)


def gould():
    """
    Gould's Sequence: Number of odd values on the nth row of Pascal's Triangle\n
    OEIS A001316
    """
    
    P = pascal()
    
    for n in naturals(1):
        val = 0
        
        for i in range(n):
            if next(P) % 2 == 1:
                val += 1
        
        yield val


# As with Pascal's triangle I found this memoized version to be vastly faster
# than directly calculating the values, which involved both binomial
# coefficients and exponentiation

def eulerian():
    """
    Eulerian Triangle: Triangle with number of permutations of a set with n elements where there are m increases\n
    OEIS A008292
    """
    
    L = [1,0]
    
    for a in naturals(1):
        T = []
        for b in range(a):
            x = (a-b)*L[b-1] + (b+1)*L[b]
            T.append(x)
            yield x
        T.append(0)
        L = T


def recontres():
    """
    Recontres Numbers: Triangle by rows counting numbers of permutations of n elements with k fixed points
    OEIS A008290
    """
    
    P = pascal()
    dr = derangement()
    D = []
    
    for n in naturals():
        D.append(next(dr))
        yield D[-1]
        
        # Skip the next value of P
        next(P)
        
        for k in range(1,n+1):
            yield D[n-k]*next(P)


def partition():
    """
    Partition Number: Number of ways to add naturals greater than 0 to get n\n
    OEIS A000041
    """
    
    D = [1]
    
    for n in naturals(1):
        yield D[-1]
        
        P = gen_pentagonal()
        next(P)
        
        sign = -1
        k=0
        
        for ctr,i in enumerate(P):
            if n-i < 0:
                D.append(k)
                break
            
            if ctr % 2 == 0:
                sign *= -1
            
            k += sign*D[n-i]


def bell():
    """
    Bell Numbers: Number of equivalence classes on a set with n elements\n
    OEIS A000110
    """
    
    R0 = [1]
    R1 = [1,2]
    
    while True:
        yield R0[0]
        R2 = [R1[-1]]
        
        for i in R1:
            R2.append(i+R2[-1])
        
        R0, R1 = R1, R2


def lazy_caterer():
    """
    Lazy Caterer Numbers: Maximum number of pieces produced when cutting a circle with exactly n lines\n
    OEIS A000124
    """
    
    for n in naturals():
        yield (n*(n+1))//2+1


# Generalized cake numbers?
def cake():
    """
    Cake Numbers: Maximum number of pieces produced when cutting a sphere with exactly n planes\n
    OEIS A000125
    """
    
    for n in naturals():
        yield (n*n*n+5*n+6)//6


# Potentially memoizeable
def multiplicative_partition():
    """
    Multiplicative Partition Numbers: Sets of integers, not including one, that have a product of n\n
    OEIS A001055
    """
    
    def all_factorizations_inner(n,m=1):
        F = [f for f in nontrivial_factors(n) if f >= m]
        
        if len(F) == 0:
            yield [n]
        
        else:
            for f in F:
                for a in all_factorizations_inner(n//f,f):
                    yield [f] + a
    
    def num_factorizations(n):
        S = set([(n,)])
        
        for i in all_factorizations_inner(n):
            S.add(tuple(sorted(i)))
        
        return len(S)
    
    for n in naturals(1):
        yield num_factorizations(n)





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Derangement Numbers")
    simple_test(derangement(),11,
                "1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961")
    
    print("\nCatalan Numbers")
    simple_test(catalan(),11,
                "1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796")
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal(),18,
                "1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10")
    
    print("\nCentral Binomial Coefficients")
    simple_test(central_binomial(),11,
                "1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756")
    
    print("\nGould's Sequence")
    simple_test(gould(),18,
                "1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, 4")
    
    print("\nEulerian Triangle by Rows")
    simple_test(eulerian(),16,
                "1, 1, 1, 1, 4, 1, 1, 11, 11, 1, 1, 26, 66, 26, 1, 1")
    
    print("\nPartition Numbers")
    simple_test(partition(),15,
                "1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135")
    
    print("\nBell Numbers")
    simple_test(bell(),11,
                "1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975")
    
    print("\nLazy Caterer's Numbers")
    simple_test(lazy_caterer(),14,
                "1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92")
    
    print("\nCake Numbers")
    simple_test(cake(),13,
                "1, 2, 4, 8, 15, 26, 42, 64, 93, 130, 176, 232, 299")
    
    print("\nMultiplicative Partitions")
    simple_test(multiplicative_partition(),18,
                "1, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 4, 1, 2, 2, 5, 1, 4")
    
    print("\nEven Permutations")
    simple_test(even_permutation(),11,
                "1, 1, 1, 3, 12, 60, 360, 2520, 20160, 181440, 1814400")
    
    print("\nRecontres Numbers")
    simple_test(recontres(),17,
                "1, 0, 1, 1, 0, 1, 2, 3, 0, 1, 9, 8, 6, 0, 1, 44, 45")