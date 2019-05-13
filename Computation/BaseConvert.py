# Converts a decimal integer into a list of integers representing the digits of 
# the number in another base. This allows it to represent numbers in arbitrarily
#  large bases.

def baseConvert(n,b,bigendian=False):
    """Convert a decimal integer to another base."""
    if b < 1:
        raise Exception("Base must be greater than 1.")
    
    
    if b == 1:
        return [1]*n
    if(n == 0):
        return([0])
    out = []
    while(n > 0):
        out.append(n%b)
        n //= b
    if(bigendian==True):
        return(out)
    return(out[::-1])

def binary_partition(n,b):
    """Convert an integer into its sum as powers of two"""

    
    if(n == 0):
        return([0])
    out = []
    ctr = 0
    while(n > 0):
        if n % 2 == 1:
            out.append(2**ctr * (n%2))
        ctr += 1
        n //= 2
    return(out[::-1])