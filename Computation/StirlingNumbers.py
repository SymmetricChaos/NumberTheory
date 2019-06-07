
# Stirling Numbers of the first kind
def stirling_numbers_1(n,k):
    if n == k:
        return 1
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return (n-1)*stirling_numbers_1(n-1,k) + stirling_numbers_1(n-1,k-1)



# Stirling Numbers of the second kind
def stirling_numbers_2(n,k):
    if n == k:
        return 1
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k*stirling_numbers_2(n-1,k) + stirling_numbers_2(n-1,k-1)



#for i in range(9):
#    for j in range(i+1):
#        print(stirling_numbers_1(i,j),end=" ")
#    print()
#print()
#for i in range(9):
#    for j in range(i+1):
#        print(stirling_numbers_2(i,j),end=" ")
#    print()