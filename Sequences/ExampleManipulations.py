from SequenceManipulation import simple_test, interleave, sequence_apply
from Simple import naturals, constant
from Recurrence import companion_pell

A142150 = interleave(naturals(0),constant(0))
A001333 = sequence_apply(companion_pell(),lambda x: x//2)

print("A142150")
simple_test(A142150,10,"0, 0, 1, 0, 2, 0, 3, 0, 4, 0")

print("\nA001333")
simple_test(A001333,10,"1, 1, 3, 7, 17, 41, 99, 239, 577, 1393")

