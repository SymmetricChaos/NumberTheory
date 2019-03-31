# Rough estimation to start off other algorithms
def estimate_root(x):
    """Crude Estimate for Square Root"""
    return x // (10**(len(str(x))//2))

# Use iterations of the babylonian method to calculate the square root of a number
def babylonian_root(x,iters=10):
    """Babylonian Method"""
    
    if x == 0:
        return 0
    
    est = estimate_root(x)
    a = est
    b = (a+(x/a))/2
    
    for i in range(iters):
        a, b = b, (a+(x/a))/2
    return b

# Use the babylonian method with integer division to find the largest integer
# with a square less than n
def int_root(x,iters=10000):
    """Integer Square Root"""
    
    if x == 0:
        return 0
    
    est = estimate_root(x)
    a = est
    b = (a+(x//a))//2
    
    t = [(a,b)]
    
    while True:
        a, b = b, (b+(x//b))//2
        if (a,b) in t:
            break
        t.append((a,b))
    
    # Sometimes b is too large when we reach a stopping point, this fixes that
    if b**2 > x:
        return b-1
    return b

def is_square(x):
    if int_root(x)**2 == x:
        return True
    return False

from math import sqrt, floor

N = 3
print(N)
#print(estimate_root(N))
print("Math Lib:",sqrt(N))
print("Int Root:",int_root(N))
print("Custom:",babylonian_root(N))

