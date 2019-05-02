from ContinuedFractions import cfrac_convergents


print("Convergents of the Golden Ratio")
for C in cfrac_convergents([1,1,1,1,1,1,1,1,1,1,1]):
    print("{:<6}  {}".format(str(C),C.digits(5)))
    
print("\nConvergents of the Sqrt of 2")
for C in cfrac_convergents([1,2,2,2,2,2,2]):
    print("{:<6}  {}".format(str(C),C.digits(5)))