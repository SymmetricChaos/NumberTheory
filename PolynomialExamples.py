from PolynomialRepresentation import poly_norm, poly_degree, poly_pad, \
                                     poly_print, poly_add, poly_mult, \
                                     poly_divmod, eq_print

# Four polynomials
P = [-42,1,-12,-1]
Q = [-3,1,0,0]
R = [9,6,7,1,3,4,5]
S = [1,1,0,1,1,0,0,0,1]

print("Four Polynomials in Ascending Vector Form")
for i in [P,Q,R,S]:
    eq_print(i,3)

print("\n\nThe Same Polynomials in Descending Written Form")
for i in [P,Q,R,S]:
    poly_print(i)
    
print("\n\nPolynomials With Degree")
for i in [P,Q,R,S]:
    print("Degree {}".format(poly_degree(i)),i)
    
print("\n\nFinite Field Addition GF(3^3)")
print(P)
print(R)
print(poly_add(P,R,27))
