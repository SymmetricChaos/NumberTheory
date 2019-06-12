from Polynomials import Polynomial

print("Number of Ways to Get a Sum with N Dice")

D1 = Polynomial([1]*6)
D2 = D1**2
D3 = D1**3
D4 = D1**4

L = [D1**i for i in range(1,5)]

for n,poly in enumerate(L,1):
    for val,num in enumerate(poly,n):
        print(f"{val:<2} = {num}")
    print()
