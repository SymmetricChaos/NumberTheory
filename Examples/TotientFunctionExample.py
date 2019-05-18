from ModularArithmetic import totient, coprimes
from random import randint

print("Euler's totient function (usually written as Φ) counts the natural number less than N which are coprime to N.\n")
for i in range(3):
    N = randint(10,99)
    print(f"Φ({N}) = {totient(N)}")
    print(coprimes(N))
    print()