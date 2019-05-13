from Other.Factorization import factorization, prime_factorization
from GeneralUtils import list_to_prod

N = 22200778
pFacs = prime_factorization(N)
facs = factorization(N)
print("Every number has a unique representation as the product of prime numbers. For example:")
print(f"{list_to_prod(pFacs)} = {N}")

print("\nThe total number of factors of a number cannot be two to the power of the number of prime factors.")
print(facs)