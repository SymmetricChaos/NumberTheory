from GeneralUtils import prod

def binary_partition(n):
    """Get the powers of two that sum to an integer"""

    if(n == 0):
        return([0])
    out = []
    ctr = 0
    while(n > 0):
        if n % 2 == 1:
            out.append(ctr)
        ctr += 1
        n //= 2
    return(out)


def exp_by_squaring(b,n,m=0):
    p = binary_partition(n)
    #Multiplications needed
    #print(len(p)+max(p)-1)
    t = b
    L = [b]
    for i in range(p[-1]):
        t = t*t
        L.append(t)
        
    return prod([L[i] for i in p])