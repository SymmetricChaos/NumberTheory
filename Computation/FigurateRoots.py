# The figurate numbers can be described by a quadratic equation

# For example the triangular numbers
# x = 0.5b(b+1)
# Can be rearranged as
# x = 0.5b^2 + .5b
# 2x = b^2 + b
# 0 = b^2 + b - 2x

# Then the quadratic formula can give us the solution
# (the coefficient are a = 1, b = 1, c = -2x)

# Ignoring the negative solution
# b = ( -1 + sqrt(1-8x) )/2

from math import sqrt

def triangular_root(n):
    return ( -1 + sqrt(1+8*n) )/2

for i in range(1,10):
    print(triangular_root(i))