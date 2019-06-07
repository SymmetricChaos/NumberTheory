
def stirling_numbers_1(n,k):
    """Stirling Numbers of the First Kind"""
    if n == k:
        return 1
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return (n-1)*stirling_numbers_1(n-1,k) + stirling_numbers_1(n-1,k-1)



def stirling_numbers_2(n,k):
    """Stirling Numbers of the Second Kind"""
    if n == k:
        return 1
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k*stirling_numbers_2(n-1,k) + stirling_numbers_2(n-1,k-1)


