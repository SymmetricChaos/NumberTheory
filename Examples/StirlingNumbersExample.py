from Computation import stirling_numbers_1, stirling_numbers_2

for i in range(9):
    for j in range(i+1):
        print(stirling_numbers_1(i,j),end=" ")
    print()
print()
for i in range(9):
    for j in range(i+1):
        print(stirling_numbers_2(i,j),end=" ")
    print()