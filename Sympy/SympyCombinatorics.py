from sympy.combinatorics import Permutation, symmetric
from sympy.interactive import init_printing

S = [4,0,1,3,2]
P = Permutation(S)
print(f"Direction Notation:\n{P.list()}")
print(f"\nOne Line Notation:\n{P}")
print(f"\nNumber of Permutations:{P.cardinality}")
print(f"\nIs Even: {P.is_even}")
print(f"Is Odd: {P.is_odd}")
print(f"Parity: {P.parity()}")
print(list(symmetric(4)))