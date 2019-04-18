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
