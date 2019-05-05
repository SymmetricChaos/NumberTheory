from RationalType import Rational
from ContinuedFractions import cfrac_convergents,cfrac_func, cfrac
from math import sqrt

print("Convergents of the Golden Ratio")
for C in cfrac_convergents([1,1,1,1,1,1,1,1,1,1,1]):
    print("{:<6}  {}".format(str(C),C.digits(5)))
    
    
print("\n\nConvergents of √2")
for C in cfrac_convergents([1,2,2,2,2,2,2]):
    print("{:<7}  {}".format(str(C),C.digits(5)))


A = Rational(534,342)
print(f"\n\nContinued Fraction Representations of {str(A)}")
print(A.cfrac())


print(f"\nContinued Convergents of {str(A)}")
for C in cfrac_convergents(A.cfrac()):
    print("{:<6}  {}".format(str(C),C.digits(5)))


print("\n\nContinued Fraction Representations for Square Roots")
for i in [2,3,5,6,7,8]:
    E = cfrac_func(sqrt,i,5)
    print(f"√{i} ≈ {E} = {str(cfrac(E)):<7} ≈ {cfrac(E).digits(3)}")    


print("\n\nDifferences of Successive Convergents of √2")
E = [i for i in cfrac_convergents([1,2,2,2,2,2,2])]
for i in range(len(E)-1):
    d = E[i]-E[i+1]
    s = " " if d > 0 else ""
    print(f"{s}{str(d)}")