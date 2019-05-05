from ContinuedFractions import cfrac_convergents,cfrac_func, cfrac
from math import sqrt

print("Convergents of the Golden Ratio")
for C in cfrac_convergents([1,1,1,1,1,1,1,1,1,1,1]):
    print("{:<6}  {}".format(str(C),C.digits(5)))
    
print("\nConvergents of the Sqrt of 2")
for C in cfrac_convergents([1,2,2,2,2,2,2]):
    print("{:<6}  {}".format(str(C),C.digits(5)))
    
print("\nCalculation Continued Fraction Representations for Square Roots")
for i in [2,3,5,6,7,8]:
    E = cfrac_func(sqrt,i,5)
    print(f"√{i} ≈ {E} = {str(cfrac(E)):<7} ≈ {cfrac(E).digits(3)}")    
