from Polynomials.PolynomialOOP import *
from numpy import linspace
A = polynomial([1,2,3,10],5)
B = polynomial([4,3,4,2],5)
C = polynomial([1,2,3,4],5)
print(A)
print(repr(A))

print(A+B)

print(A*B)

print(A.evaluate(linspace(-5,5,20)))


R = polynomial([9,6,7,1,3,4,5],9)
S = polynomial([1,1,0,1,1,0,0,0,1],9)
print(S//R)
print(S%R)

#print(dir(1.1))