
from Computation.RootFinding import int_root, is_square

print("Fermat's method for factorization relies on the difference squares.")
print("\na^2 - b^2 = (a+b)(a-b)")
print("\nThis means that any number which can be written as the difference of two squares must have a+b and a-b as factors.")
a = 17
b = 6
p = (a+b)*(a-b)
print(f"\nFor example {p} can be factored as {a+b} and {a-b}")
print("\nTo factor a number N we can see that\nN = a^2 - b^2\nimplies\na^2 - N = b^2")
print("\nThat means we find a factorization by repeatedly subtracting squares from N until the result is a square.")

N = 1521

print(f"\nLet's try to factor {N}\n")

a = int_root(N)
factor_found = False
while True:
    a += 1
    b2 = a**2-N
    print(f"a^2   = {a**2}\na^2-N = {b2}\n")
    if is_square(b2):
        print(f"{b2} is square")
        factor_found = True
        print(f"We can factor {N} as\n{a-int_root(b2)} * {a+int_root(b2)}")
        break
