from Sequences.MathUtils import choose, factorization
from Sequences.Polygonal import gen_pentagonal
from Sequences.Simple import naturals

def derangements():
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


def catalan():
    """
    Catalan Numbers: Number of non-crossing partitions of a set with n elements\n
    OEIS A000108
    """
    
    for n in naturals():
        N = 1
        D = 1
        
        for k in range(2,n+1):
            N *= n+k
            D *= k
        
        yield N//D


# Building the triangle using only addition and index look ups is about 100 
# times faster than calculating the binomial coefficients directly on my
# machine
# There  is probably a way to do this is place
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


# Memoized version is about 1000 times faster than the explicit formula as that
# involved both computing a binomial coefficient and exponentiation
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


# Generalized cake numbers? Uses binomial coefficients
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
        F = [f for f in factorization(n,nontrivial=True) if f >= m]
        
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
    simple_test(derangements(),9,
                "1, 0, 1, 2, 9, 44, 265, 1854, 14833")
    
    print("\nCatalan Numbers")
    simple_test(catalan(),9,
                "1, 1, 2, 5, 14, 42, 132, 429, 1430")
    
    print("\nPascal's Triangle by Rows")
    simple_test(pascal(),10,
                "1, 1, 1, 1, 2, 1, 1, 3, 3, 1")
    
    print("\nGould's Sequence")
    simple_test(gould(),10,
                "1, 2, 2, 4, 2, 4, 4, 8, 2, 4")
    
    print("\nEulerian Triangle by Rows")
    simple_test(eulerian(),10,
                "1, 1, 1, 1, 4, 1, 1, 11, 11, 1")
    
    print("\nPartition Numbers")
    simple_test(partition(),10,
                "1, 1, 2, 3, 5, 7, 11, 15, 22, 30")
    
    print("\nBell Numbers")
    simple_test(bell(),9,
                "1, 1, 2, 5, 15, 52, 203, 877, 4140")
    
    print("\nLazy Caterer's Numbers")
    simple_test(lazy_caterer(),10,
                "1, 2, 4, 7, 11, 16, 22, 29, 37, 46")
    
    print("\nCake Numbers")
    simple_test(cake(),10,
                "1, 2, 4, 8, 15, 26, 42, 64, 93, 130")
    
    print("\nMultiplicative Partitions")
    simple_test(multiplicative_partition(),10,
                "1, 1, 1, 2, 1, 2, 1, 3, 2, 2")