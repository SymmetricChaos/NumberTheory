from math import log2, sqrt, floor
from PrimeNumbers import primes

def perfect_power(n):
    
    if n == 0 or n == 1:
        return True
    
    lim = floor(log2(n))+2
    
    for i in primes():
        ctr = 2
        while True:
            pwr = ctr**i
            if pwr > n:
                break
            if pwr == n:
                return True
            ctr += 1
        if i > lim:
            break

    return False

def prime_power(n):
    
    lim = floor(sqrt(n))+1
    
    div = False
    for p in primes():
        
        if n % p == 0:
            div = True
            
        while n % p == 0:
            n = n // p
        
        
        if div == True and n == 1:
            return True
        
        if div == True and n != 1:
            return False
        
        if p > lim:
            break
        
    return True
