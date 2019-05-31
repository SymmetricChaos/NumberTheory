# The figurate numbers can be described by a quadratic 
# equation. This makes it possible to find a root in terms
# of figurate numbers other than squares

# For example the triangular numbers
# x = 0.5b(b+1)
# Can be rearranged as
# x = 0.5b^2 + .5b
# 2x = b^2 + b
# 0 = b^2 + b - 2x

# Then the quadratic formula can give us the solution
# (the coefficient are a = 1, b = 1, c = -2x)

# Ignoring the negative solution
# root = ( -1 + sqrt(1-8x) )/2

# We can generalize this by using the formula for general
# figurate number.

# x = ( n^2*(S-2)-n*(S-4) ) * 0.5
# 2x = n^2*(S-2)-n*(S-4)
# 0 = n^2*(S-2)-n*(S-4) - 2x
# (the coefficient are a = (S-2), b = -(S-4), c = -2x)
    
# Ignoring the negative solution
# root = ( (S-4) + sqrt((S-4)^2-4*(S-2)*-2x) ) / 2*(S-2)
# simplifying
# root = ( (S-4) + sqrt((S-4)^2 + (S-2)8x) ) / 2*(S-2)


from math import sqrt

def figurate_root(n,S):
    A = S-4
    B = S-2
    return ( A + sqrt( A**2 + B*8*n ) ) / (2*B)

print("Various Figurate Roots\n")
print("     Triangular  Square     Pentagonal")
for i in range(1,16):
    a = figurate_root(i,3)
    b = figurate_root(i,4)
    c = figurate_root(i,5)
    print(f"{i:<2}   {a:.3f}       {b:.3f}      {c:.3f}")
    
