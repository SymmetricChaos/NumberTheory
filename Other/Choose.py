def choose(n,k):
    """Binomial coefficient"""
    if n < k:
        raise Exception("n cannot be less than k")
    if k < 0:
        raise Exception("k must be nonnegative")
        
    # Calculate the numerator and denominator seperately in order to avoid loss
    # of precision for large numbers.
    N = 1
    D = 1
    for i in range(1,k+1):
        N *= (n+1-i)
        D *= i
    return N//D