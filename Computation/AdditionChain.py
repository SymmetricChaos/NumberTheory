# Find the shortest chain of additions, starting from 1, which give n.
# This is a simple branch and bound style algorithm which starts by trying
# the greedy method and prunes branches that are worse than what it has found
# before.

def addition_chain(N,L=[1],best=float('inf')):
    # If we found a solution return it
    if L[-1] == N:
        return L
    
    # If we're not better than the best known terminate by returning None
    if len(L) >= best:
        return None
    
    # Otherwise search all valid steps to continue
    out = []
    for i in reversed(L):
        d = (L[-1]+i)
        
        # Ignore branches that would give too large of a number
        if N - d >= 0:
            
            v = addition_chain(N,L+[d],best)
            # If we get a None then the branch failed and we add nothing to the
            # list of options
            if v == None:
                continue
            # Otherwise we have a new best solution
            if len(v) < best:
                best = len(v)
                out = v
    
    # If all branches returned none then this whole section is ignored
    if out == []:
        return None
    return out

print(addition_chain(31))