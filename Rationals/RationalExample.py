from RationalsType import Rational

A = Rational(4,10)
B = Rational(7,16)
C = Rational(71,18)
D = A/B

print(A,"+",B,"=",A+B,"\n")
print(C,"+",B,"=",C+B,"\n")
print(A,"-",A,"=",A-A,"\n")
print(A,"*",B,"=",A*B,"\n")
print(A,"/",B,"=",A/B,"\n")
print(B,"*",D,"=",B*D,"\n")
print(A,"+",A.inv(),"=",A+A.inv(),"\n")
print(A,"**",3,"=",A**3,"\n")
print(C.mixed_form())