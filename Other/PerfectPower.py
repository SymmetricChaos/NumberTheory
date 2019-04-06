from math import log2, floor

def perfect_power(n):
    
    if n == 0 or n == 1:
        return True
    
    lim = floor(log2(n))+2
    
    for i in range(2,lim+1):
        ctr = 2
        while True:
            pwr = ctr**i
            if pwr > n:
                break
            if pwr == n:
                return True
            ctr += 1

    return False