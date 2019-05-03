from ModularArithmetic import gcd

def euclid_triple(m,n,k=1):
    assert m > n
    assert n > 0
    assert k > 0
    assert type(m) == int
    assert type(n) == int
    assert type(k) == int
    a = (m*m - n*n)*k
    b = (2*m*n)*k
    c = (m*m + n*n)*k
    return a,b,c

def mn_pairs(lim):
    m = 1
    while True:
        for n in range(1,m):
            yield (m,n)
        m += 1
        if m > lim:
            break

print("Primitive Pythagorean Triples")
for m,n in mn_pairs(12):
    par = m%2 + n%2
    if gcd(m,n) == 1 and par != 2:
        T = euclid_triple(m,n)
        print(T)