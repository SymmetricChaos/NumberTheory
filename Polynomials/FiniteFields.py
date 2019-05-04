from Polynomials.PolynomialType import Polynomial

# Examples of finite field of prime power order
# MAYBE?

A = Polynomial([2,1],3)
B = Polynomial([2,1],3)
P = Polynomial([-1,-1,0,1],3)
print(P)
for i in range(14):
    print(A.coef)
    A = (A * B)%P