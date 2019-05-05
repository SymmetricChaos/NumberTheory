from RationalsType import Rational

def cfrac(L):
    a,b = L[-1],1
    del L[-1]
    for i in reversed(L):
        A = Rational(i,1)
        B = Rational(b,a)
        C = A+B
        a = C.n
        b = C.d
    return Rational(a,b)

def cfrac_convergents(L):
    N = [1,L[0]]
    D = [0,1]
    con = 2
    while con < len(L):
        yield Rational(N[-1],D[-1])
        N.append( L[con] * N[con-1] + N[con-2] )
        D.append( L[con] * D[con-1] + D[con-2] )
        con += 1
    yield Rational(N[-1],D[-1])