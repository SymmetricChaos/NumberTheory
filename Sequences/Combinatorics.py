from Sequences.Utils import choose
from Sequences.Polygonal import gen_pentagonal
from Sequences.Simple import naturals

def derangements():
    """Derangement numbers"""
    
    yield 1
    yield 0
    
    S = [1,0]
    
    ctr = 0
    while True:
        ctr += 1
        d = ctr * (S[0]+S[1])
        S[0], S[1] = S[1], d
        yield d


def catalan():
    """Catalan Numbers"""
    
    n = 0
    while True:
        N = 1
        D = 1
        for k in range(2,n+1):
            N *= n+k
            D *= k
        yield N//D
        
        n += 1


def pascal():
    """Pascal's Triangle"""
    
    n, k = 0, 0
    while True:
        
        yield choose(n,k)
               
        if n == k:
            n += 1
            k = 0
        else:
            k += 1


# Number of ways to add naturals greater than 0 to get n
def partition():
    """Partition Number"""
    
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


# Bell numbers count the partitions of a set with n elements
def bell():
    """Bell Numbers"""
    
    R0 = [1]
    R1 = [1,2]
    
    while True:
        
        yield R0[0]
        
        R2 = [R1[-1]]
        
        for i in R1:
            R2.append(i+R2[-1])
        
        R0, R1 = R1, R2


def eulerian():
    """Euler's Triangle"""
    
    for m in naturals(1):
        for n in range(m):
            S = 0
            sign = -1
            for k in range(n+1):
                sign *= -1
                S += sign*choose(m+1,k)*(n+1-k)**m
            yield S