from Primality import is_prime
from ModularArithmetic import gcd

def quad_residue(q,m):
    
    if is_prime(m) and gcd(q,m) == 1:
        e = q**((m-1)//2) % m
        if e == 1:
            return True
        return False
    else:
        for i in range(m):
            if i**2 % m == q:
                return True
        return False

def find_quad_residue(m):
    L = []
    for i in range(m):
        if quad_residue(i,m) and i not in L:
            L.append(i)
    L.sort()
    return L



for i in range(2,22):
    qr = find_quad_residue(i)
    
    print("{:<{}} {}".format(i,2,qr))
    