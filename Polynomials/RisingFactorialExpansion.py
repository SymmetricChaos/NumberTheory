from PolynomialType import Polynomial

R = Polynomial([0,1])
for i in range(6):
    print(R)
    R = R * Polynomial([i+1,1])
