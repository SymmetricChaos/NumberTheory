from RationalsType import Rational

def farey_sequence(n):
    assert type(n) == int
    assert n > 0
        
    S = [Rational(0,1), Rational(1,n)]
    while True:
        A = S[-2]
        B = S[-1]
        k = (n + A.d) // B.d
        p = k * B.n-A.n
        q = k * B.d-A.d
        if p > n:
            break
        S.append(Rational(p,q))
    return S

for i in range(1,7):
    F = farey_sequence(i)
    print(F)