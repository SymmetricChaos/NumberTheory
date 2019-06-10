def dyck_inner(S,n,l,r):

    ## Check how many of each parenthesis we have
    a = S.count(l)
    b = S.count(r)
    ## If there are more closing than opening we stop immediately
    if a > n:
        return []
    if b > n:
        return []
    if b > a:
        return []
    ## Otherwise we continue until there are 2n parentheses
    if a + b == 2*n and a == b:
        return [S]
    return dyck_inner(S+l,n,l,r) + dyck_inner(S+r,n,l,r)


def dyck_words(n,word="()"):
    l = word[0]
    r = word[1]
    
    return dyck_inner(l,n,l,r)
    
print(dyck_words(4))