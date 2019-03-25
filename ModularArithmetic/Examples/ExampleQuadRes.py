from ModularArithmetic import find_quad_residue
    
for i in range(2,22):
    qr = find_quad_residue(i)
    print("{:<{}} {}".format(i,2,qr))