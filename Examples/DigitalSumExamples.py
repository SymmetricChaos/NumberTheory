from Computation import digital_sum, additive_persistence
from random import randint

lo, hi = 100000000,999999999
print("The digital sum, which is the sum of the digits of a number, is used in recreational mathematics. It can also be useful in elementary math for finding properties of numbers that can easily be calculated by hand.")

print("\nThe digital sums of some random numbers")
for i in range(10):
    r = randint(lo,hi)
    print(f"{r} ⟶ {digital_sum(r)}")
    
print("\n\nThe digital root of a number takes the successive digital sums of a number until a dingle digit is reached")

print("\nThe digital roots of some random numbers")
for i in range(5):
    r = randint(lo,hi)
    print(r,end="")
    while r > 9:
        print(" ⟶ ",end="")
        r = digital_sum(r)
        print(r,end="")
    print()
    
print("\nIf the digital root of a number is 3, 6, or 9 then the number is divisible by 3.")


print("\n\nThe number of steps needed to reach the digital root is the additive persistence of a number.")
print("\nThe persistence of some random numbers")
for i in range(10):
    r = randint(lo,hi)
    print(f"{r} ⟶ {additive_persistence(r)}")