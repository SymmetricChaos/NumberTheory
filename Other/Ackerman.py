def ackerman(m,n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1,ackerman(m,n-1))
    
def ackerman_3(m,n,p):
    if p == 0:
        return m+n
    if n == 0 and p == 1:
        return 0
    if n == 0 and p == 2:
        return 1
    if n == 0 and p >= 3:
        return m
    else:
        return ackerman_3(m,ackerman_3(m,n-1,p),p-1)