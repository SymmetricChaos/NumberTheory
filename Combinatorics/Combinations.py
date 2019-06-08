def combo_pairs(N,replacement=False):
    """Combinations of natural numbers in ascending order"""
    
    # Without replacement
    if replacement == False:
        if N != 0:
            for i in range(N):
                for j in range(i+1,N):
                    yield (i,j)
        else:
            i = 0
            while True:
                for j in range(i):
                    yield (j,i)
                i += 1
                
    # With replacement
    if replacement == True:
        if N != 0:
            for i in range(N):
                for j in range(i+1):
                    yield (j,i)
        else:
            i = 0
            while True:
                for j in range(i+1):
                    yield (j,i)
                i += 1
