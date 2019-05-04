from PolynomialType import Polynomial

# The finite field GF(2^8) with 256 elements has various expressions

def rij_print(P):
    s = ""
    for i in reversed(P.coef):
        s += str(i)
    print(s)
        

def rij_add(P,Q):
    
    # The Rijndael polynomial 
    R = Polynomial([1,1,0,1,1,0,0,0,1],2)
    
    return (P+Q) % R

def rij_mult(P,Q):
    
    # The Rijndael polynomial 
    R = Polynomial([1,1,0,1,1,0,0,0,1],2)
    
    return (P*Q) % R

P = Polynomial([0,1,1,0,1,1,1],2)
Q = Polynomial([1,0,1,0,1],2)

rij_print(P)
rij_print(Q)
rij_print(rij_add(P,Q))