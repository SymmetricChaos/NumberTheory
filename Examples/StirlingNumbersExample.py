from Combinatorics import stirling_numbers_1, stirling_numbers_2
from GeneralUtils import equal_spacing

print("Stirling Numbers of the First Kind")
for i in range(8):
    L = []
    for j in range(i+1):
        L.append(stirling_numbers_1(i,j))
    equal_spacing(L,5,'left')
print("\nStirling Numbers of the Second Kind")
for i in range(8):
    L = []
    for j in range(i+1):
        L.append(stirling_numbers_2(i,j))
    equal_spacing(L,4,'left')