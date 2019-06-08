from Combinatorics.Choose import choose

# The Catalan numbers count the number of noncrossing partitions of a set

def catalan(n):
    assert type(n) == int
    assert n >= 0
    return choose(2*n,n)//(n+1)
    