from Sequences.MathUtils import poly_mult
from Sequences.NiceErrorChecking import require_iterable, require_integers

def taylor_terms(A,c=0):
    
    require_iterable(["A"],[A])
    require_integers(["c"],[c])
    
    P = [1]
    
    for a in A:
        yield poly_mult([a],P)
        
        P = poly_mult([1,-x],P)