from FareySequence import farey_sequence
from HarmonicSequence import harmonic_sequence

for i in harmonic_sequence(10):
    print(i)

print()

for i in range(1,6):
    F = farey_sequence(i)
    s = ""
    for f in F:
        s += str(f) + " "
    print(s)