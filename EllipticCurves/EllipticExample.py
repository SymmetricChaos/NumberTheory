from EllipticCurves.EllipticPoint import Elliptic_Curve, Elliptic_Point, cyclic_subgroup, cyclic_subgroups


a, b, f = 2, 3, 29
C = Elliptic_Curve(a,b,f)
P = C.points()
p = Elliptic_Point(P[8][0],P[8][1],C)


print("The elliptic curve y^2 = x^3 + {}x + {} over GF({}) has {} points on it.".format(a,b,f,len(P)))
print("\nThose points are:")
print(P)

print("\nEach of these points generates a cyclic subgroup with an order that is a factor of {}.".format(len(P)))

print("\nFor example repeated addition by {} gives the subgroup".format(P[8]))
print([i.coords for i in cyclic_subgroup(p)])

print("\nThe order of each subgroup is:")
print([len(g) for g in cyclic_subgroups(C)])