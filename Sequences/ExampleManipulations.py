from SequenceManipulation import simple_test, interleave, sequence_apply, chunk_by_n, partial_sums
from Simple import naturals, constant
from Recurrence import companion_pell
from Aliquot import amicable_pairs

A142150 = interleave(naturals(0),constant(0))
A001333 = sequence_apply(companion_pell(),lambda x: x//2)
A259180 = chunk_by_n(amicable_pairs(),2)
A000217 = partial_sums(naturals())

print("A142150")
simple_test(A142150,10,"0, 0, 1, 0, 2, 0, 3, 0, 4, 0")

print("\nA001333")
simple_test(A001333,10,"1, 1, 3, 7, 17, 41, 99, 239, 577, 1393")

print("\nA259180 by pairs")
simple_test(A259180,4,"(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)")

print("\nA000217")
simple_test(A000217,10,"0, 1, 3, 6, 10, 15, 21, 28, 36, 45")
