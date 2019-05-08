# The Lucas-Lehmer test is a fast method for checking is a Mersenne number is
# prime.

def lucas_lehmer_test(n):
    if n == 2:
        return True
        
    s = 4
    M = 2**n-1
    for i in range(n-2):
        s = pow(s,2,M)-2
        if s == 0:
            return True
    return False