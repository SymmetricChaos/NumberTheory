from Rationals import farey_sequence

print("The Farey Sequences are the sequences of unique fractions between 0 and 1 with denominators less than or equal to n.")
print("Here is the Farey sequence F(9).")
F = farey_sequence(9)

n = 0
for ctr,i in enumerate(F):
    if ctr % 9 == 0:
        print()
    print(i,end = "  ")