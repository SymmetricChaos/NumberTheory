from ModularArithmetic import primitive_roots, coprimes, show_congruences

m = 18
print("A number is coprime to another if and only if those numbers have no common factors.")
print("\nOften we are most interested in the natural numbers coprime to and less than a given number.")
print(f"\nFor example the numbers coprime to {m} are {coprimes(m)}")
print("\nA related concept is that of primitive roots.")
print("\nA primitive root modulo some number is one such that its powers modulo that number include all the numbers coprime of that number.")
r = primitive_roots(m)
print(f"\nThe primitive roots of {m} are {r}")

print()
for i in r:
    show_congruences(i,m)