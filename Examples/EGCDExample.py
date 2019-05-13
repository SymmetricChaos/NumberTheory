from ModularArithmetic.Utils import gcd, lcm, egcd
from GeneralUtils import equal_spacing

a, b = 620,380
print("The greatest common denominator of two natural numbers is the largest number that is a factor of both.")
print(f"The GCD of the set {a} and {b} is {gcd(a,b)}")

print("\nCalculating the GCD can be done reasonably quickly using the Euclidean Algorithm.")

a, b = 629,777
print(f"\nThis algorithm procedes by subtracting the smaller number from the larger until the numbers are equal. Here we find the GCD of {a} and {b}.\n")
equal_spacing([a,b],5,'left')
while a != b:
    if a > b:
        a = a-b
    else:
        b = b-a
    equal_spacing([a,b],5,'left')
        
print(f"\nSo the their greatest common denominator is {gcd(a,b)}")

print("\nThere are slightly more efficient methods of calculation available today.")

S = [5610,24871,1683]
print("\nWe can also find the GCD of a set of numbers")
print(f"\nThe GCD of {S} is {gcd(S)}")

a, b = 629,777
print("\n\n\nThe least common multiple of two natural numbers the smallest number that is a multiple of both.")
print(f"The LCM of the set {a} and {b} is {lcm(a,b)}")

print("\nIf the GCD is known then it is easy to find the LCM as it is the product of the numbers divided by their GCD.")


print("\n\n\nBézout's identity says that given a and b if their GCD is g then there are integers x and y such that\ng = ax + by")
print("\nA small change to the Euclidean Algorithm returns these numbers as well.")
a, b = 629,407
g,x,y = egcd(a,b)
print(f"{a*x+b*y} = {a}*{x} + {b}*{y}")

