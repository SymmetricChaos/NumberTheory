from ModularArithmetic import find_quad_residue


print("The quadratic residues of a numbers are the remainders of squares when divided by that number.")
for i in range(2,22):
    qr = find_quad_residue(i)
    print("{:<{}} {}".format(i,2,qr))