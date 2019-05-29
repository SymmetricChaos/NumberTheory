from Computation import binary_partition, exp_by_squaring
from GeneralUtils import list_to_prod
print("The naieve method for calculating exponents is to multiply a number by itself n times. This requires n-1 multiplications. However there are much more efficient ways to calculate positive integer exponents.")
print("In general the most efficient method is difficult to find. However it is easy to find very fast methods. In particular repeated squaring is quite efficient compare to the naieve method.")

b = 2
e = 471
print(f"\nFor example we can calculate {b}^{e} by seeing that, by the rules of exponents, it can be rewritten as:")

bpart = binary_partition(e)
bpart_str = [f"2^{2**i}" for i in bpart]
print(list_to_prod(bpart_str))

print("\nThese particular exponents are easy to calculate because they are the result of repeated squaring.")
print(f"{b}^2  = {b}^1 * {b}^1")
print(f"{b}^4  = {b}^2 * {b}^2")
print(f"{b}^16 = {b}^4 * {b}^4")

print("\nThis 'ladder' need only be climbed up about log2(n) steps to get all the terms needed. The binary expansion of the number, which is easy enough to calculate, determines which terms are to be chosen.")

print(f"\nTo calculate {b}^{e} naievely requires {e-1} multiplications.")
print(f"\nUsing the squaring method only {len(bpart)+max(bpart)-1} are needed.")
