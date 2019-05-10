from ModularArithmetic.Utils import gcd, lcm, egcd

S = [629,777,407]
print("The greatest common denominator of natural numbers is the largest number that is a factor of all of them.")
print(f"The GCD of the set {S} is {gcd(S)}")

print("\n\nThe least common multiple is the smallest number that is a multiple of all of them.")
print(f"The LCM of the set {S} is {lcm(S)}")

print("\nIf the GCD is known then it is easy to find the LCM as it is the product of the set divided by their GCD.")

print("\n\nCalculating the GCD can be done reasonably quickly using the Euclidean Algorithm.")

print("\n\nBézout's identity says that given a and b if their GCD is g then there are integers x and y such that\ng = ax + by")
print("\nA small change to the Euclidean Algorithm returns these numbers as well.")
a, b = 629,407
g,x,y = egcd(a,b)
print(f"{a*x+b*y} = {a}*{x} + {b}*{y}")

