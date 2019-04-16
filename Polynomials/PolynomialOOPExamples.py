from Polynomials.PolynomialOOP import polynomial#, set_modulus, runtime_constants

#set_modulus(9)
#print(runtime_constants)

A = polynomial([7,2,0,5],11)
B = polynomial([12,1,3],11)

print("If we write\npolynomial([7,2,0,5],11)\nthat represents")
print(A)
print("\nIf we use a coefficient that is too large it will be reduced. So if we write\npolynomial([12,1,3],11)\nthat represents")
print(B)

print("\nWe can do a lot of familiar arithmetic using polynomials. In the following examples\nA = ",A,"\nB = ",B)

print()
print("A + B = ",A+B)
print("A * B = ",A*B)
print("A / B = ",A//B)
print("A % B = ",A%B)
#print("dx A  = ",A.derivative())

