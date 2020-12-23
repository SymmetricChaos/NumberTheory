from Sequences.MathUtils import poly_mult, poly_sum
from Sequences.NiceErrorChecking import require_iterable, require_integers
from Sequences.Simple import naturals

def taylor_terms(A,c=0):
    """
    Coefficients of each term of the Talyor Series defined by the sequence A and constant c\n
    """
    
    require_iterable(["A"],[A])
    require_integers(["c"],[c])
    
    P = [1]
    
    for a in A:
        yield poly_mult([a],P)
        
        P = poly_mult([1,-c],P)


def taylor_sums(A,c=0):
    """
    Coefficients of each partial sum of the Talyor Series defined by the sequence A and constant c\n
    """
    
    require_iterable(["A"],[A])
    require_integers(["c"],[c])
    
    S = [0]
    
    for P in taylor_terms(A,c):
        S = poly_sum(P,S)
        
        yield S





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    simple_test(taylor_terms(naturals(1),1),5,
                "")
    
    simple_test(taylor_sums(naturals(1),1),5,
                "")