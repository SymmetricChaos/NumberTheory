from PolynomialRepresentation import poly_add, poly_divmod, poly_print

# The finite field GF(2^8) with 256 elements has various expressions


def Rijndael_add(P,Q):
    
    # The Rijndael polynomial 
    R = [1,1,0,1,1,0,0,0,1]
    
    S = poly_add(P,Q,2)
    S = poly_divmod(S,R,2)[1]
    
    poly_print(S)
    

Rijndael_add([0,1,1,0,1,1,1],[1,0,1,0,1])