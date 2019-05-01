from RationalsType import Rational

def farey_sequence(n):
    S = set()
    for a in range(n):
        for b in range(1,n+1):
            R = Rational(a,b)
            if R < 1:
                S.add(R)
    S = list(S)
    S.sort()
    return S
        
F = farey_sequence(8)
print(F)