from Sequences.MathUtils import choose
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


def pascal():
    """
    Pascal's Triangle: Number triangle with binomial coefficients\n
    OEIS A007318
    """
    
    n, k = 0, 0
    
    while True:
        yield choose(n,k)
               
        if n == k:
            n += 1
            k = 0
        else:
            k += 1


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


def eulerian():
    """
    Eulerian Triangle: Triangle with number of permutations of a set with n elements where there are m increases\n
    OEIS A008292
    """
    
    for m in naturals(1):
        for n in range(m):
            S = 0
            sign = -1
            
            for k in range(n+1):
                sign *= -1
                S += sign*choose(m+1,k)*(n+1-k)**m
            
            yield S


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


# Generalized cake numbers? Uses binomial coefficients
def cake():
    """
    Cake Numbers: Maximum number of pieces produced when cutting a cube with exactly n planes\n
    OEIS A000125
    """
    
    for n in naturals():
        yield (n*n*n+5*n+6)//6


# def multiplicative_partition():
#     """
#     Multiplicative Partition Numbers: Count of unique factorizations of each positive integer ignoring 1\n
#     OEIS A001055
#     """
    
    




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
    
    print("\nCake Numbers")
    simple_test(cake(),9,
                "1, 2, 4, 8, 15, 26, 42, 64, 93")
    