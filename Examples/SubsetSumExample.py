from Other import subset_sum_dynamic
import random


for i in range(3):
    L = [random.randint(0,100) for i in range(25)]
    N = random.randint(0,1200)
    print("Given the set:")
    print(L)
    print(f"What is subset that has the sum {N}?")
    S = subset_sum_dynamic(L,N)
    print(S)
    print("\n\n")