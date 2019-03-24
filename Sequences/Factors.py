def factors(n,prime=False):
    L = []
    
    # If not in primes mode just check all the numbers
    if prime == False:
        for i in range(2,n+1):
            if n % i == 0:
                L.append(i)
        return L
    
    # If it is in primes mode check all primes
    else:
        for i in primes():
            if i > n:
                break
            if n % i == 0:
                L.append(i)
        return L