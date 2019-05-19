def digital_sum(n):
    if n < 10:
        return n
    L = [int(i) for i in str(n)]
    return sum(L)
    
def digital_root(n):
    if n < 10:
        return n
    L = [int(i) for i in str(n)]
    while len(L) > 1:
        s = sum(L)
        L = [int(i) for i in str(s)]
    return s



def additive_persistence(n):
    steps = 0
    L = [int(i) for i in str(n)]
    while len(L) > 1:
        steps += 1
        s = sum(L)
        L = [int(i) for i in str(s)]
    return steps