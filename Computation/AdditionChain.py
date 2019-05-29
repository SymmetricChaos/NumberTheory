# Find the shortest chain of additions, starting from 1, which give n.
# This is a simple branch and bound style algorithm which starts by trying
# the greedy method and prunes branches that are worse than what it has found
# before.
def addition_chain(N,L=[1],best=float('inf')):

    # If we found a solution return it
    if L[-1] == N:
        return L
    
    # If we're not better than the best known terminate by returning a wrong
    # answer without further searching.
    if len(L) >= best:
        return L+[0]
    
    # Otherwise search all valid steps to continue and make a list of the
    # results.
    # Then return the shortest of those.
    
    t = []
    
    for i in reversed(L):
        d = (L[-1]+i)
        
        if N - d >= 0:
            
            v = addition_chain(N,L+[d],best)
            if len(v) < best:
                best = len(v)
            t.append(v)
    print(min(t,key=len)) 
    return min(t,key=len)
            
v = addition_chain(16)
print()
print(v)