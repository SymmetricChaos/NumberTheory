# Find the shortest chain of additions, starting from 1, which give n.

def addition_chain(N,L=[1]):
    
    if L[-1] == N:
        return L
    
    t = []
    for i in L:
        d = (L[-1]+i)

        if N - d >= 0:
            t.append(addition_chain(N,L+[d]))
    
    return min(t,key=len)
            

print(addition_chain(27))

# We should be able to adapt this branch and bound algorithm
#def is_subset_sum(s,pos,n,out=[]):
#    """Recursive function to find a subset sum"""
#    # If we have gotten the sum down to zero than we have succeeded
#    if n == 0:
#        return out
#    
#    # If we are not considering anything and we haven't gotten to zero then
#    # this branch is a failure.
#    if n >= 0 and pos == 0:
#        return []
#    
#    # If the last element in the array is bigger than the sum then we only need
#    # to consider branches without it.
#    if (s[pos - 1] > n):
#        return is_subset_sum(s, pos - 1, n,out)
#    
#    # Otherwise try removing the last element and try including the last
#    # element. If either branch finds a sum then we succeed.
#    # We are exploiting a clever feature of Python here. We can use many objects
#    # as inputs for logical operators. An empty list is evaluated as False while
#    # any non-empty list is evaluated as True.
#    return is_subset_sum(s,pos-1,n,out) or is_subset_sum(s, pos-1, n-s[pos-1],out+[s[pos-1]])
