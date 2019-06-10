from Combinatorics import lobb_number

print("The Lobb numbers")

for i in range(6):
    for j in range(i+1):
        print(lobb_number(j,i),end = " ")
    print()