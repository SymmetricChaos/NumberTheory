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

#import random 
#L = [random.randint(0,100) for i in range(10)]
#S = subset_sum(L,143)
#print(S,sum(S))