from PolynomialType import Polynomial



def poly_GCD(A,B):
    if B.coef == [0]:
        return A
    else:
        return poly_GCD(B,A%B)
    

if __name__ == '__main__':
    P = Polynomial([6,7,1])
    Q = Polynomial([-6,-5,1])
    R = Polynomial([1,1])
    print(P)
    print(Q)
    
    print("gcd should be (x+1)")
    print(poly_GCD(P,Q))
    
    print(R)
    for i in divmod(P,R):
        print(i)