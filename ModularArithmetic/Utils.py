from Other.Factorization import factorization
from Sequences import primes

# Extended Euclidean algorithm
# Very useful for a bunch of functions in modular arithmetic
# g   : Greatest common denominator
# x,y : integers such that g = ax + by
def egcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Determine the greatest common denominator for a set of numbers
def gcd(*args):
    """Greatest Common Denominator"""

    # Handle the case that a list is provided
    if len(args) == 1 and type(args[0]) is list:
        return gcd(*args[0])
    
    # the gcd of a number with itself is iself
    if len(args) == 1:
        return args[0]
    
    # calculate gcd for two numbers
    if len(args) == 2:
        a = args[0]
        b = args[1]
        g,x,y = egcd(a,b)
        return g
    
    # if more than two break it up recursively
    a = gcd(*args[0:2])
    b = gcd(*args[2:])
    return gcd(a,b)


# Determine the least common multiple for a set of numbers
def lcm(*args):
    """Least Common Multiple"""
    
    # Handle the case that a list is provided
    if len(args) == 1 and type(args[0]) is list:
        return lcm(*args[0])
    
    # the lcm of a number with itself is iself
    if len(args) == 1:
        return args[0]
    
    # calculate lcm for two numbers
    if len(args) == 2:
        a = args[0]
        b = args[1]
        g,x,y = egcd(a,b)
        return abs(a*b)//g
    
    # if more than two break it up recursively
    a = lcm(*args[0:2])
    b = lcm(*args[2:])
    return lcm(a,b)


# Use egcd to calculate the modular multiplicative inverse
def modinv(a, m):
    """Modular Multiplicative Inverse"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Calculate the numbers coprime to some modulus m
def coprimes(m):
    """Numbers Coprime to Input"""
    L = []
    for i in range(1,m):
        if gcd(i,m) == 1:
            L.append(i)
    return L

# Check if two numbers are coprime
def coprime(p,q):
    """Check if inputs are coprime"""
    if gcd(p,q) == 1:
        return True
    return False

# Is there any number other than 1 than divides all elements of the set?
def setwise_coprime(*args):
    """Check if inputs are setwise coprime"""
    if gcd(*args) == 1:
        return True
    return False

# Is every pair of elements coprime?
def pairwise_coprime(*args):
    """Check if inputs are pairwise coprime"""
    L = []
    for i in args:
        L += factorization(i)[1:]
    if len(set(L)) == len(L):
        return True
    return False

# Count of naturals coprime to n
def totient(n):
    """Euler's Totient Function"""
    N = 1
    D = 1
    for p in primes():
        if p > n:
            break
        
        if n % p == 0:
            N *= (p-1)
            D *= p
    
    return n*N//D
