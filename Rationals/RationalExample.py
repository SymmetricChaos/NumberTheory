from RationalsType import Rational

A = Rational(4,10)
B = Rational(7,19)
C = Rational(71,22)
D = A/B

print("Addition and Subtraction")
print(A,"+",B,"=",A+B)
print(A,"-",B,"=",A-B)
print(A,"-",A,"=",A-A)

print("\nMultiplication and Division")
print(A,"*",B,"=",A*B)
print(A,"/",B,"=",A/B)
print(A,"*",A.inv(),"=",A/A)

print("\nMediant")
print(A,"⊕",B,"=",A.mediant(B))


print("\nInteger Powers")
print(A,"**",3,"=",A**3)
print(B,"**",4,"=",B**4)

print("\nMixed Fraction Form")
M = C.mixed_form()
sM = " + ".join([str(m) for m in M])
print(C,"=",sM)

print("\nDecimal Digits")
print(A,"=",A.digits(10))
print(B,"=",B.digits(10))
print(C,"=",C.digits(10))

print("\nSize Comparison")
print(A,">",B,"=",A>B)
print(C,"<=",A,"=",C<=A)