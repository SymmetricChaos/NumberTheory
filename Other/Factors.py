from Sequences import primes

def factors(n,nontrivial=False):
    L = []
    a, b = 1, n+1
    if nontrivial == True:
        a, b = 2, n
    for i in range(a,b):
        if n % i == 0:
            L.append(i)
    return L
    
def prime_factorization(n):
    L = []
    for p in primes():
        while n % p == 0:
            L.append(p)
            n = n // p
        if n == 1:
            break
    return L