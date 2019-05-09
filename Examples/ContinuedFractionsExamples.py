from Rationals import Rational, cfrac_convergents,cfrac_func, cfrac
from math import sqrt

print("Convergents of the Golden Ratio")
for C in cfrac_convergents([1,1,1,1,1,1,1,1,1,1,1]):
    print("{:<6}  {}".format(str(C),C.digits(5)))
    
    
print("\n\nConvergents of √2")
for C in cfrac_convergents([1,2,2,2,2,2]):
    print("{:<6}  {}".format(str(C),C.digits(5)))

print("\nDifferences of Successive Convergents of √2")
E = [i for i in cfrac_convergents([1,2,2,2,2,2,2])]
for i in range(len(E)-1):
    d = E[i]-E[i+1]
    s = " " if d > 0 else ""
    print(f"{s}{str(d)}")

A = Rational(20461,1793)
print(f"\n\nContinued Fraction of {str(A)}")
print(A.cfrac())


print(f"\nConvergents")
for C in cfrac_convergents(A.cfrac()):
    print(f"{str(C)}")


print("\n\nContinued Fraction for Square Roots")
for i in [2,3,5,6,7,8]:
    E = cfrac_func(sqrt,i,5)
    print(f"√{i} ≈ {E} = {str(cfrac(E)):<7} ≈ {cfrac(E).digits(3)}")    
