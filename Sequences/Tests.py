from Sequences import naturals, fibonacci, lucas, pell, pell_lucas, tribonacci,\
                      P_fibonacci

for i,j in enumerate(naturals(10,7),7):
    print(i,j)
print()

for i,j in enumerate(fibonacci(10,7),7):
    print(i,j)
print()

for i,j in enumerate(lucas(10,7)):
    print(i,j)
print()

for i,j in enumerate(pell(10)):
    print(i,j)
print()

for i,j in enumerate(pell_lucas(10)):
    print(i,j)
print()

for i,j in enumerate(tribonacci(10)):
    print(i,j)
print()

for i,j in enumerate(P_fibonacci(10,7,P=3),7):
    print(i,j)
print()