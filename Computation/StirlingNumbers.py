# Stirling Numbers of the second kind

def stirling_numbers_2(n,k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k*stirling_numbers_2(n-1,k) + stirling_numbers_2(n-1,k-1)

for i in range(10):
    for j in range(i):
        print(stirling_numbers_2(i,j),end=" ")
    print()