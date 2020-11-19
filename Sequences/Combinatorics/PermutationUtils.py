

def permutation_cycle(C,T,index=0):
    
    C = C + (C[0],)
    new = list(T[:])
    for pos in range(len(C)-1):
        new[C[pos+1]-index] = C[pos]
    
    return tuple(new)
