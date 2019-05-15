from ModularArithmetic import modinv
from random import randint

mod = 11

print("In modular arithmetic addition and multiplication work normally unless the result is greater than the modulus. In that case the result is the remainder after dividing by the modulus.")
print(f"\nFor our examples the modulus will be {mod}.\n")
for i in range(5):
    a, b = randint(0,9), randint(0,9)
    print(f"{a} + {b} = {(a+b)%mod}")
print()
for i in range(5):
    a, b = randint(0,9), randint(0,9)
    print(f"{a} × {b} = {(a*b)%mod}")