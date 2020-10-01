from Sequences.Primes import odd_primes
from Sequences.Simple import odds, naturals
from Sequences.MathUtils import egcd, prime_factorization, legendre_symbol, nth_sign

def legendre_symbols():
    """
    Irreguar Array of Legendre Symbols
    OEIS A226520 (skipping first two)
    """
    
    for p in odd_primes():
        yield 0
        for a in range(1,p):
            out = pow(a,(p-1)//2,p)
            if out == 1:
                yield 1
            else:
                yield -1


def jacobi_symbols():
    """
    Irreguar Array of Jacobi Symbols
    OEIS (not A226520)
    """
    
    for p in odds():
        for a in range(p):
            fac = prime_factorization(p)
            out = 1
            for f in fac:
                out *= legendre_symbol(a,p)
            yield out


def mobius_function():
    """
    Map of the Mobius Function
    """
    
    yield 1
    
    for n in naturals(2):
        P = prime_factorization(n)
        
        if len(P) == len(set(P)):
            yield nth_sign(len(P))
        else:
            yield 0


def modular_inverses():
    """
    Triangle of Modular Multiplicative Inverses
    OEIS A102057
    """
    
    for a in naturals(2):
        for b in range(1,a):
            g,x,y = egcd(b,a)
            
            if g != 1:
                yield 0
            
            else:
                yield x%a


# def quadratic_residue(m):
#     """
#     Quadratic Residues Modulo M
#     """




if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Triangle of Modular Inverses")
    simple_test(modular_inverses(),18,
                "1, 1, 2, 1, 0, 3, 1, 3, 2, 4, 1, 0, 0, 0, 5, 1, 4, 5")
    
    print("\nIrregular Array of Legendre Symbols")
    simple_test(legendre_symbols(),16,
                "0, 1, -1, 0, 1, -1, -1, 1, 0, 1, 1, -1, 1, -1, -1, 0")
    
    print("\nIrregular Array of Jacobi Symbols")
    simple_test(jacobi_symbols(),16,
                "1, 0, 1, -1, 0, 1, -1, -1, 1, 0, 1, 1, -1, 1, -1, -1")
    
    print("\nMobius Function")
    simple_test(mobius_function(),16,
                "1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0")