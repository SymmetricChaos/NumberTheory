from Computation.RootFinding import int_root

# Trial division is the simplest way of checking if a number is prime although
# it runs in exponential time (pseudo-polynomial) it is quite fast for "small"
# numbers and easy to implement. It is only necessary to check primes up to the
# square root of the number in question.

def trial_division_test(n,x=None):
    """Primality testing by trial division"""
    
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    
    if x == None:
        x = int_root(n)+2
    else:
        x = min(int_root(n)+2,x)
    
    # Prime numbers up to 1000 have been pre-sieved.
    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
         67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 
         139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 
         223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 
         293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 
         383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 
         463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 
         569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 
         647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 
         743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 
         839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 
         941, 947, 953, 967, 971, 977, 983, 991, 997]
    
    for i in P:
        if n % i == 0:
            return False
        if i >= x:
            return True

    for i in range(1009,x,2):
        if n % i == 0:
            return False
    
    return True

# Using both Fermat's factorization method and trial division together produces
# a faster test for primality by exploiting the fact that Fermat's method can
# exclude a large amount of numbers at once.


def fermat_and_trial_test(n,lim=10):
    
    a = int_root(n)
    
    factor_found = False
    pr = a
    while True:
        a += 1
        b2 = a**2-n
        b = int_root(b2)
        
        # If a factor is found the number is not prime
        if b**2 == b2:
            factor_found = True
            break
        
        # Steps of fermat's method take significantly longer than trial division
        # so at a certain point its not worth continuing.
        if pr-(a-b) < lim:
            break
        
        pr = a-b
        
    if factor_found == True:
        return False

    return trial_division_test(n,a-b)
        

