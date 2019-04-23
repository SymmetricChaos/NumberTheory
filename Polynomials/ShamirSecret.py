from PolynomialOOP import polynomial
from random import randint

def shamir(S,n,k,p):
    
    if p <= S:
        raise Exception("p must be strictly greater than S")
    if p <= n:
        raise Exception("p must be strictly greater than n")
        
    A = [S] + [randint(1,p) for i in range(k-1)]
    
    PA = polynomial(A,p)
    
    ps = [(i,PA.evaluate(i)) for i in range(1,n+1)]
    
    return ps
    
    
    
S = shamir(1234,6,3,1931)

for i in S:
    print(i)