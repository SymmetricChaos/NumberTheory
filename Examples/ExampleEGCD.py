from ModularArithmetic.Utils import gcd, lcm

S = [629,777,407]
print("The greatest common denominator of natural numbers is the largest number that is a factor of all of them.")
print(f"The GCD of the set {S} is {gcd(S)}")

print("\n\nThe least common multiple is the smallest number that is a multiple of all of them.")
print(f"The LCM of the set {S} is {lcm(S)}")
