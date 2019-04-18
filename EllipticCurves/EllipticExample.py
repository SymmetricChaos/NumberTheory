from EllipticCurves import Elliptic_Curve, Elliptic_Point, cyclic_subgroup, cyclic_subgroups


a, b, f = 5, 2, 13
C = Elliptic_Curve(a,b,f)
P = C.points()

print("The elliptic curve y^2 = x^3 + {}x + {} over GF({}) has {} points on it, including the point at infinity.".format(a,b,f,len(P)))
print("\nThose points are:")
print(P)


print("\nIt is possible to add together points on an elliptive curve. In fact they form a commutative group.")
A = Elliptic_Point(P[3][0],P[3][1],C)
B = Elliptic_Point(P[8][0],P[8][1],C)
print(A,"+",B,"=",A+B)

print("\nThe point at infinity is the identity element.")
print(C.identity,"+",B,"=",C.identity+B)
print(B,"+",C.identity,"=",C.identity+B)

print("\nScalar multiplication, adding a point to itself repeatedly, is also defined.")
print(A,"* 2 =", A*2)
print(A,"* 5 =", A*4)

print("\nEach of these points generates a cyclic subgroup with an order that is a factor of {}.".format(len(P)))

print("\nFor example repeated addition by {} gives the subgroup".format(A))
print([i.coords for i in cyclic_subgroup(A)])

print("\nThe order of each subgroup is:")
print([len(g) for g in cyclic_subgroups(C)])

