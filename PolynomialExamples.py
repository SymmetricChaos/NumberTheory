from PolynomialRepresentation import poly_norm, poly_degree, poly_pad, \
                                     poly_print, poly_add, poly_mult, \
                                     poly_divmod

# Four polynomials
P = [-42,1,-12,-1]
Q = [-3,1,0,0]
R = [9,6,7,1,3,4,5]
S = [1,1,0,1,1,0,0,0,1]

print("Four Polynomials in Ascending Vector Form")
for i in [P,Q,R,S]:
    print(i)

print("\nThe Same Polynomials in Descemding Written Form")
for i in [P,Q,R,S]:
    poly_print(i)
