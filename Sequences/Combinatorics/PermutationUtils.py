

def permutation_cycle(cycle,T,index=0):
    
    cycle = cycle + (cycle[0],)
    new = list(T[:])
    for pos in range(len(cycle)-1):
        new[cycle[pos+1]-index] = cycle[pos]
    
    return tuple(new)
