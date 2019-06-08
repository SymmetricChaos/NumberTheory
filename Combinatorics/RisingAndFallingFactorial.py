def falling_factorial(x,n):
    out = 1
    for k in range(n):
        out *= x-k
    return out
    
def rising_factorial(x,n):
    out = 1
    for k in range(n):
        out *= x+k
    return out

