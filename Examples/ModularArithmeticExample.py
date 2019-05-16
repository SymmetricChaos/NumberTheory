from ModularArithmetic import modinv
from random import randint

mod = 11

print("In modular arithmetic addition and multiplication work normally unless the result is greater than the modulus. In that case the result is the remainder after dividing by the modulus.")
print(f"\nFor our examples the modulus will be {mod}.\n")
for i in range(5):
    a, b = randint(0,9), randint(0,9)
    print(f"{a} + {b} = {(a+b)%mod} mod {mod}")
print()
for i in range(5):
    a, b = randint(0,9), randint(0,9)
    print(f"{a} × {b} = {(a*b)%mod} mod {mod}")
    
print("\nSubtraction is also very simple as it is addition backward.\n")
for i in range(5):
    a, b = randint(0,9), randint(0,9)
    print(f"{a} - {b} = {(a-b)%mod} mod {mod}")
    
print("\nDivision, however, is a bit more complicated. While ordinary division is still possible a more intersting inverse of multiplication is available.")
print("\nConsider the multiplication")
while True:
    a, b = randint(0,9), randint(0,9)
    if (a*b)%mod == 1:
        print(f"{a} × {b} = {(a*b)%mod} mod {mod}")
        print(f"\nWe can say that {b} is the multiplicative inverse of {a} (modulo {mod}) because their product is 1")
        break

print("\nFinding the modular multiplicative inverse of a number is not as trivial as .")