from FareySequence import farey_sequence
from HarmonicSequence import harmonic_series, alternating_harmonic_series

print("Partial Sums of the Harmonic Series")
for i in harmonic_series(10):
    print(f"{str(i):<9}  {i.digits(5)}")


print("\nPartial Sums of the Alternating Harmonic Series")
for i in alternating_harmonic_series(9):
    print(f"{str(i):<9}  {i.digits(5)}")


print("\nFarey Sequences")
for i in range(1,5):
    F = farey_sequence(i)
    print(F)
