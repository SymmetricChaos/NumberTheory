from Polynomials.PolynomialOOP import polynomial

cA = [-14,0,-12,1]
cB = [5,-3,1]
A = polynomial(cA)
B = polynomial(cB)

print("For computation it is easiest to store polynomial is ascending order starting with the lowest coefficient. When writing them out is it traditional to do so starting with the highest coefficient.")

print("\nBecause of this \npolynomial({}) = {}".format(cA,A))

print("\n\nWe can do a lot of familiar arithmetic using polynomials. In the following examples\nA = ",A,"\nB = ",B)

print("\n")
print("A + B =",A+B)
print("A - B =",A-B)
print("A * B =",A*B)
print("A ^ 2 =",A**2)
print("A / B =",A/B)
print("A % B =",A%B)

C = A / B
D = A % B
if A == C*B+D:
    print("\nDivision works correctly")
else:
    print("\nSomething went wrong with division")
    print("C * B =", C*B)
    print("C * B + D =",C*B+D)

print("\nThe derivative is also available.")
print("A' =",A.derivative())
print("\nAs is negation.")
print("-A =",-A)