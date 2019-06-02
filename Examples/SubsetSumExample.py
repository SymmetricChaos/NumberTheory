def subset_sum_dynamic(L,N):
    """Faster solution to subset sum"""
    L.sort(reverse=True)
    if any([i < 0 for i in L]):
        raise Exception("Doesn't work with negatives")
    return is_subset_sum(L,len(L),N)
    
import random
for i in range(5):
    L = [random.randint(0,100) for i in range(25)]
    N = random.randint(0,1000) 
    print(N,L)
    S = subset_sum_dynamic(L,N)
    print(sum(S),S)
    print("\n\n")

#subset_sum_dynamic([-1,100],99)

for i in range(5):
    L = [random.randint(-100,100) for i in range(10)]
    N = random.randint(-200,200) 
    print(N,L)
    for i in subset_sums(L,N):
        print(sum(i),i)
    print("\n\n")