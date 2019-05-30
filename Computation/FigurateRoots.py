# The figurate numbers can be described by a quadratic equation

# For example the triangular numbers
# a = 0.5b(b+1)
# Can be rearranged as
# a = 0.5b^2 + .5b
# 2a = b^2 + b
# 0 = b^2 + b - 2a

# Then the quadratic formula can give us the solution

# b = ( -1 + sqrt(1-8a) )/2

from math import sqrt

def triangular_root(n):
    return ( -1 + sqrt(1+8*n) )/2

for i in range(1,10):
    print(triangular_root(i))