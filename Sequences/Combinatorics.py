from Sequences.MathUtils import choose
from Sequences.Polygonal import gen_pentagonal
from Sequences.Simple import naturals

def derangements():
    """Derangement Numbers: Permutations with no element in its original position"""
    
    yield 1
    yield 0
    
    S = [1,0]
    
    for n in naturals(1):
        d = n * (S[0]+S[1])
        S[0], S[1] = S[1], d
        yield d


def catalan():
    """Catalan Numbers: Number of non-crossing partitions of a set with n elements"""
    
    for n in naturals():
        N = 1
        D = 1
        
        for k in range(2,n+1):
            N *= n+k
            D *= k
        
        yield N//D


def pascal():
    """Pascal's Triangle: Number triangle with binomial coefficients"""
    
    n, k = 0, 0
    
    while True:
        yield choose(n,k)
               
        if n == k:
            n += 1
            k = 0
        else:
            k += 1


def partition():
    """Partition Number: Number of ways to add naturals greater than 0 to get n"""
    
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
    """Bell Numbers: Number of equivalence classes on a set with n elements"""
    
    R0 = [1]
    R1 = [1,2]
    
    while True:
        yield R0[0]
        R2 = [R1[-1]]
        
        for i in R1:
            R2.append(i+R2[-1])
        
        R0, R1 = R1, R2


def eulerian():
    """Eulerian Numbers: Triangle with number of permutations of a set with n elements where there are m increases"""
    
    for m in naturals(1):
        for n in range(m):
            S = 0
            sign = -1
            
            for k in range(n+1):
                sign *= -1
                S += sign*choose(m+1,k)*(n+1-k)**m
            
            yield S


def gould():
    """Gould's Sequence: Number of odd values on the nth row of Pascal's Triangle"""
    
    P = pascal()
    
    for n in naturals(1):
        val = 0
        
        for i in range(n):
            if next(P) % 2 == 1:
                val += 1
        
        yield val


# Generalized cake numbers? Uses binomial coefficients
def cake():
    """Cake Numbers: Maximum number of pieces produced when cutting a cube with exactly n planes"""
    
    for n in naturals():
        yield (n*n*n+5*n+6)//6
