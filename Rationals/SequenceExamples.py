from FareySequence import farey_sequence
from HarmonicSequence import harmonic_sequence

print("Partial Sums of the Harmonic Series")
for i in harmonic_sequence(10):
    print(i)

print()

print("Farey Sequences")
for i in range(1,10):
    F = farey_sequence(i)
    print(F)