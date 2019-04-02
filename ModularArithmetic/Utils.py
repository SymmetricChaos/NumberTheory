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
    # simplest case
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
    # simplest case
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

# Check if two numbers are coprimes
def coprime(p,q):
    """Check if inputs are coprime"""
    if gcd(p,q) == 1:
        return True
    return False


from Sequences import primes
def totient(n):
    N = 1
    D = 1
    for p in primes():
        if p > n:
            break
        
        if n % p == 0:
            N *= (p-1)
            D *= p
    
    return n*N//D
        
        