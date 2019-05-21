from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subset_sum(L,n):
    """Find a subset of L that has a sum of n if it exists"""
    
    L.sort()
    for i in list(powerset(L)):
        if sum(i) == n:
            return i
    return ()


def subset_sum_dynamic(L,N):
    
    def is_subset_sum(s,n,sm):
        print(s[:n],sm)
        # If we are not considering anything and we haven't gotten to zero then
        # this branch is a failure.
        if sm >= 0 and n == 0:
            return False
        
        # If we have gotten the sum down to zero than we have succeeded
        if sm == 0:
            return True
        
        # If the last element in the array is bigger than the sum try excluding
        # the element
        if (s[n - 1] > sm) : 
            return is_subset_sum(s, n - 1, sm); 
   
        # Otherwise try removing the last element and try including the last
        # element. If either of these branches succeeds then 
        return is_subset_sum(s,n-1,sm) or is_subset_sum(s, n-1, sm-s[n-1])
    
    return is_subset_sum(L,len(L),N)
    
print(subset_sum_dynamic([1,9,21],31))


#import random
#for i in range(1):
#    L = [random.randint(0,100) for i in range(5)]
#    N = random.randint(0,1000) 
#    S = subset_sum_dynamic(L,N)
#    print(N,L)
#    print(S)
#    print()