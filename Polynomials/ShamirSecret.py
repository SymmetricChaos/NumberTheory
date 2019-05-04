from PolynomialType import Polynomial
from PrimeNumbers import is_prime
from random import randint

# S: the secret
# n: the number of people to share with
# k: the number of pieces needed to decipher
# p: the order of the field used, a prime
def shamir(S,n,k,p):
    assert p > S, "p must be strictly greater than S"
    assert p > n, "p must be strictly greater than n"
    assert is_prime(p), "p must be prime"
        
    A = [S] + [randint(1,p) for i in range(k-1)]
    
    PA = Polynomial(A,p)
    
    ps = [(i,PA.evaluate(i)) for i in range(1,n+1)]
    
    return ps
    
    
    
S = shamir(1234,6,3,1931)

for i in S:
    print(i)