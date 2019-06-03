from Polynomials.PolynomialType import Polynomial

print("The rising factorial can be expressed as a series of polynomials.")

R = Polynomial([0,1])
for i in range(6):
    print(R)
    R = R * Polynomial([i+1,1])
