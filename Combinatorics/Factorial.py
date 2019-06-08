def factorial(n):
    if n == 0:
        return 1
    else:
        ctr = 1
        for i in range(1,n+1):
            ctr *= i
        return ctr
