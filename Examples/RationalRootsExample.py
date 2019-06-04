from Polynomials import Polynomial, rational_roots
from random import randint

print("Examples of polynomials with rational roots.\n")

ctr = 0
while ctr < 3:
    co = [randint(-99,99) for i in range(5)]
    
    #P = Polynomial([6,-7,0,1])
    P = Polynomial(co)
    R = rational_roots(P)
    
    if len(R) > 0:
        print(P)
        print(f"Roots: {R}")
        ctr += 1
        print()
        
print("Polynomials do not necessarily have any ration roots.")