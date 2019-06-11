from Combinatorics.Choose import choose

# The Narayana numbers count the number of Dyck words of length 2m that contain n peak

def narayana_number(m,n):
    assert type(m) == int
    assert type(n) == int
    assert n >= m >= 1
    a = choose(n,m)
    b = choose(n,m-1)
    return (a*b)//n

for n in range(1,6):
    for m in range(1,n+1):
        print(narayana_number(m,n))
    print()