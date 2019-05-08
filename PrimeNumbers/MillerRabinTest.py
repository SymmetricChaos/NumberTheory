# The Miller-Rabin primality test is an extremely fast method of checking
# whether or not a number is prime. When it returns False the number is
# definitely composite. When it returns True the number is probably prime.
# However with the default set of witnesses this is deterministic only for
# number up to 2^80

# Test if a number is composite for a given base
def is_composite(a,d,n,r):
    for i in range(0,r+1):
        if pow(a,2**i*d,n) == 1:
            return False
    return True

# Wrapper function
def miller_rabin_test(n,W=[],silent=False):
    """Miller-Rabin primality test"""
    
    if W == []:
        W = [2,3,5,7,11,13,17,19,23,29,31,37,41]
    
    # Deal with even numbers first
    if n == 2:
        return True
    if n % 2 == 0:
        return False


    d = n-1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for witness in W:
        if witness >= n:
            break
        # If the test for compositeness returns true we know for certain the
        # number is composite and we return false
        if is_composite(witness,d,n,r):
            return False
    
    if silent == False and n > (2**80):
        print("Test is only probable.")
        
    return True