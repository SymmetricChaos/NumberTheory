def factoradic(n):
    L = []
    ctr = 1
    while n > 0:
        n, l = divmod(n,ctr)
        L.append(l)
        ctr += 1
    L.reverse()
    return L