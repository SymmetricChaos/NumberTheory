from EllipticCurves.EllipticPoint import Elliptic_Curve, Elliptic_Point, cyclic_subgroup, cyclic_subgroups

C = Elliptic_Curve(2,3,223)
P = C.points()
a = Elliptic_Point(P[12][0],P[12][1],C)

print([i.coords for i in cyclic_subgroup(a)])
print()
print([len(g) for g in cyclic_subgroups(C)])