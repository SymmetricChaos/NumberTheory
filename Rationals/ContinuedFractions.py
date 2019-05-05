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
    
    yield Rational(N[-1],D[-1])
    
    while con < len(L)+1:
        N.append( L[con-1] * N[con-1] + N[con-2] )
        D.append( L[con-1] * D[con-1] + D[con-2] )

        yield Rational(N[-1],D[-1])
        
        con += 1
        
def cfrac_expansion(rational):
    assert type(rational) == Rational
    
    L = []
    while True:
        w,f = rational.mixed_form()
        L.append(w)
        if f == 0:
            break
        rational = f.inv()

    return L