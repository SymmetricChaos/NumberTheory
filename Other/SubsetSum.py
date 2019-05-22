from itertools import chain, combinations

def powerset(iterable):
    """The powerset of some iterable"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# This method is inefficient but it does guarantee no shorter sum exists
def subset_sum(L,n):
    """Find a subset of L that has a sum of n if it exists"""
    
    L.sort()
    for i in list(powerset(L)):
        if sum(i) == n:
            return i
    return ()

def is_subset_sum(s,pos,n,out=[]):
    #print(out)
    # If we have gotten the sum down to zero than we have succeeded
    if n == 0:
        return out
    
    # If we are not considering anything and we haven't gotten to zero then
    # this branch is a failure.
    if n >= 0 and pos == 0:
        return []
    
    # If the last element in the array is bigger than the sum then we only need
    # to consider branches without it.
    if (s[pos - 1] > n):
        return is_subset_sum(s, pos - 1, n,out); 
    
    # Otherwise try removing the last element and try including the last
    # element. If either branch finds a sum then we succeed.
    # We are exploiting a clever feature of Python here. We can use many objects
    # are inputs for logical operators. An empty list is evaluated as False while
    # any non-empty list is evaluated as True.
    return is_subset_sum(s,pos-1,n,out) or is_subset_sum(s, pos-1, n-s[pos-1],out+[s[pos-1]])


def subset_sum_dynamic(L,N):
    
    return is_subset_sum(L,len(L),N)
    
#print(subset_sum_dynamic([5,8,40,9,17,21,1,11,19],31))

import random
for i in range(5):
    L = [random.randint(0,100) for i in range(25)]
    N = random.randint(0,1000) 
    print(N,L)
    S = subset_sum_dynamic(L,N)
    print(sum(S),S)
    print("\n\n")