from PolynomialOOP import polynomial

R = polynomial([0,1])
for i in range(6):
    print(R)
    R = R * polynomial([i+1,1])
