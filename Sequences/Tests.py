from Sequences import *

for i,j in enumerate(naturals(10,7),7):
    print(i,j)
print()

for i,j in enumerate(fibonacci(10,7),7):
    print(i,j)
print()

for i,j in enumerate(lucas(10,7)):
    print(i,j)
print()

for i,j in enumerate(pell(10,7),7):
    print(i,j)
print()

for i,j in enumerate(pell_lucas(10,7),7):
    print(i,j)
print()

for i,j in enumerate(tribonacci(10,7),7):
    print(i,j)
print()

for i,j in enumerate(P_fibonacci(10,7,P=3),7):
    print(i,j)
print()

for i,j in enumerate(PQ_fibonacci(10,P=1,Q=2)):
    print(i,j)
print()

for i,j in enumerate(padovan(10)):
    print(i,j)
print()