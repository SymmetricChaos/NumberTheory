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

